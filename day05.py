# lists
# A list stores multiple values in one variable.
# students.append("Rahul") students.append("Rahul")
# students.remove("Neha")
# New Concept: in Operator The in operator checks whether something exists.

# dictionaries its like structure:A dictionary stores data in key : value pairs.
# student = {
#     "name": "Raman",
#     "roll": 21,
#     "marks": 92
# }
students = [
    {
        "name": "Raman",
        "marks": 92
    },
    {
        "name": "Aman",
        "marks": 85
    }
]
print(students[0]["name"])
print(students[0]["marks"])
print(students[1]["name"])
print(students[1]["marks"])


#
students = [
    {"name": "Raman", "marks": 92},
    {"name": "Aman", "marks": 85},
    {"name": "Priya", "marks": 96}
]

for student in students:
    print(student["name"])
    print(student["marks"])
    print()
# Notice the last print() adds a blank line between students.
# Here's what you've learned today:
# ✅ Lists
# ✅ Indexing
# ✅ append()
# ✅ remove()
# ✅ in operator
# ✅ Dictionaries
# ✅ Updating dictionaries
# ✅ List of dictionaries
# ✅ Looping through a list of dictionaries
