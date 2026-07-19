from database import cursor, connection


def add_teacher():

    print("\n===== Add Teacher =====")

    # -----------------------------
    # Teacher ID
    # -----------------------------
    while True:
        try:
            teacher_id = int(input("Enter Teacher ID: "))

            if teacher_id <= 0:
                print("❌ Teacher ID must be positive.")
                continue

            break

        except ValueError:
            print("❌ Please enter numbers only.")

    # -----------------------------
    # Teacher Name
    # -----------------------------
    while True:

        name = input("Enter Teacher Name: ").strip()

        if name == "":
            print("❌ Name cannot be empty.")
        else:
            break

    # -----------------------------
    # Phone Number
    # -----------------------------
    while True:

        phone = input("Enter Phone Number: ").strip()

        if len(phone) != 10 or not phone.isdigit():
            print("❌ Enter a valid 10-digit phone number.")
        else:
            break

    # -----------------------------
    # Email
    # -----------------------------
    while True:

        email = input("Enter Email: ").strip()

        if "@" not in email or "." not in email:
            print("❌ Invalid Email.")
        else:
            break

    # -----------------------------
    # Salary
    # -----------------------------
    while True:
        try:
            salary = float(input("Enter Salary: "))

            if salary < 0:
                print("❌ Salary cannot be negative.")
                continue

            break

        except ValueError:
            print("❌ Enter a valid salary.")

    # -----------------------------
    # Joining Date
    # -----------------------------
    joining_date = input("Enter Joining Date (YYYY-MM-DD): ")

    # -----------------------------
    # Check Teacher ID
    # -----------------------------
    check_query = """
    SELECT * FROM teachers
    WHERE teacher_id = %s
    """

    cursor.execute(check_query, (teacher_id,))

    teacher = cursor.fetchone()

    if teacher is not None:
        print(f"\n❌ Teacher ID {teacher_id} already exists.")
        return

    # -----------------------------
    # Insert Teacher
    # -----------------------------
    insert_query = """
    INSERT INTO teachers
    (teacher_id, name, phone, email, salary, joining_date)
    VALUES
    (%s, %s, %s, %s, %s, %s)
    """

    try:

        cursor.execute(
            insert_query,
            (
                teacher_id,
                name,
                phone,
                email,
                salary,
                joining_date
            )
        )

        connection.commit()

        print("\n✅ Teacher Added Successfully!")

    except Exception as e:

        connection.rollback()

        print("\n❌ Error:", e)


def view_teachers():

    query = "SELECT * FROM teachers"

    cursor.execute(query)

    teachers = cursor.fetchall()

    if len(teachers) == 0:
        print("\nNo Teachers Found.")
        return

    print("\n===== Teacher List =====")

    for teacher in teachers:
        print(f"""
Teacher ID : {teacher[0]}
Name       : {teacher[1]}
Phone      : {teacher[2]}
Email      : {teacher[3]}
Salary     : {teacher[4]}
Joining    : {teacher[5]}
-----------------------------
""")


def search_teacher():

    print("\n===== Search Teacher =====")

    while True:
        try:
            teacher_id = int(input("Enter Teacher ID: "))

            if teacher_id <= 0:
                print("❌ Teacher ID must be positive.")
                continue

            break

        except ValueError:
            print("❌ Please enter numbers only.")

    query = """
    SELECT *
    FROM teachers
    WHERE teacher_id = %s
    """

    cursor.execute(query, (teacher_id,))

    teacher = cursor.fetchone()

    if teacher is None:
        print("\n❌ Teacher Not Found.")
        return

    print("\n===== Teacher Details =====")
    print(f"Teacher ID    : {teacher[0]}")
    print(f"Name          : {teacher[1]}")
    print(f"Phone         : {teacher[2]}")
    print(f"Email         : {teacher[3]}")
    print(f"Salary        : {teacher[4]}")
    print(f"Joining Date  : {teacher[5]}")


def update_teacher():

    print("\n===== Update Teacher =====")

    while True:
        try:
            teacher_id = int(input("Enter Teacher ID: "))

            if teacher_id <= 0:
                print("❌ Teacher ID must be positive.")
                continue

            break

        except ValueError:
            print("❌ Please enter numbers only.")

    select_query = """
    SELECT *
    FROM teachers
    WHERE teacher_id = %s
    """

    cursor.execute(select_query, (teacher_id,))
    teacher = cursor.fetchone()

    if teacher is None:
        print("\n❌ Teacher Not Found.")
        return

    print("\n===== Teacher Details =====")
    print(f"1. Name         : {teacher[1]}")
    print(f"2. Phone        : {teacher[2]}")
    print(f"3. Email        : {teacher[3]}")
    print(f"4. Salary       : {teacher[4]}")
    print(f"5. Joining Date : {teacher[5]}")

    try:
        choice = int(input("\nEnter Field to Update: "))
    except ValueError:
        print("❌ Invalid Choice.")
        return

    if choice == 1:
        new_value = input("Enter New Name: ")
        query = "UPDATE teachers SET name = %s WHERE teacher_id = %s"

    elif choice == 2:
        new_value = input("Enter New Phone: ")
        query = "UPDATE teachers SET phone = %s WHERE teacher_id = %s"

    elif choice == 3:
        new_value = input("Enter New Email: ")
        query = "UPDATE teachers SET email = %s WHERE teacher_id = %s"

    elif choice == 4:
        try:
            new_value = float(input("Enter New Salary: "))
        except ValueError:
            print("❌ Invalid Salary.")
            return

        query = "UPDATE teachers SET salary = %s WHERE teacher_id = %s"

    elif choice == 5:
        new_value = input("Enter New Joining Date (YYYY-MM-DD): ")
        query = "UPDATE teachers SET joining_date = %s WHERE teacher_id = %s"

    else:
        print("❌ Invalid Choice.")
        return

    try:
        cursor.execute(query, (new_value, teacher_id))
        connection.commit()

        print("\n✅ Teacher Updated Successfully!")

    except Exception as e:
        connection.rollback()
        print("\n❌ Error:", e)


def delete_teacher():

    print("\n===== Delete Teacher =====")

    while True:
        try:
            teacher_id = int(input("Enter Teacher ID: "))

            if teacher_id <= 0:
                print("❌ Teacher ID must be positive.")
                continue

            break

        except ValueError:
            print("❌ Please enter numbers only.")

    select_query = """
    SELECT *
    FROM teachers
    WHERE teacher_id = %s
    """

    cursor.execute(select_query, (teacher_id,))
    teacher = cursor.fetchone()

    if teacher is None:
        print("\n❌ Teacher Not Found.")
        return

    print("\n===== Teacher Details =====")
    print(f"Teacher ID    : {teacher[0]}")
    print(f"Name          : {teacher[1]}")
    print(f"Phone         : {teacher[2]}")
    print(f"Email         : {teacher[3]}")
    print(f"Salary        : {teacher[4]}")
    print(f"Joining Date  : {teacher[5]}")

    confirm = input("\nAre you sure you want to delete this teacher? (Y/N): ")

    if confirm.lower() != "y":
        print("\nDeletion Cancelled.")
        return

    delete_query = """
    DELETE FROM teachers
    WHERE teacher_id = %s
    """

    try:
        cursor.execute(delete_query, (teacher_id,))
        connection.commit()

        print("\n✅ Teacher Deleted Successfully!")

    except Exception as e:
        connection.rollback()
        print("\n❌ Error:", e)
