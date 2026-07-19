from database import cursor, connection

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
