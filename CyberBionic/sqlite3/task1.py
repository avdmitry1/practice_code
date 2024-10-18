import sqlite3

connection = sqlite3.connect("db.sqlite3")

cursor = connection.cursor()

# Create table


def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        purpose TEXT NOT NULL,
        sum INTEGER NOT NULL,
        time TEXT NOT NULL
    );
    """

    cursor.execute(query)
    connection.commit()
    print("Table created successfully.")


def add_column():
    choose = input("What column do you want to add? ")
    query = f"""ALTER TABLE employees ADD COLUMN {choose} INTEGER"""
    cursor.execute(query)
    connection.commit()
    print("Column added successfully.")


def delete_column():
    choose = input("What column do you want to delete ?")
    query = f"""ALTER TABLE employees DROP COLUMN {choose}"""
    cursor.execute(query)
    connection.commit()
    print("Column deleted successfully.")


def get_database():
    query = "PRAGMA table_info(employees)"
    cursor.execute(query)
    rows = cursor.fetchall()
    print("\nColumn Name\tType\tPrimary Key\tNot Null\tDefault Value")
    for row in rows:
        print(f"{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}\t{row[5]}")


def rename_column():
    choice = input("What column do you want to rename? ")
    new_name = input("What is the new name?: ")
    query = f"""
    ALTER TABLE employees RENAME COLUMN {choice} TO {new_name};
    """
    cursor.execute(query)
    connection.commit()
    print("Column renamed successfully.")


def update():
    choice = input("What column do you want to update? ")
    query = f"""
    UPDATE employees
    SET {choice} = ?
    WHERE id = ?
    """
    new_name = input("What new name: ")
    id_ = input("What id? ")
    cursor.execute(query, (new_name, id_))
    connection.commit()
    print(f"{choice} updated successfully.")


def menu():
    while True:
        print("\nChoose an option:")
        print("1. Add column")
        print("2. Delete column")
        print("3. Get all employees")
        print("4. Update employee")
        print("5. Rename employee")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_column()
        elif choice == "2":
            delete_column()
        elif choice == "3":
            get_database()
        elif choice == "4":
            choice = input("What column you want to update: ")
            choice2 = input("What id? ")
            update(choice, choice2)
        elif choice == "5":
            rename_column()
        elif choice == "6":
            print("Exit")


if __name__ == "__main__":
    menu()
