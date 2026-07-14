import json


def load_students():
    file = open("data/students.json", "r")
    students = json.load(file)
    return students
    file.close()


def print_menu():
    print("===============================")
    print("         AI-SCHOOL OS          ")
    print("===============================")
    print()
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


students = load_students()


def add_student():
    name = input("Enter Name: ")
    roll = int(input("Enter Roll No: "))
    for student in students:
        if student["roll"] == roll:
            print("Roll No already exist,")
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
    print("Student Added Successfully")


def view_students():
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


def search_student():
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


def update_student():
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
                print("\nStudent Updated Successfully\n")
                print(f"Name : {student['name']}")
                print(f"Roll : {student['roll']}")
                print(f"Marks: {student['marks']}")

            found = True
            break

    if not found:
        print("Student Not Found")


def delete_student():
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
                print("Student Deleted Successfully")
            elif choice == 2:
                print("Deletion Cancelled")
            found = True
            break

    if found == False:
        print("Student Not Found")


while True:
    print_menu()
    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        print("Please enter a valid choice.")
        continue
    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_student()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
