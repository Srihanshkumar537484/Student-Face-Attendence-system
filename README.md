# Student Face Attendance System 🎓📸

**Student Face Attendance System** ek automated solution hai jo facial recognition ka upyog karke attendance register karne ke liye banaya gaya hai. Yeh manual attendance ke samay ko bachata hai aur proxy attendance ki samasya ko khatam karta hai.

## 🌟 Key Features

- **Real-time Face Recognition:** OpenCV aur Python ka use karke live camera se chehre pehchan-na.
- **Automated Logging:** Pehchane gaye student ki attendance turant database mein record ho jati hai.
- **MySQL Integration:** SQL database ka upyog karke student records aur attendance history ko secure rakha gaya hai.
- **CRUD Operations:** Admin asani se naye students add kar sakta hai, details update kar sakta hai, ya purana data delete kar sakta hai.
- **CSV Export:** Attendance data ko Excel ya CSV format mein export karne ki suvidha.

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Computer Vision:** OpenCV (`cv2`)
- **Database:** MySQL
- **Face Recognition:** `face_recognition` library ya `Haar Cascades`
- **GUI (Optional):** Tkinter / CustomTkinter

## 📁 Project Structure


Student-Face-Attendance/
├── dataset/             # Student ki photos ka folder

├── sql/                 # Database schema aur SQL scripts

├── main.py              # Main application entry point

├── attendance.py        # Recognition logic

├── db_helper.py         # SQL connection aur CRUD functions

├── requirements.txt     # Python libraries

└── config.json          # Database credentials

1.⚙️ Installation & Setup
Repository Clone Karein:

Bash
git clone [https://github.com/Srihanshkumar537484/Student-Face-Attendance.git](https://github.com/Srihanshkumar537484/Student-Face-Attendance.git)
cd Student-Face-Attendance
Database Setup:

2.MySQL open karein aur ek database banayein (e.g., attendance_db).
sql/schema.sql ko run karke tables create karein.

3.Dependencies Install Karein:
Bash
pip install -r requirements.txt
Run the Project:

4.Bash
python main.py

💡 How It Works

1.Training: Sabse pehle students ke chehre scan karke dataset folder mein save kiye jate hain.

2.Detection: Jab camera on hota hai, OpenCV har frame mein face detect karta hai.

3.Matching: System captured image ko database mein maujood images se compare karta hai.

4.Attendance: Agar match milta hai, toh current date aur time ke saath SQL table mein entry ho jati hai.
