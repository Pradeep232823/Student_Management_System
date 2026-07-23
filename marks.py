from database import get_connection
import helpers

def add_marks():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        while True:
            print()
            student_id = helpers.get_choice("Enter Student ID to enter marks: ")
            if student_id is None:
                continue
            
            if not helpers.is_student(student_id):
                continue

            while True:
                print()
                subjects_count = helpers.get_choice("Enter number of subjects: ")
                if subjects_count is None:
                    continue

                if subjects_count > 0:
                    break
                print()
                print("Please enter a positive number.")
            
            for i in range(subjects_count):
                print()
                print(f"Subject {i+1}")
                subject = helpers.validate_subject(student_id)
                marks = helpers.validate_marks()
                query = "INSERT INTO marks (student_id, subject_name, marks) VALUES(%s,%s,%s)"
                values = (student_id, subject, marks)
                cursor.execute(query,values)
            conn.commit()
            print()
            print("Marks added successfully..")
            break

    finally:
        cursor.close()
        conn.close()

def update_marks():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        student_id = helpers.is_student_exist_in_marks("Enter Student ID to update marks: ")
        helpers.student_marks_records(student_id)
        subject = helpers.is_subject_exist_in_marks(student_id)
        marks = helpers.validate_marks()
        query = "UPDATE marks SET marks = %s WHERE student_id = %s AND subject_name = %s"
        values = (marks, student_id, subject)
        cursor.execute(query, values)
        conn.commit()
        print()
        print(f"Student marks updated for subject: {subject}")
        helpers.student_marks_records(student_id)
    finally:
        cursor.close()
        conn.close()
def view_marks():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        while True:
            print("""
====================
View Marks Options
====================

1. View all students records
2. View specific student records
3. Back
""")
            choice = helpers.get_choice("Enter the number according to your choice: ")
            if choice is None:
                continue
            match choice:
                case 1:
                    query = "select student_id from marks group by student_id"
                    cursor.execute(query)
                    students = cursor.fetchall()
                    print()
                    print("All Students Marks Records")
                    for student in students:
                        helpers.student_marks_records(student[0])
                    
                case 2:
                    student_id = helpers.is_student_exist_in_marks("Enter Student ID to view records: ")
                    helpers.student_marks_records(student_id)
                    
                case 3:
                    break
                case _:
                    helpers.invalid_choice()

    finally:
        cursor.close()
        conn.close()

def delete_marks():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        student_id = helpers.is_student_exist_in_marks("Enter the student ID you want to delete marks: ")
        helpers.student_marks_records(student_id)
        subject = helpers.is_subject_exist_in_marks(student_id)
        choice = helpers.delete_record()
        if not choice:
            print()
            print("Deletion cancelled..")
            return
        
        query = "DELETE FROM MARKS WHERE Student_id = %s AND subject_name = %s"

        cursor.execute(query,(student_id,subject))
        conn.commit()
        print()
        print("Student marks records deleted successfully")
        helpers.student_marks_records(student_id)

    finally:
        cursor.close()
        conn.close()

def calculate_total():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "select m.student_id, s.student_name, sum(marks) AS total FROM marks m join students s on m.student_id = s.student_id group by student_id"
        cursor.execute(query)
        rows = cursor.fetchall()
        print()
        print("Marks Summary of each student")
        print("-" * 45)
        print(f"{'Student ID':<15} {'Student Name':<15} {'Total Marks':<15} ")
        print("-" * 45)
        for row in rows:
            print(f"{row[0]:<15} {row[1]:<15} {row[2]:<15}")
        print("-" * 45)
    finally:
        cursor.close()
        conn.close()

def calculate_average():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "select m.student_id, s.student_name, avg(marks) AS average FROM marks m join students s on m.student_id = s.student_id group by student_id"
        cursor.execute(query)
        rows = cursor.fetchall()
        print()
        print("Marks Average of each student")
        print("-" * 45)
        print(f"{'Student ID':<12} {'Student Name':<15} {'Average Marks':<15} ")
        print("-" * 45)
        for row in rows:
            print(f"{row[0]:<12} {row[1]:<15} {row[2]:<15}")
        print("-" * 45)
    finally:
        cursor.close()
        conn.close()
    
def main():
    while True:
        print("""
====================
Marks Management
====================

1. Add Marks
2. View Marks
3. Update Marks
4. Delete Marks
5. Calculate Total
6. Calculate Average
7. Back
""")
        choice = helpers.get_choice("Enter the number according to your choice: ")
        if choice is None:
            continue
        match choice:
            case 1:
                add_marks()
            case 2:
                view_marks()
            case 3:
                update_marks()
            case 4:
                delete_marks()
            case 5:
                calculate_total()
            case 6:
                calculate_average()
            case 7:
                break
            case _:
                helpers.invalid_choice()