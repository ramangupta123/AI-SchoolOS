import json
from student_model import Student


def load_students():
    try:
        # 'with' automatically closes the file, even if an error occurs.
        with open("data/students.json", "r") as file:
            students = json.load(file)
            new_list = []
            for student in students:
                new_list.append(
                    Student(student["name"], student["roll"], student["marks"]))
            return new_list
    except:
        return []


def save_students(students):
    new_list = []
    for student in students:
        new_list.append(student.to_dict())
    with open("data/students.json", "w") as file:
        json.dump(new_list, file)
