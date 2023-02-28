# Object-Oriented Programming in Python.
# Inheritance

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old.')

    def speak(self):
        print("I don't know what to say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.color}')


class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def show(self):
        print(f'I am {self.name} and I am {self.age} years old and I am {self.breed}')

    def speak(self):
        print("Bark")

p = Pet("Tuna", 2)
p.speak()
p.show()

c = Cat("Putu", 1, "Blue")
c.speak()
c.show()

d = Dog("Royal", 4, "German Shephard")
d.speak()
d.show()