student_name = input("Enter student name : ")
student_class = int(input("Enter class: "))
roll = input("Enter roll no: ")
total_fees = int(input("Enter total fees: "))
paid_fees = int(input("Enter paid fees: "))
pending_fees = total_fees - paid_fees

print(f"Student Name: {student_name}")
print(f"Student Class: {student_class}")
print(f"Roll No: {roll}")
print(f"Total Fees: {total_fees}")
print(f"Paid Fess: {paid_fees}")
print(f"Pending Fees: {pending_fees}")
