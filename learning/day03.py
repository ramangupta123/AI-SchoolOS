student_name = input("Enter student name: ")
marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance: "))
pending_fees = int(input("Enter pending fees: "))


print("================Student Report===================")
print(f"Student Name: {student_name}")
print(f"Marks: {marks}")
print(f"Attendance: {attendance}")

if marks >= 33:
    print("Result: Pass")
else:
    print("Result: Fail")


if attendance >= 75 and pending_fees == 0:
    print("Exam Status: ELigible")
else:
    print("Exam Status: Not Eligible")
