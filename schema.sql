create database student_db;
use student_db;
-- Students Table
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    gender VARCHAR(10),
    dob DATE,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(10),
    address VARCHAR(255),
    course VARCHAR(100),
    year_semester VARCHAR(50)
);

-- Attendance Table
CREATE TABLE attendance (
    attendance_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    attend_date DATE NOT NULL,
    status ENUM('Present', 'Absent', 'Leave') NOT NULL,

    FOREIGN KEY (student_id)
        REFERENCES students(student_id)
        ON DELETE CASCADE
);

-- Marks Table
CREATE TABLE marks (
    mark_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    subject_name VARCHAR(100) NOT NULL,
    marks FLOAT NOT NULL,

    FOREIGN KEY (student_id)
        REFERENCES students(student_id)
        ON DELETE CASCADE
);

-- Fees Table
CREATE TABLE fees (
    fee_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    total_fee INT NOT NULL,
    paid_fee INT NOT NULL,
    due_fee INT NOT NULL,
    payment_date DATE,

    FOREIGN KEY (student_id)
        REFERENCES students(student_id)
        ON DELETE CASCADE
);

-- Admin Table
CREATE TABLE admin (
    admin_id VARCHAR(20) PRIMARY KEY,
    password VARCHAR(255) NOT NULL
);

INSERT INTO admin(admin_id, password)
VALUES ('admin', 'admin123');