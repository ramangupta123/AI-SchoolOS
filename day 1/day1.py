# Student Information System

# Step 1: Take input from the user
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
student_class = input("Enter class: ")

# Step 2: Take marks for 5 subjects
marks = []

for i in range(5):
    mark = float(input(f"Enter marks for Subject {i + 1}: "))
    marks.append(mark)

# Step 3: Calculate total
total = sum(marks)

# Step 4: Calculate percentage
percentage = (total / 500) * 100

# Step 5: Check Pass or Fail
if percentage >= 40:
    result = "Pass"
else:
    result = "Fail"

# Step 6: Assign Grade
if percentage >= 90:
    grade = "A"
elif percentage >= 75:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

# Step 7: Print Report
print("\n========== STUDENT REPORT ==========")
print(f"Name       : {name}")
print(f"Roll No    : {roll_no}")
print(f"Class      : {student_class}")
print(f"Marks      : {marks}")
print(f"Total      : {total}/500")
print(f"Percentage : {percentage:.2f}%")
print(f"Result     : {result}")
print(f"Grade      : {grade}")
print("====================================")
