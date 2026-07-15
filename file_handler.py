import json


def load_students():
    try:
        # 'with' automatically closes the file, even if an error occurs.
        with open("data/students.json", "r") as file:
            students = json.load(file)
            return students
    except:
        return []


def save_students(students):
    with open("data/students.json", "w") as file:
        json.dump(students, file)
