while 1:
    print("======================================")
    print("          R.K. PUBLIC SCHOOL          ")
    print("       SCHOOL MANAGEMENT SYSTEM       ")
    print("======================================")

    print("1. Add Student")
    print("2. Generate Report Card")
    print("3. Fee Collection")
    print("4. Exit")

    choice = int(input("Enter a choice: "))

    if choice < 1 or choice > 4:
        print("Invalid choice")
    elif choice == 1:
        print("Add Student Selected")
    elif choice == 2:
        print("Generate Report Card Selected")
    elif choice == 3:
        print("Fee Collection Selected")
    else:
        print("Thank you for using School Management System")
        break
