students = []
while True:
    print("==================================")
    print()
    print("         RK PUBLIC SCHOOL         ")
    print("    SCHOOL MANAGEMENT SYSTEM      ")
    print()
    print("==================================")
    print()
    print()
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = int(input("Enter choice: "))
    if choice == 1:
        Name = input("Enter name:")
        Roll = int(input("Enter roll no:"))
        Marks = int(input("Enter marks:"))
        student = {
            "name": Name,
            "roll": Roll,
            "marks": Marks
        }
        students.append(student)
        print("Students Added Succesfully")

    elif choice == 2:
        if len(students) == 0:
            print("No Student Found")
        else:
            i = 1
            for student in students:

                print("============================")
                print(f"Student {i}")
                i += 1
                print()
                print(f"Name: {student['name']}")
                print(f"Roll: {student['roll']}")
                print(f"Marks: {student['marks']}")
                print("============================")
    elif choice == 3:
        print("Thank You!")
        break
    else:
        print("Invalid Choice")
