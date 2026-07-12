def print_menu():
    print("===============================")
    print("         AI-SCHOOL OS          ")
    print("===============================")
    print()
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")


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
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
