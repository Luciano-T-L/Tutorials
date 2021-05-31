class Dog:
    # When you create a class variable, you do this at the top of the class
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    # Elso called "decorators"
    @classmethod
    # can use class methods and variables
    def num_dogs(cls):
        return len(cls.dogs)

    # Can't use class methods or class variables
    # Elso called "decorators"
    @staticmethod
    def bark(n):
        # Barks n times
        for _ in range(n):
            print("Bark!")


"""tim = Dog('Tim')
jim = Dog("Jim")
# print(Dog.dogs)

# Calling num_dogs method
print(Dog.num_dogs())
# or
print(tim.num_dogs())"""

# Calling static method (don't use any argument of Dog class
Dog.bark(5)
