# Student Management System

## Technologies Used

- Python
- MySQL

---

## Project Overview

The Student Management System is a Command Line Interface (CLI) based application developed using Python and MySQL. It allows an administrator to manage student records, attendance, marks, fees, and generate reports through a simple console interface.

The application follows a modular architecture, where each module is responsible for a specific functionality such as authentication, student management, attendance, marks, fees, reports, database connectivity, and input validation.

All data is stored securely in a MySQL database, and every operation performed through the CLI is reflected in the database.

---

## Requirements

- Python 3.10 or later
- MySQL Server
- mysql-connector-python

---

## Installation

1. Clone the repository.

```bash
git clone <repository-url>
cd Student_Management_System
```

2. Install the required dependency.

```bash
pip install -r requirements.txt
```

3. Create the database using the `schema.sql` file.

4. Update the MySQL connection details in `database.py` if required.

5. Run the application.

```bash
python main.py
```

---

## Project Structure

```text
Student_Management_System/
│
├── attendance.py      # Attendance management
├── auth.py            # Admin authentication
├── database.py        # Database connection
├── fees.py            # Fee management
├── helpers.py         # Validation and helper functions
├── main.py            # Application entry point
├── marks.py           # Marks management
├── reports.py         # Report generation
├── student.py         # Student CRUD operations
├── schema.sql         # Database schema
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation
```

---

## Default Admin Credentials

| Username | Password |
|----------|----------|
| admin | admin123 |

> **Note:** The default credentials are provided for demonstration purposes. In a production environment, passwords should be changed and stored securely using password hashing.

---

## Database Structure

**Database Name:** `student_db`

### Tables

- admin
- students
- attendance
- marks
- fees

---

## Table Description

### 1. Admin

The **admin** table stores administrator login credentials. These credentials are used to authenticate the administrator before granting access to the system.

---

### 2. Students

The **students** table stores the personal and academic details of each student.

**Fields:**

- Student ID
- Student Name
- Gender
- Date of Birth
- Email
- Phone Number
- Address
- Course
- Year-Semester

#### Validation

The following validations are performed before storing student data:

- Student ID must be unique.
- Email must be unique.
- Valid email format.
- Valid date format.
- Valid phone number.
- Valid course.
- Valid year-semester.
- No empty or invalid input values.

All validations are implemented using reusable helper functions in the `helpers` module.

---

### 3. Attendance

The **attendance** table stores the attendance records of students.

**Fields:**

- Attendance ID
- Student ID
- Attendance Date
- Attendance Status (Present / Absent / Leave)

#### Validation

- Student must exist.
- Valid attendance date.
- Valid attendance status.

---

### 4. Marks

The **marks** table stores subject-wise marks for every student.

**Fields:**

- Mark ID
- Student ID
- Subject Name
- Marks

Each student can have multiple subject records.

#### Validation

- Student must exist.
- Duplicate subjects are not allowed.
- Marks must be within the valid range.
- Subject name validation.

---

### 5. Fees

The **fees** table stores fee payment information.

**Fields:**

- Fee ID
- Student ID
- Total Fee
- Paid Fee
- Due Fee
- Payment Date

#### Fee Calculation

- Due Fee = Total Fee − Paid Fee
- During fee updates, Paid Fee and Due Fee are automatically recalculated.
- Payment Date is updated with the latest payment date.

---

## Features

- Secure Admin Login Authentication
- Student Management (Add, View, Search, Update, Delete)
- Attendance Management
- Marks Management
- Fee Management
- Student Reports
- Attendance Reports
- Marks Reports
- Fee Reports
- Input Validation
- MySQL Database Integration
- Modular Python Architecture
- Menu-Driven CLI Interface

---

## Reports

The system generates the following reports.

### Student Reports

- Total Students
- Students Grouped by Course
- Students Grouped by Year-Semester

### Attendance Reports

- Student Attendance Summary
- Overall Attendance Statistics

### Marks Reports

- Student Average Results
- Highest Average Marks
- Lowest Average Marks
- Overall Average Marks

### Fee Reports

- Total Fees Collected
- Outstanding Fees
- Students with Pending Fees

---

## Validation

The project uses reusable helper functions to validate user input before storing it in the database.

Validation includes:

- Student Name
- Email Address
- Phone Number
- Date
- Course
- Year-Semester
- Attendance Status
- Subject Name
- Marks
- Fee Information

These validations help ensure that only valid and consistent data is stored in the database.

---

## Future Enhancements

Some features that can be added in future versions include:

- Password hashing for admin authentication.
- Student login module.
- Export reports to CSV or PDF.
- Graphical User Interface (GUI).
- Advanced search and filtering.
- Dashboard with charts and analytics.
- Backup and restore database functionality.

---

## Conclusion

This project demonstrates the implementation of a modular Student Management System using Python and MySQL. It showcases database connectivity, CRUD operations, SQL queries, input validation, report generation, and modular programming principles through a console-based application.

It is designed as a beginner-friendly database management project that demonstrates practical usage of Python and MySQL while following a clean modular architecture.


# Major Screenshots representation of entire project

## Admin Login Page

![Admin Login Page](Screenshots/1.png)

## Adding Student into database

![Adding student into database](Screenshots/2.png)

## View Students

![Total Students data](Screenshots/3.png)

## Marking Attendance for a student

![Attendance Marking for a student](Screenshots/9.png)

## Total Attendance Records

![Total Attendance Records](Screenshots/10.png)

## Attendance Summary

![Attendance Summary](Screenshots/12.png)

## Adding marks for individual Students

![Adding Marks](Screenshots/14.png)

![Adding Marks](Screenshots/15.png)

## Viewing Students Marks

![Students marks data](Screenshots/16.png)

![Students marks data](Screenshots/17.png)

## Calculating Total and Average marks

![Total Marks](Screenshots/23.png)

![Average Marks](Screenshots/24.png)

## Adding Fee records for student

![Adding Fee records](Screenshots/25.png)

## Viewing Fee records

![Viewing fee records](Screenshots/26.png)

## Fee Due students list

![Fee due list](Screenshots/29.png)

## Total Students Report

![Total students report](Screenshots/31.png)

## Students count reports by course and year-semester

![Students count by course](Screenshots/32.png)

![Students count by year-semester](Screenshots/33.png)

## Attendance Reports

![Attendance report](Screenshots/34.png)

![Attendance report](Screenshots/35.png)

## Students Marks reports

The following screenshots show average marks, highest average, lowest average, and overall average reports.

![Student Marks report](Screenshots/36.png)
![Student Marks report](Screenshots/37.png)
![Student Marks report](Screenshots/38.png)
![Student Marks report](Screenshots/39.png)

## Students Fee reports

![Students Fee reports](Screenshots/40.png)
![Students Fee reports](Screenshots/41.png)
![Students Fee reports](Screenshots/42.png)

## Admin Logout Page

![Admin Logout Page](Screenshots/43.png)
