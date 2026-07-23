from database import get_connection
import helpers

def mark_attendance():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        while True:
            print()
            student_id = helpers.get_choice("Enter the Student ID to Mark Attendance: ")
            if student_id is None:
                continue
            
            if not helpers.is_student(student_id):
                continue
            date = helpers.validate_date("Enter Attended Date (YYYY-MM-DD): ")
            status = helpers.valid_attendance_status()

            query = "SELECT 1 FROM attendance WHERE student_id = %s AND attend_date = %s"
            cursor.execute(query,(student_id,date))

            if cursor.fetchone():
                print()
                print("Attendance is already marked for this student on this date..")
                continue

            query = "INSERT INTO ATTENDANCE(student_id,attend_date,status) VALUES(%s,%s,%s)"
            values = (student_id,date,status)
            cursor.execute(query,values)
            print()
            print("Attendance marked successfully..")
            conn.commit()
            break
    finally:
        cursor.close()
        conn.close()

def view_attendance():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        while True:
            print("""
=========================
View Attendance Options
=========================

1. View all attendance records
2. View specific student attendance records
3. Back
""")
            choice = helpers.get_choice("Enter the number according to your choice: ")
            if choice is None:
                continue
            match choice:
                case 1:
                    query = "SELECT attendance_id, student_id, attend_date, status FROM ATTENDANCE"
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    if not rows:
                        print()
                        print("Student records not found..")
                        return
                    print()
                    print(f"All attendance records: {len(rows)}")
                    
                    helpers.attendance_table_header()

                    for row in rows:
                        helpers.attendance_row_data(row)

                    print("-" * 60)
                case 2:
                    print()
                    student_id = helpers.get_choice("Enter Student ID to view attendance: ")
                    if student_id is None:
                        continue
                    if not helpers.is_student(student_id):
                        continue
                    query = "SELECT attendance_id, student_id, attend_date, status FROM attendance WHERE student_id = %s"
                    cursor.execute(query,(student_id,))
                    rows = cursor.fetchall()
                    if not rows:
                        print()
                        print("No records found")
                        continue
                    print()
                    print(f"Student attendance records: {len(rows)}")
                    
                    helpers.attendance_table_header()

                    for row in rows:
                        helpers.attendance_row_data(row)

                    print("-" * 60)
                case 3:
                    return
                    
                case _:
                    helpers.invalid_choice()
            
    finally:
        cursor.close()
        conn.close()

def attendance_summary():
    conn = get_connection()
    cursor = conn.cursor()
    try: 
        query = """SELECT a.student_id, s.student_name, SUM(status = 'Present') AS present, 
        SUM(status = 'Absent') AS absent, SUM(status = 'Leave') AS leave_count, COUNT(*) AS total FROM attendance 
        a join students s on a.student_id = s.student_id GROUP BY a.student_id, s.student_name order by a.student_id"""
        cursor.execute(query)
        rows = cursor.fetchall()
        if not rows:
            print()
            print("No records found")
            return
        print()
        print(f"Attendance Summary")
        
        print("-" * 80)
        print(f"{'Student_id':<15} {'Student_name':<20} {'Present':<10} {'Absent':<10} {'Leave':<10} {'Total':<10}")
        print("-" * 80)

        for row in rows:
            print(f"{row[0]:<15} {row[1]:<20} {row[2]:<10} {row[3]:<10} {row[4]:<10} {row[5]:<10}")

        print("-" * 80)
    finally:
        cursor.close()
        conn.close()

def main():
    while True:
        print("""
==================================
Attendance Management Operations
==================================

1. Mark Attendance
2. View Attendance
3. Attendance Summary
4. Back
""")
        choice = helpers.get_choice("Enter the number according to your choice: ")
        if choice is None:
            continue
        match choice:
            case 1:
                mark_attendance()
            case 2:
                view_attendance()
            case 3:
                attendance_summary()
            case 4:
                break
            case _:
                helpers.invalid_choice()