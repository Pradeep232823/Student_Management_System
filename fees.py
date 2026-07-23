import helpers
from database import get_connection
def add_fee():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        while True:
            print()
            student_id = helpers.get_choice("Enter student id to add fees: ")
            if student_id is None:
                continue
            if not helpers.is_student(student_id):
                continue
            if helpers.is_student_fee_exist(student_id):
                print()
                print("Student fee already exist.. Try update operation..")
                continue

            total_fee = helpers.validate_fee("Enter the Total Fee in rupees: ")

            while True:
                paid_fee = helpers.validate_fee("Enter the Fee Paid in rupees: ")

                if paid_fee > total_fee:
                    print()
                    print("Paid Fee cannot exceed total fee..")
                    continue
                break

            due_fee = total_fee - paid_fee

            payment_date = helpers.validate_date("Enter the payment date: ")

            query = "INSERT INTO fees (student_id, total_fee, paid_fee, due_fee, payment_date) values (%s,%s,%s,%s,%s)"
            values = (student_id, total_fee, paid_fee, due_fee, payment_date)
            cursor.execute(query, values)
            conn.commit()
            print()
            print("Fee records inserted successfully..")
            break
    finally:
        cursor.close()
        conn.close()

def view_fee():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        while True:
            print("""
==================
View Fee Options
==================

1. View All Students Fee
2. View Specific Student Fee
3. Back
""")
            choice = helpers.get_choice("Enter the number according to your choice: ")
            if choice is None:
                continue

            match choice:
                case 1:
                    query = "SELECT f.student_id, s.student_name, total_fee, paid_fee, due_fee, payment_date FROM fees f JOIN students s on f.student_id = s.student_id order by f.student_id"
                    cursor.execute(query)
                    rows = cursor.fetchall()
                    if not rows:
                        print()
                        print("No fee records found.")
                        continue
                    helpers.student_fee_header()
                    for row in rows:
                        helpers.student_fee_rows(row)
                    print("-" * 100)
                case 2:
                    print()
                    student_id = helpers.get_choice("Enter student id to view fee details: ")
                    if student_id is None:
                        continue
                    if not helpers.is_student(student_id):
                        continue
                    if not helpers.is_student_fee_exist(student_id):
                        print()
                        print("Student fee does not exist..")
                        continue

                    helpers.student_fee_header()
                    helpers.student_fee_details(student_id)
                    print("-" * 100)

                case 3:
                    break
                case _:
                    helpers.invalid_choice()
    finally:
        cursor.close()
        conn.close()

def update_fee():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        while True:
            print()
            student_id = helpers.get_choice("Enter student id to update fees: ")
            if student_id is None:
                continue
            if not helpers.is_student(student_id):
                continue
            if not helpers.is_student_fee_exist(student_id):
                print()
                print("Student fee does not exist..")
                continue
            
            helpers.student_fee_header()
            helpers.student_fee_details(student_id)
            print("-" * 100)
            
            cursor.execute("SELECT paid_fee, due_fee FROM fees WHERE student_id = %s",(student_id,))
            row = cursor.fetchone()
            current_paid_fee, current_due_fee = row

            if current_due_fee == 0:
                print()
                print("The student's fee has already been fully paid.")
                break
            
            while True:
                print()
                new_paid_fee = helpers.validate_fee("Enter the Fee Paid in Rupees: ")

                if new_paid_fee > current_due_fee:
                    print()
                    print("Payment amount cannot exceed the due fee.")
                    continue
                break
            
            updated_paid_fee = current_paid_fee + new_paid_fee
            updated_due_fee = current_due_fee - new_paid_fee

            payment_date = helpers.validate_date("Enter the Payment Date: ")

            query = "UPDATE fees SET paid_fee = %s, due_fee = %s, payment_date = %s WHERE student_id = %s"
            values = (updated_paid_fee, updated_due_fee, payment_date, student_id)
            cursor.execute(query, values)
            conn.commit()

            print()
            print("Student Fee details updated successfully..")
            helpers.student_fee_header()
            helpers.student_fee_details(student_id)
            print("-" * 100)
            break

    finally:
        cursor.close()
        conn.close()

def students_with_due():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "SELECT f.student_id, s.student_name, total_fee, paid_fee, due_fee, payment_date FROM fees f JOIN students s on f.student_id = s.student_id WHERE due_fee > 0 ORDER BY f.student_id"
        cursor.execute(query)
        rows = cursor.fetchall()
        if not rows:
            print()
            print("No students have due fees.")
            return
        helpers.student_fee_header()
        for row in rows:
            helpers.student_fee_rows(row)
        print("-" * 100)

    finally:
        cursor.close()
        conn.close()

def main():
    while True:
        print("""
=================
Fee Management
=================
1. Add Fee Payment
2. View Fee Details
3. Update Fee
4. Students with Due Fees
5. Back
""")
        choice = helpers.get_choice("Enter the number according to your choice: ")
        if choice is None:
            continue

        match choice:
            case 1:
                add_fee()
            case 2:
                view_fee()
            case 3:
                update_fee()
            case 4:
                students_with_due()
            case 5:
                break
            case _:
                helpers.invalid_choice()