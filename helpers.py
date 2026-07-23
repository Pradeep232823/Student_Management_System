from datetime import datetime
from database import get_connection

def non_numeric():
    print()
    print("Entered a non-numeric value. Please enter a valid number.")

def invalid_choice():
    print()
    print("Invalid choice. Please try again.")

def get_choice(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            non_numeric()
            return None

def delete_record():
    while True:
        print()
        choice = input("Do you want to delete records (Y/N): ").strip().lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print()
            print("Please enter Y or N.")

def valid_attendance_status():
    while True:
        status = input("Enter the attendance status (Present/Absent/Leave): ").strip().capitalize()
        if status in ["Present","Absent","Leave"]:
            return status
        print()
        print("Invalid Status..")

def validate_name():
    while True:
        name = input("Enter Name: ").strip()
        isValid = True
        
        for ch in name:
            if not (ch.isalpha() or ch.isspace() or ch == "."):
                isValid = False
                print()
                print("Invalid Name.. Try again..")
                break
        if isValid and name:
            return name

def validate_gender():
    while True:
        gender = input("Enter Gender: ").strip().capitalize()

        if gender.lower() in ["male","female","other"]:
            return gender
        print()
        print("Invalid Gender.. Try again..")

def validate_date(prompt):
    while True:
        date = input(prompt)

        try:
            date = datetime.strptime(date, "%Y-%m-%d").date()
            return date
        except ValueError:
            print()
            print("Invalid date.")
def is_email_exists(email):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "SELECT 1 FROM STUDENTS WHERE email=%s"
        cursor.execute(query,(email,))
        if cursor.fetchone():
            return True
        return False
    finally:
        cursor.close()
        conn.close()
def validate_email():
    while True:
        email = input("Enter Email: ").strip()

        # Must contain exactly one '@'
        if email.count('@') != 1:
            print()
            print("Invalid email.")
            continue

        email_parts = email.split('@')

        # Only gmail.com allowed
        if email_parts[1] != "gmail.com":
            print()
            print("Email domain must be gmail.com.")
            continue

        username = email_parts[0]

        if not username:
            print()
            print("Invalid email.")
            continue

        # First character
        first = username[0]

        if not (first.isalpha() or first.isdigit() or first in "!#$%&'*+/=?^_`{|}~-"):
            print()
            print("Invalid email.")
            continue

        # Remaining characters
        valid = True

        for ch in username[1:]:
            if ch in " @()<>[],;:\"\\":   # disallowed
                valid = False
                break

        if not valid:
            print()
            print("Invalid email.")
            continue

        exist = is_email_exists(email)
        if exist:
            print()
            print("Email already exist..Try another..")
            continue
        
        return email
        
def validate_phone():
    while True:
        phone = input("Enter Phone Number: ").strip()
        
        if phone.isdigit() and len(phone)==10:
            return phone
        print()
        print("Phone number must be numeric and contain exactly 10 digits..")

def validate_address():
    while True:
        address = input("Enter Address: ").strip()

        if address:
            return address
        print()
        print("Address cannot be empty.")

def validate_course():
    while True:
        course = input("Enter Course: ").strip().upper()
        courses = ["CSE","ECE","EEE","CIVIL","MECH","AIML","AIDS"]
        if course in courses:
            return course
        print()
        print("Invalid Course..")

def validate_year_semester():
    while True:
        year_semester = input("Enter the studying year and semester in the format (year-semester): ")
        valid = ["1-1","1-2","2-1","2-2","3-1","3-2","4-1","4-2"]
        if year_semester in valid:
            return year_semester
        print()
        print("Invalid Year and Semester Choose from given below: ")
        for year_sem in valid:
            print(year_sem)
        print()

def students_table_header():
    print("-" * 130)
    print(f"{'ID':<3} {'Name':<15} {'Gender':<6} {'DOB':<12} {'Email':<20} {'PHONE':<12} {'ADDRESS':<30} {'COURSE':<10} {'YEAR-SEM':<6} ")
    print("-" * 130)

def students_row_data(row):
    print(f"{row[0]:<3} {row[1]:<15} {row[2]:<6} {str(row[3]):<12} {row[4]:<20} {row[5]:<12} {str(row[6]):<30} {row[7]:<10} {row[8]:<6} ")

def attendance_table_header():
    print("-" * 60)
    print(f"{'Attendance_ID':<15} {'Student_id':<15} {'Attend_date':<15} {'Status':<10} ")
    print("-" * 60)

def attendance_row_data(row):
    print(f"{row[0]:<15} {row[1]:<15} {str(row[2]):<15} {str(row[3]):<10} ")

validators = {
    "student_name": validate_name,
    "gender": validate_gender,
    "dob": lambda: validate_date("Enter DOB (YYYY-MM-DD): "),
    "email": validate_email,
    "phone": validate_phone,
    "address": validate_address,
    "course": validate_course,
    "year_semester": validate_year_semester
}

def validate_marks():
    while True:
        print()
        marks = get_choice("Enter Marks: ")
        if marks is None:
            continue
        if 0 <= marks <= 100:
            return marks
        print()
        print("Marks should be between 0 and 100.")

def validate_subject(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        while True:
            print()
            subject = input("Enter subject name: ").strip().title()
            if not subject:
                print()
                print("Subject should not be empty")
                continue
            query = "SELECT 1 FROM marks WHERE student_id = %s AND subject_name = %s"
            cursor.execute(query,(student_id,subject))
            if cursor.fetchone():
                print()
                print("This subject marks already entered to this student..")
                continue
            return subject
    finally:
        cursor.close()
        conn.close()

def is_student_exist_in_marks(prompt):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        while True:
            print()
            student_id = get_choice(prompt)
            if student_id is None:
                continue
            query = "SELECT 1 FROM marks WHERE student_id = %s LIMIT 1"
            cursor.execute(query, (student_id,))

            if cursor.fetchone() is None:
                print()
                print("The Student records not exist.. Try again..")
                continue

            return student_id

    finally:
        cursor.close()
        conn.close()

def student_marks_records(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT student_name FROM students WHERE student_id = %s",(student_id,))
        student_name = cursor.fetchone()[0]
        query = "SELECT subject_name, marks FROM marks WHERE student_id = %s"
        cursor.execute(query,(student_id,))
        rows = cursor.fetchall()
        if not rows:
            print()
            print("No marks records found for this student..")
            return
        print()
        print(f"Student ID: {student_id}")
        print(f"Student Name: {student_name}")
        print("-" * 30)
        print(f"{'Subject Name':<15} {'Marks':<15} ")
        print("-" * 30)
        for row in rows:
            print(f"{row[0]:<15} {row[1]:<15} ")
        print("-" * 30)
        return

    finally:
        cursor.close()
        conn.close()

def is_subject_exist_in_marks(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        while True:
            print()
            subject = input("Enter subject name: ").strip().title()
            if not subject:
                print()
                print("Subject should not be empty")
                continue
            query = "SELECT 1 FROM marks WHERE student_id = %s AND subject_name = %s"
            cursor.execute(query,(student_id,subject))
            if not cursor.fetchone():
                print()
                print("The subject is not exist in records for this student id.. Try again..")
                continue
            return subject
    finally:
        cursor.close()
        conn.close()

def is_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "SELECT 1 FROM students WHERE student_id = %s "
        cursor.execute(query,(student_id,))
        if cursor.fetchone():
            return True
        print()
        print("The student does not exist..")
        return False
    finally:
        cursor.close()
        conn.close()

def validate_fee(prompt):
    while True:
        amount = get_choice(prompt)
        if amount is None:
            continue
        if amount <= 0:
            print()
            print("Amount must be greater than 0")
            continue
        return amount

def is_student_fee_exist(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "SELECT 1 FROM fees WHERE student_id = %s"
        cursor.execute(query,(student_id,))
        if cursor.fetchone():
            return True
        return False
    finally:
        cursor.close()
        conn.close()

def student_fee_header():
    print()
    print("Student Fee Records..")
    print("-" * 100)
    print(f"{'Student ID':<12} {'Student Name':<20} {'Total Fee':<15} {'Paid Fee':<15} {'Due Fee':<15} {'Last Payment Date':<20}")
    print("-" * 100)

def student_fee_rows(row):
    print(f"{row[0]:<12} {row[1]:<20} {row[2]:<15} {row[3]:<15} {row[4]:<15} {str(row[5]):<20}")

def student_fee_details(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT s.student_name, total_fee, paid_fee, due_fee, payment_date FROM fees f JOIN students s on f.student_id = s.student_id WHERE f.student_id = %s",(student_id,))
        row = cursor.fetchone()
        
        print(f"{student_id:<12} {row[0]:<20} {row[1]:<15} {row[2]:<15} {row[3]:<15} {str(row[4]):<20}")
        return

    finally:
        cursor.close()
        conn.close()