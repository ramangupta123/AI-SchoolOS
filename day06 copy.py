def print_menu():
    print("===============================")
    print("         AI-SCHOOL OS          ")
    print("===============================")
    print()
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Exit")


students = []


def add_student():
    name = input("Enter Name: ")
    roll = int(input("Enter roll no:"))
    marks = int(input("Enter marks:"))
    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    print("Students Added Successfully")


def view_students():
    if len(students) == 0:
        print("No Students Found")
    else:

        i = 1
        for student in students:
            print("===========================")

            print()

            print(f"Student {i}")
            i += 1
            print()
            print(f"Name : {student['name']}")
            print(f"Roll : {student['roll']}")
            print(f"Marks: {student['marks']}")
            print("===========================")


def search_student():
    search_name = input("Enter student name: ")
    found = False
    for student in students:
        if student["name"] == search_name:
            print("Student Found")
            print()
            print(f"Name: {student['name']}")
            print(f"Roll: {student['roll']}")
            print(f"Marks: {student['marks']}")
            found = True
            break
    if found == False:
        print("Student Not Found")


def update_student():
    roll = int(input("Enter Student Roll No: "))
    flag = False
    for student in students:
        if student["roll"] == roll:
            print()
            print(f"1.Name: {student['name']}")
            print(f"2.Roll: {student['roll']}")
            print(f"3.Marks: {student['marks']}")
            print()

            choice = int(input("Enter Choice:"))

            updated = False
            if choice == 1:
                new_name = input("Enter new name:")
                student["name"] = new_name
                updated = True
            elif choice == 2:
                new_roll = int(input("Enter new roll no:"))
                student["roll"] = new_roll
                updated = True
            elif choice == 3:
                new_marks = int(input("Enter new marks:"))
                student["marks"] = new_marks
                updated = True
            else:
                print("Enter valid choice.")
            if updated == True:
                print()
                print(f"1.Name: {student['name']}")
                print(f"2.Roll: {student['roll']}")
                print(f"3.Marks: {student['marks']}")
                print()
                print("Student Updated Successfully.")
            flag = True
            break
    if flag == False:
        print("Student Not Found")


while True:
    print_menu()

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_student()

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
