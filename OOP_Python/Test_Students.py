# Object-Oriented Programming in Python.

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0-100

    def get_grade(self):
        return self.grade

    def set_grade(self, grade):
        self.grade = grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return print("Student added successfully!")
        return print("Student cannot be added :(")

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value+=student.get_grade()

        return value/len(self.students)


s1 = Student("Fajle", 24, 88)
s2 = Student("Abdullah", 24, 65)
s3 = Student("Sahos", 24, 69)
science = Course("Science", 2)
science.add_student(s1)
science.add_student(s2)
science.add_student(s3)
print(science.students[0].name,science.students[0].age)
print(science.get_average_grade())
