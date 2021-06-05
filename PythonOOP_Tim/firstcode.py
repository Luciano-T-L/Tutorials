# Object Orientated Programming in Python

"""def hello():
    print("Hello")


x = 1  # x is equal to the object which is a type integer with the value 1.

print(type(hello))
"""

# Methods

"""string = "hello"
print(string.upper())  # upper() is a method acting on a especific object
"""

# Creating classes

# Now I can definig the operations that a dog is able to do.
class Dog:
    # This method will allows us to instantiate the object right when it is created
    # So, when we create a new Dog instance, this method will be called
    def __init__(self, name):
        # Create an attribute of the class dog which is name
        self.name = name

    # A method is essentially just a function that goes inside of a class.
    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")

"""d = Dog()  # The variable d and I'm going to assign it to a instance of the class Dog.
# Calling a mthod on my dog object
d.bark()
print(d.add_one(5))
print(type(d))"""

# Using __init__

# Now we have two different dog objects.
d = Dog("Tim")
print(d.name)
d2 = Dog("Bill")
print(d2.name)
