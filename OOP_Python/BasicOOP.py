# Object-Oriented Programming in Python.

class Dog:
    # Method is essentially just a funtion inside a class. All of our methods are start with a parameter self.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    def set_age(self, age):
        self.age = age

    def bark(self):
        print(f'ouf uf oof ghrr')

    def add_one(self, x):
        return x+1

d = Dog ("Zero", 20)
print(d.name)
d.set_age(12)
print(d.age)
d2 = Dog("Zazz", 3)
print(d2.get_name())
print(d2.age)
d.bark()
print(d.add_one(5))
print(type(d))