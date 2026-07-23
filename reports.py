from database import get_connection
import helpers
from student import view_students
from attendance import attendance_summary

def student_report():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        while True:
            print("""
====================
Student Report
====================

1. Total Students
2. Students Grouped by Course
3. Students Grouped by Year-Semester
4. Back
""")
            choice = helpers.get_choice("Enter the number according to your choice: ")
            if choice is None:
                continue

            match choice:
                case 1:
                    view_students()
                case 2:
                    query = "SELECT course, COUNT(*) FROM students GROUP BY course"
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    if not rows:
                        print("No records found...")
                        continue
                    print()
                    print("Students count by Course..")
                    print("-" * 30)
                    print(f"{'Course':<10} {'Students Count':<15} ")
                    print("-" * 30)
                    for row in rows:
                        print(f"{row[0]:<10} {row[1]:<15}")
                    print("-" * 30)
                case 3:
                    query = "SELECT year_semester, COUNT(*) FROM students GROUP BY year_semester ORDER BY year_semester"
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    if not rows:
                        print("No records found...")
                        continue
                    print()
                    print("Students count by Year-Semester..")
                    print("-" * 30)
                    print(f"{'Year-Semester':<15} {'Students Count':<15} ")
                    print("-" * 30)
                    for row in rows:
                        print(f"{row[0]:<15} {row[1]:<15}")
                    print("-" * 30)
                case 4:
                    break
                case _:
                    helpers.invalid_choice()
    finally:
        cursor.close()
        conn.close()

def attendance_report():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        while True:
            print("""
====================
Attendance Report
====================

1. Student Attendance Summary
2. Overall Statistics
3. Back
""")
            choice = helpers.get_choice("Enter the number according to your choice: ")
            if choice is None:
                continue

            match choice:
                case 1:
                    attendance_summary()
                    
                case 2:
                    query = "SELECT SUM(status='Present'), SUM(status='Absent'), SUM(status='Leave'), COUNT(*) FROM attendance"
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    if not rows:
                        print("Attendance records not found..")
                        continue
                    print()
                    print("Overall Attendance Statistics..")
                    print("-" * 35)
                    print(f"{'Present':<10} {'Absent':<9} {'Leave':<7} {'Total':<7} ")
                    print("-" * 35)
                    for row in rows:
                        print(f"{row[0]:<10} {row[1]:<9} {row[2]:<7} {row[3]:<7} ")
                    print("-" * 35)
                case 3:
                    break
                case _:
                    helpers.invalid_choice()
    finally:
        cursor.close()
        conn.close()

def marks_report():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        while True:
            print("""
====================
Marks Report
====================

1. Student Results
2. Highest Average
3. Lowest Average
4. Overall Average
5. Back
""")
            choice = helpers.get_choice("Enter the number according to your choice: ")
            if choice is None:
                continue

            match choice:
                case 1:
                    query = """
                    SELECT m.student_id, s.student_name, ROUND(AVG(m.marks),2) FROM marks m JOIN students s ON m.student_id = s.student_id 
                    GROUP BY m.student_id, s.student_name ORDER BY m.student_id"""
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    if not rows:
                        print("No records found..")
                        continue
                    print()
                    print("Students Average Results..")
                    print("-" * 45)
                    print(f"{'Student ID':<12} {'Student Name':<15} {'Average Marks':<15} ")
                    print("-" * 45)
                    for row in rows:
                        print(f"{row[0]:<12} {row[1]:<15} {row[2]:<15} ")
                    print("-" * 45)
                case 2:
                    query = """
SELECT m.student_id, s.student_name, ROUND(AVG(m.marks),2) AS Avg_Marks 
FROM marks m JOIN students s ON m.student_id = s.student_id GROUP BY m.student_id, s.student_name 
HAVING AVG(m.marks) = (SELECT AVG(marks) FROM marks GROUP BY student_id ORDER BY AVG(marks) desc LIMIT 1);
"""
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    if not rows:
                        print("No records found..")
                        continue
                    print()
                    print("Highest Average Records..")
                    print("-" * 45)
                    print(f"{'Student ID':<12} {'Student Name':<15} {'Average Marks':<15} ")
                    print("-" * 45)
                    for row in rows:
                        print(f"{row[0]:<12} {row[1]:<15} {row[2]:<15} ")
                    print("-" * 45)
                case 3:
                    query = """
SELECT m.student_id, s.student_name, ROUND(AVG(m.marks),2) AS Avg_Marks 
FROM marks m JOIN students s ON m.student_id = s.student_id GROUP BY m.student_id, s.student_name 
HAVING AVG(m.marks) = (SELECT AVG(marks) FROM marks GROUP BY student_id ORDER BY AVG(marks) asc LIMIT 1);
"""
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    if not rows:
                        print("No records found..")
                        continue
                    print()
                    print("Lowest Average Records..")
                    print("-" * 45)
                    print(f"{'Student ID':<12} {'Student Name':<15} {'Average Marks':<15} ")
                    print("-" * 45)
                    for row in rows:
                        print(f"{row[0]:<12} {row[1]:<15} {row[2]:<15} ")
                    print("-" * 45)
                case 4:
                    query = "SELECT AVG(marks) FROM marks"
                    cursor.execute(query)
                    Average = cursor.fetchone()[0]
                    if Average is None:
                        print("No records found..")
                        continue
                    print()
                    print(f"Overall Average Marks: {round(Average,2)}")
                case 5:
                    break
                case _:
                    helpers.invalid_choice()
    finally:
        cursor.close()
        conn.close()

def fee_report():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        while True:
            print("""
====================
Fee Report
====================

1. Total Fees Collected
2. Outstanding Fees
3. Pending Students
4. Back
""")
            choice = helpers.get_choice("Enter the number according to your choice: ")
            if choice is None:
                continue

            match choice:
                case 1:
                    query = "SELECT SUM(paid_fee) FROM fees"
                    cursor.execute(query)
                    total_fee = cursor.fetchone()[0]
                    if total_fee is None:
                        print("Records not found..")
                        continue
                    print()
                    print(f"Total Fee Collected: {total_fee}")
                case 2:
                    query = "SELECT SUM(due_fee) FROM fees"
                    cursor.execute(query)
                    total_fee = cursor.fetchone()[0]
                    if total_fee is None:
                        print("Records not found..")
                        continue
                    print()
                    print(f"Total Outstanding(Due) Fee: {total_fee}")
                case 3:
                    query = "SELECT f.student_id, s.student_name, f.due_fee FROM fees f JOIN students s on f.student_id = s.student_id where f.due_fee > 0"
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    if not rows:
                        print("No records found..")
                        continue
                    print()
                    print("Fee Pending Students Records..")
                    print("-" * 40)
                    print(f"{'Student ID':<12} {'Student Name':<15} {'Due Fee':<10} ")
                    print("-" * 40)
                    for row in rows:
                        print(f"{row[0]:<12} {row[1]:<15} {row[2]:<10} ")
                    print("-" * 40)
                case 4:
                    break
                case _:
                    helpers.invalid_choice()
    finally:
        cursor.close()
        conn.close()

def main():
    while True:
        print("""
=====================
Reports Management
=====================

1. Student Report
2. Attendance Report
3. Marks Report
4. Fee Report
5. Back
""")
        choice = helpers.get_choice("Enter the number according to your choice: ")
        if choice is None:
            continue

        match choice:
            case 1:
                student_report()
            case 2:
                attendance_report()
            case 3:
                marks_report()
            case 4:
                fee_report()
            case 5:
                break
            case _:
                helpers.invalid_choice()