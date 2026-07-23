from database import get_connection
import helpers
def add_student():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        print()
        print("Enter Student details")
        print()
        student_name = helpers.validate_name()
        gender = helpers.validate_gender()
        dob = helpers.validate_date("Enter DOB (YYYY-MM-DD): ")
        email = helpers.validate_email()
        phone = helpers.validate_phone()
        address = helpers.validate_address()
        course = helpers.validate_course()
        year_semester = helpers.validate_year_semester()

        query = """
        INSERT INTO STUDENTS(student_name,gender,dob,email,phone,address,course,year_semester) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"""

        values = (student_name,gender,dob,email,phone,address,course,year_semester)
        
        cursor.execute(query, values)
        conn.commit()
        print()
        print("Student added successfully")
    finally:
        cursor.close()
        conn.close()

def view_students():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "SELECT * FROM STUDENTS"
        cursor.execute(query)
        rows = cursor.fetchall()
        if not rows:
            print()
            print("No records found")
            return
        print()
        print(f"Total Students: {len(rows)}")
        
        helpers.students_table_header()

        for row in rows:
            helpers.students_row_data(row)

        print("-" * 130)
    finally:
        cursor.close()
        conn.close()

def search_student():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        while True:
            print()
            student_id = helpers.get_choice("Enter Student ID to search: ")
            if student_id is None:
                continue

            query = "SELECT * FROM STUDENTS WHERE STUDENT_ID = %s "
            
            cursor.execute(query,(student_id,))

            row = cursor.fetchone()
            if not row:
                print()
                print("Student Id is not exist..")
                continue
            print()
            print(f"Student Details Found")
            
            helpers.students_table_header()

            helpers.students_row_data(row)

            print("-" * 130)
            break

    finally:
        cursor.close()
        conn.close()

def update_student():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        while True:
            print()
            student_id = helpers.get_choice("Enter the Student ID Need to update: ")
            if student_id is None:
                continue
            query = "SELECT * FROM STUDENTS WHERE STUDENT_ID = %s"
            cursor.execute(query,(student_id,))

            row = cursor.fetchone()
            if not row:
                print()
                print("Student Id is not exist..")
                continue
            print()
            print(f"Student Details Found")
            
            helpers.students_table_header()
            
            helpers.students_row_data(row)
            print("-" * 130)

            print("""
==================
Student Fields
==================

0. Name
1. Gender
2. DOB
3. Email
4. Phone
5. Address
6. Course
7. Year-Semester
""")
            all_choices = ["Student_name","Gender","DOB","Email","Phone","Address","Course","Year_semester"]
            count = 0
            while True:
                count = helpers.get_choice("How many fields you want to update: ")
                if count is None:
                    continue
                if 1 <= count <= 8:
                    break
                print()
                print("Please enter a value between 1 and 8.")
            choices_num = []
            for _ in range(count):
                while True:
                    choice = helpers.get_choice("Enter field number: ")
                    if choice is None:
                        continue

                    if 0 <= choice <= 7 and choice not in choices_num:
                        choices_num.append(choice)
                        break
                    print()
                    print("Invalid or duplicate choice.")
            
            columns = tuple(all_choices[i] for i in choices_num)

            new_values = []

            

            for column in columns:
                new_values.append(helpers.validators[column.lower()]())
            
            set_clause = ", ".join(f"{column} = %s" for column in columns)
            
            query = "UPDATE STUDENTS SET " + set_clause + " WHERE student_id = %s"

            values = tuple(new_values) + (student_id,)

            cursor.execute(query, values)
            conn.commit()
            print()
            print("Student records updated successfully")
            cursor.execute("SELECT * FROM STUDENTS WHERE STUDENT_ID = %s", (student_id,))
            updated_row = cursor.fetchone()
            
            helpers.students_table_header()

            helpers.students_row_data(updated_row)

            print("-" * 130)
            break

    finally:
        cursor.close()
        conn.close()

def delete_student():
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        while True:
            print()
            student_id = helpers.get_choice("Enter Student ID to delete: ")
            if student_id is None:
                continue
            query = "SELECT * FROM STUDENTS WHERE STUDENT_ID = %s"
            cursor.execute(query,(student_id,))

            row = cursor.fetchone()
            if not row:
                print()
                print("Student Id is not exist..")
                continue
            
            choice = helpers.delete_record()
            if not choice:
                print()
                print("Deletion cancelled..")
                continue

            query = "DELETE FROM STUDENTS WHERE Student_id = %s"

            cursor.execute(query,(student_id,))
            print()
            print("Student records deleted successfully")
            conn.commit()
            break
    finally:
        cursor.close()
        conn.close()


def main():
    while True:
        print("""
================================
Student Management Operations
================================

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Back
""")
        choice = helpers.get_choice("Enter the number according to your preferred choice: ")
        if choice is None:
            continue
        match choice:
            case 1:
                add_student()
            case 2:
                view_students()
            case 3:
                search_student()
            case 4:
                update_student()
            case 5:
                delete_student()
            case 6:
                break
            case _:
                helpers.invalid_choice()