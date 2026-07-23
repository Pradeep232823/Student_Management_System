from database import get_connection

def authorize():
    print()
    print("**** Admin Login ****")
    username = input("Enter the Username: ")
    password = input("Enter the Password: ")
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM admin WHERE admin_id = %s AND password = %s"
    values = (username, password)

    cursor.execute(query, values)
    admin = cursor.fetchone()

    cursor.close()
    conn.close()
    return True if admin else False