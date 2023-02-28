# Object-Oriented Programming in Python.
# Class & Static Method

# ------------ Class Method ------------
class Person:
    numbers_of_people = 0

    def __init__(self,name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_person(cls):
        return cls.numbers_of_people

    @classmethod
    def add_person(cls):
        cls.numbers_of_people += 1


p1 = Person("Fajle")
p2 = Person("Sahos")
print(Person.number_of_person())


# ------------ Static Method ------------









