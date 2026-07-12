student_name = input("Enter student name: ")
marks = int(input("Enter marks: "))

print(f"Student Name: {student_name}")
print(f"Marks: {marks}")

if marks >= 90:
    print(f"Result: A+")
elif marks >= 75:
    print("Result: A")
elif marks >= 60:
    print("Result: B")
elif marks >= 45:
    print("Result: C")
elif marks >= 33:
    print("Result: D")
else:
    print("Result: Fail")

# hw

student_name = input("Enter student name : ")
student_class = int(input("Enter class: "))
roll = input("Enter roll no: ")
marks = int(input("Enter marks: "))
total_fees = int(input("Enter total fees: "))
paid_fees = int(input("Enter paid fees: "))
pending_fees = total_fees - paid_fees

print("================== Student Report ======================")
print(f"Student Name: {student_name}")
print(f"Student Class: {student_class}")
print(f"Roll No: {roll}")
print(f"Marks: {marks}")
if marks >= 90:
    print(f"Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 45:
    print("Grade: C")
elif marks >= 33:
    print("Grade: D")
else:
    print("Grade: Fail")


print(f"Total Fees: {total_fees}")
print(f"Paid Fess: {paid_fees}")
print(f"Pending Fees: {pending_fees}")
if pending_fees > 0:
    print("Fee Status: Pending")
else:
    print("Fee STatus: Paid")


print("========================================================")
