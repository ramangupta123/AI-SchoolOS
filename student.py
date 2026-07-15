from file_handler import save_students


def add_student(students):
    name = input("Enter Name: ")
    roll = int(input("Enter Roll No: "))
    for student in students:
        if student["roll"] == roll:
            print("Roll No already exist.")
            return

    while True:
        marks = int(input("Enter Marks: "))

        if 0 <= marks <= 100:
            break

        print("Marks Invalid. Please enter marks between 0 and 100")
    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    save_students(students)
    print("Student Added Successfully")


def view_students(students):
    if len(students) == 0:
        print("No Students Found")
    else:
        i = 1
        for student in students:
            print("===========================")
            print(f"Student {i}")
            print()
            print(f"Name : {student['name']}")
            print(f"Roll : {student['roll']}")
            print(f"Marks: {student['marks']}")
            print("===========================")
            i += 1


def search_student(students):
    search_name = input("Enter Student Name: ")
    found = False

    for student in students:
        if student["name"] == search_name:
            print("\nStudent Found\n")
            print(f"Name : {student['name']}")
            print(f"Roll : {student['roll']}")
            print(f"Marks: {student['marks']}")
            found = True
            break

    if not found:
        print("Student Not Found")


def update_student(students):
    roll = int(input("Enter Student Roll No: "))
    found = False

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found\n")
            print(f"1. Name : {student['name']}")
            print(f"2. Roll : {student['roll']}")
            print(f"3. Marks: {student['marks']}")
            print()

            choice = int(input("Enter Choice: "))

            updated = False

            if choice == 1:
                new_name = input("Enter New Name: ")
                student["name"] = new_name
                updated = True

            elif choice == 2:
                new_roll = int(input("Enter New Roll No: "))
                student["roll"] = new_roll
                updated = True

            elif choice == 3:
                new_marks = int(input("Enter New Marks: "))
                student["marks"] = new_marks
                updated = True

            else:
                print("Invalid Choice")

            if updated:
                save_students(students)
                print("\nStudent Updated Successfully\n")
                print(f"Name : {student['name']}")
                print(f"Roll : {student['roll']}")
                print(f"Marks: {student['marks']}")

            found = True
            break

    if not found:
        print("Student Not Found")


def delete_student(students):
    roll = int(input("Enter Student Roll No:"))
    found = False
    for student in students:
        if student["roll"] == roll:
            print("Student Found")
            print(f"Name : {student['name']}")
            print(f"Roll : {student['roll']}")
            print(f"Marks: {student['marks']}")
            print()

            print("Are you sure want to delete?")
            print("1. Yes")
            print("2. No")
            print()

            choice = int(input("Enter choice:"))
            if choice == 1:
                students.remove(student)
                save_students(students)
                print("Student Deleted Successfully")
            elif choice == 2:
                print("Deletion Cancelled")
            found = True
            break

    if found == False:
        print("Student Not Found")
