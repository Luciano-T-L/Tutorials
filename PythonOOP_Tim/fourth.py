# Inheritance

"""class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("Bark")
"""

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say!")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name}, I am {self.age} years old and I'm {self.color}")

p = Pet("Tim", 19,)
p.show()
p.speak()

c = Cat("Bill", 34, "Brown")
c.show()
c.speak()

d = Dog("Kill", 29)
d.show()
d.speak()

