# Python Automation Toolkit 🛠️

Welcome to my Python Automation repository! This collection features two standalone utilities built from scratch using Python's standard libraries. These tools demonstrate core programming logic, data structures, and file system automation.

---

## 📁 Repository Structure

The projects are organized into dedicated subfolders for clean modular structure:

```text
Python-Automation-Toolkit/
│
├── 📁 Student_Management_System/
│   └── student_management.py      # Console database logbook
│
├── 📁 Automatic_File_Organizer/
│   └── file_organizer.py          # Smart file sorting utility
│
└── 📄 README.md                   # Project documentation
```

---

## 🚀 Projects Overview

### 1. Student Management System
A console-based data tracking dashboard designed to execute core database operations while permanently storing information locally.
* **Add Profiles:** Registers new students with completely unique IDs.
* **Update Records:** Edits specific details dynamically without losing old information.
* **Delete Logs:** Safely removes individual student records upon query request.
* **Search System:** Instantly finds individual records using targeted ID lookups.
* **Display Output:** Prints out a clean overview layout tracking all active students.
* **CSV Syncing:** Automatically preserves and keeps data updated inside a local `students.csv` file.

### 2. Automatic File Organizer
A desktop workspace cleanup utility that scans any messy directory path and instantly brings order to it.
* **File Separation:** Scans extensions to isolate `Images`, `PDFs`, `Videos`, `Documents`, `Audio`, and `Archives`.
* **Dynamic Creation:** Evaluates destination rules and builds missing category folders on-the-fly.
* **Execution Summary:** Displays a quick breakdown report showing exactly how many files were relocated.

---

## 💻 How to Run the Scripts

### Prerequisites
Ensure you have **Python 3.x** installed on your system.

### Running the Student Management System
1. Open your terminal and navigate to the project directory.
2. Execute the file using:
   ```bash
   python Student_Management_System/student_management.py
   ```

### Running the File Organizer
1. Execute the file using:
   ```bash
   python Automatic_File_Organizer/file_organizer.py
   ```
2. Paste the absolute path of the messy folder when prompted (e.g., `C:\Users\YourName\Desktop\CleanMe`).

---

## 🔮 Future Enhancements (Roadmap)

I plan to expand these utilities in the future with the following advanced features:

### For the Student Management System:
* **Graphical User Interface (GUI):** Upgrade from a terminal menu to a visual window application using `Tkinter` or `PyQt` featuring functional input forms and data tables.
* **Database Integration:** Transition from local CSV storage to a robust SQLite database for scalable, relational data storage.
* **PDF Report Generator:** Add an export option that generates formal student transcript cards and performance reports directly into PDF documents.

### For the Automatic File Organizer:
* **Background Monitoring:** Implement a real-time background script using the `watchdog` library that continuously monitors and auto-cleans folders (like your Downloads directory) the moment a new file drops in.
* **Duplicate File Sweeper:** Add a feature that checks file hashing signatures (MD5/SHA256) to identify and safely delete duplicate files, recovering lost drive space.
* **Custom User Rules:** Develop a basic text configuration file so users can easily customize their own folder names and file extensions without editing the core Python script.

---

## 📋 Professional Context
* **Platform:** Swiftly Internship Milestone
* **Focus Domain:** Python Programming & Script Automation
