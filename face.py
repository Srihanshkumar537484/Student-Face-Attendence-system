from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime
import cv2

class Face:
    def __init__(self, shrey):
        self.shrey = shrey
        self.shrey.title("Face Attendance System")
        self.shrey.geometry("1530x820+0+0")

        # Images bar
        img = Image.open(r"C:\Users\sva16\OneDrive\Desktop\faceattendancesystem\faceattendancesystem\images\f.jpg")
        img = img.resize((1530, 820), Image.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img)

        photo1 = Label(self.shrey, image=self.photoimg)
        photo1.place(x=0, y=50, width=1530, height=820)

        writee = Label(self.shrey, text="Face Recognition", font=("times new roman", 35, "bold"), bg="white", fg="#660033")
        writee.place(x=0, y=0, width=1530, height=45)

        btn1 = Button(photo1, text="Face Detection Process", command=self.face_capture, font=("times new roman", 15, "bold"), bg="#0E182A", fg="white")
        btn1.place(x=820, y=650)

    # Attendance save
    def attendance(self, i, r, d, n):
        today_date = datetime.now().strftime("%d/%m/%y")

        with open("Shrey.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (d not in name_list) and (n not in name_list)):
                now = datetime.now()
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{d},{n},{dtString},{today_date},Present")

    # Face recognition
    def face_capture(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gra_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gra_image, scaleFactor, minNeighbors)

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                idn, predict = clf.predict(gra_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="",
                    database="face_system"
                )
                my_cursor = conn.cursor()
                try:
                    my_cursor.execute("SELECT name FROM student WHERE id = %s", (idn,))
                    i = my_cursor.fetchone()
                    i = i[0] if i else "Unknown"

                    my_cursor.execute("SELECT roll FROM student WHERE id = %s", (idn,))
                    r = my_cursor.fetchone()
                    r = r[0] if r else "Unknown"

                    my_cursor.execute("SELECT dep FROM student WHERE id = %s", (idn,))
                    d = my_cursor.fetchone()
                    d = d[0] if d else "Unknown"

                    my_cursor.execute("SELECT id FROM student WHERE id = %s", (idn,))
                    n = my_cursor.fetchone()
                    n = n[0] if n else "Unknown"

                except mysql.connector.Error as err:
                    print(f"Database Error: {err}")
                    i, r, d, n = "Unknown", "Unknown", "Unknown", "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"ID: {n}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Name: {i}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                    cv2.putText(img, f"Department: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)

                    self.attendance(i, r, d, n)

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
            return

        def recognize(img, clf, faceCascade):
            draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        # Check if the camera opened successfully
        if not video_cap.isOpened():
            print("Error: Could not open video capture.")
            return

        while True:
            ret, img = video_cap.read()
            if not ret:
                print("Failed to capture image. Exiting...")
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            # Break the loop on Enter key press
            if cv2.waitKey(1) == 13:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    shrey = Tk()
    obj = Face(shrey)
    shrey.mainloop()
