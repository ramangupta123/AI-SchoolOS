class Student:

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print(f"Name : {self.name}")
        print(f"Roll : {self.roll}")
        print(f"Marks: {self.marks}")

    def to_dict(self):
        return {
            "name": self.name,
            "roll": self.roll,
            "marks": self.marks
        }
