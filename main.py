from menu import (
    print_main_menu,
    print_student_menu,
    print_teacher_menu
)

from student import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)

from teacher import (
    add_teacher,
    view_teachers,
    search_teacher,
    update_teacher,
    delete_teacher
)


while True:

    print_main_menu()

    try:
        choice = int(input("Enter Choice: "))
    except ValueError:
        print("Please enter a valid choice.")
        continue

    # ==========================
    # STUDENT MANAGEMENT
    # ==========================
    if choice == 1:

        while True:

            print_student_menu()

            try:
                student_choice = int(input("Enter Choice: "))
            except ValueError:
                print("Please enter a valid choice.")
                continue

            if student_choice == 1:
                add_student()

            elif student_choice == 2:
                view_students()

            elif student_choice == 3:
                search_student()

            elif student_choice == 4:
                update_student()

            elif student_choice == 5:
                delete_student()

            elif student_choice == 6:
                break

            else:
                print("Invalid Choice")

    # ==========================
    # TEACHER MANAGEMENT
    # ==========================
    elif choice == 2:

        while True:

            print_teacher_menu()

            try:
                teacher_choice = int(input("Enter Choice: "))
            except ValueError:
                print("Please enter a valid choice.")
                continue

            if teacher_choice == 1:
                add_teacher()

            elif teacher_choice == 2:
                view_teachers()

            elif teacher_choice == 3:
                search_teacher()

            elif teacher_choice == 4:
                update_teacher()

            elif teacher_choice == 5:
                delete_teacher()

            elif teacher_choice == 6:
                break

            else:
                print("Invalid Choice")

    # ==========================
    # EXIT
    # ==========================
    elif choice == 3:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
