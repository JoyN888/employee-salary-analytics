import mysql.connector

# Database connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="EMPP"
)

cursor = con.cursor()

print("Connected Successfully")

# Check employee function
def check_employee(employee_id):
    sql = "SELECT * FROM employees WHERE id=%s"
    cursor.execute(sql, (employee_id,))
    return cursor.fetchone() is not None

# Add employee function
def add_employee():
    Id = input("Enter Employee Id: ")

    if check_employee(Id):
        print("Employee already exists")
        return

    name = input("Enter Name: ")
    position = input("Enter Position: ")
    salary = input("Enter Salary: ")

    sql = "INSERT INTO employees VALUES (%s,%s,%s,%s)"
    cursor.execute(sql, (Id, name, position, salary))
    con.commit()

    print("Employee Added")

# Display employees
def display_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()

    print("\nEmployee Records:")
    print("----------------------------")

    for row in rows:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Position:", row[2])
        print("Salary:", row[3])
        print("----------------------------")

# Remove employee
def remove_employee():
    Id = input("Enter Employee Id to remove: ")

    if not check_employee(Id):
        print("Employee does not exist")
        return

    sql = "DELETE FROM employees WHERE id=%s"
    cursor.execute(sql, (Id,))
    con.commit()

    print("Employee Removed Successfully")

# Promote employee
def promote_employee():
    Id = input("Enter Employee Id to promote: ")

    if not check_employee(Id):
        print("Employee does not exist")
        return

    try:
        amount = float(input("Enter salary increment amount: "))

        sql = "SELECT salary FROM employees WHERE id=%s"
        cursor.execute(sql, (Id,))
        current_salary = cursor.fetchone()[0]

        new_salary = current_salary + amount

        update_sql = "UPDATE employees SET salary=%s WHERE id=%s"
        cursor.execute(update_sql, (new_salary, Id))

        con.commit()
        print("Employee Promoted Successfully")

    except:
        print("Invalid input")

# Menu Function
def menu():
    while True:
        print("\n===== Employee Management System =====")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Remove Employee")
        print("4. Promote Employee")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            remove_employee()
        elif choice == '4':
            promote_employee()
        elif choice == '5':
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice")

menu()
