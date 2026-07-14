import json

file = open("data/students.json")
students = json.load(file)
print(students)
