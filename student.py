from student_model import Student
from database import cursor, connection


def add_student():

    print("\n===== Add Student =====")

    while True:
        try:
            roll = int(input("Enter Roll Number: "))

            if roll <= 0:
                print("❌ Roll Number must be positive.")
                continue

            break

        except ValueError:
            print("❌ Please enter numbers only.")

    while True:
        name = input("Enter Student Name: ").strip()

        if name == "":
            print("❌ Name cannot be empty.")
        else:
            break

    while True:
        try:
            marks = int(input("Enter Marks: "))

            if 0 <= marks <= 100:
                break

            print("❌ Marks must be between 0 and 100.")

        except ValueError:
            print("❌ Please enter a valid number.")

    # -------------------------------
    # Check if roll number already exists
    # -------------------------------
    check_query = """
    SELECT * FROM students
    WHERE roll = %s
    """

    cursor.execute(check_query, (roll,))

    student = cursor.fetchone()

    if student is not None:
        print(f"\n❌ Roll Number {roll} already exists.")
        return

    # -------------------------------
    # Insert Student
    # -------------------------------
    insert_query = """
    INSERT INTO students (roll, name, marks)
    VALUES (%s, %s, %s)
    """

    try:

        cursor.execute(insert_query, (roll, name, marks))

        connection.commit()

        print("\n✅ Student Added Successfully!")

    except Exception as e:

        connection.rollback()

        print("\n❌ Error:", e)


def view_students():

    query = """
    SELECT * FROM students
    """

    cursor.execute(query)

    students = cursor.fetchall()

    if len(students) == 0:
        print("\nNo students found.")
        return

    print("\n===== Student List =====")

    for student in students:
        print(f"Roll Number : {student[0]}")
        print(f"Name        : {student[1]}")
        print(f"Marks       : {student[2]}")
        print("---------------------------")


def search_student():

    roll = int(input("Enter Roll Number: "))

    query = """
    SELECT * FROM students
    WHERE roll = %s
    """

    cursor.execute(query, (roll,))

    student = cursor.fetchone()

    if student is None:
        print("\n❌ Student Not Found.")
        return

    print("\n===== Student Details =====")
    print(f"Roll Number : {student[0]}")
    print(f"Name        : {student[1]}")
    print(f"Marks       : {student[2]}")


def update_student():

    roll = int(input("Enter Roll Number: "))

    # Check whether student exists
    check_query = """
    SELECT * FROM students
    WHERE roll = %s
    """

    cursor.execute(check_query, (roll,))

    student = cursor.fetchone()

    if student is None:
        print("\n❌ Student Not Found.")
        return

    print("\n===== Student Found =====")
    print(f"1. Name  : {student[1]}")
    print(f"2. Roll  : {student[0]}")
    print(f"3. Marks : {student[2]}")

    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Roll Number")
    print("3. Marks")

    choice = int(input("Enter Choice: "))

    if choice == 1:

        new_name = input("Enter New Name: ")

        query = """
        UPDATE students
        SET name = %s
        WHERE roll = %s
        """

        cursor.execute(query, (new_name, roll))

    elif choice == 2:

        new_roll = int(input("Enter New Roll Number: "))

        query = """
        UPDATE students
        SET roll = %s
        WHERE roll = %s
        """

        cursor.execute(query, (new_roll, roll))

    elif choice == 3:

        new_marks = int(input("Enter New Marks: "))

        if not (0 <= new_marks <= 100):
            print("❌ Marks should be between 0 and 100.")
            return

        query = """
        UPDATE students
        SET marks = %s
        WHERE roll = %s
        """

        cursor.execute(query, (new_marks, roll))

    else:
        print("❌ Invalid Choice.")
        return

    connection.commit()

    print("\n✅ Student Updated Successfully!")


def delete_student():

    roll = int(input("Enter Roll Number: "))

    # Check whether the student exists
    check_query = """
    SELECT * FROM students
    WHERE roll = %s
    """

    cursor.execute(check_query, (roll,))

    student = cursor.fetchone()

    if student is None:
        print("\n❌ Student Not Found.")
        return

    print("\n===== Student Found =====")
    print(f"Roll Number : {student[0]}")
    print(f"Name        : {student[1]}")
    print(f"Marks       : {student[2]}")

    confirm = input(
        "\nAre you sure you want to delete this student? (y/n): ").lower()

    if confirm != "y":
        print("\nDeletion Cancelled.")
        return

    delete_query = """
    DELETE FROM students
    WHERE roll = %s
    """

    cursor.execute(delete_query, (roll,))

    connection.commit()

    print("\n✅ Student Deleted Successfully!")
