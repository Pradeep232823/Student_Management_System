import student
import attendance
import marks
import fees
import reports
from auth import authorize
from helpers import get_choice, invalid_choice

def login():
    logged_in = authorize()

    if logged_in:
        print()
        print("Login Successful..")
        return True
    print()
    print("Invalid Credentials.. Try again..")
    return False
    
def logout():
    while True:
        print()
        choice = input("Do you want to logout (Y/N): ").strip().lower()

        if choice == "y":
            print()
            print("Logout Successful")
            return True
        elif choice == "n":
            return False
        else:
            print()
            print("Please enter Y or N.")

def dashboard():
    while True:
        print("""
===================================
STUDENT MANAGEMENT SYSTEM
===================================

1. Student Management
2. Attendance Management
3. Marks Management
4. Fee Management
5. Reports
6. Logout
""")
        choice = get_choice("Enter the number according to your preferred choice: ")
        if choice is None:
            continue

        match choice:
            case 1:
                student.main()
            case 2:
                attendance.main()
            case 3:
                marks.main()
            case 4:
                fees.main()
            case 5:
                reports.main()
            case 6:
                if logout():
                    break
            case _:
                invalid_choice()

def main():
    while True:
        print("""
1. Enter to Login
2. Exit
""")

        main_choice = get_choice("Enter the number according to your preferred choice: ")
        if main_choice is None:
            continue

        match main_choice:
            case 1:
                if login():
                    dashboard()
            case 2:
                print()
                print("Thank you for using the Student Management System.")
                break
            case _:
                invalid_choice()
if __name__ == "__main__":
    main()