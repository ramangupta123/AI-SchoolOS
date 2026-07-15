import json
from menu import print_menu
from file_handler import load_students, save_students
from student import add_student, view_students, search_student, update_student, delete_student

students = load_students()

while True:
    print_menu()
    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        print("Please enter a valid choice.")
        continue
    if choice == 1:
        add_student(students)

    elif choice == 2:
        view_students(students)

    elif choice == 3:
        search_student(students)

    elif choice == 4:
        update_student(students)

    elif choice == 5:
        delete_student(students)

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
