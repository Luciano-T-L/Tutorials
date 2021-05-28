# Creating new class "Dog"
class Dog(object):
    # Constructor method (__init__). If you want anything to happen initially when you first create
    # a class you have to this init method.
    # name and age are parameters
    def __init__(self, name, age):
        # Dog has-a name (attributes)
        self.name = name
        self.age = age
        self.li = [1, 2, 3]

    # Method, anything that you create using "def", looks like a function, but you have to call them using an object
    def speak(self):
        print("Hi, I'm", self.name, "and I'm", self.age, "years old")

    # Creating another method to change the name
    def change_name(self, age):
        self.age = age

    # Create a new instance attribute that is going to be apply to Dog class, that is note a attribute
    # because it's not in the constructor method __init__
    def add_weight(self, weight):
        self.weight = weight


# Creating a instance of type Dog, the init method is called automatically
tim = Dog("Tim", 10)  # Now a have to give it a parameter "name" and the parameter "age"
# We don't have to say:
# tim.__init__()

# fred is a instance of class Dog and it have a name and a age
fred = Dog("Fred", 5)  # Now a have to give it a name and a age
# I'm saying to python: fred.name = "Fred"

# Calling a method
tim.speak()
fred.speak()
tim.change_name(8)
tim.speak()

# If I just want to know the age.
print(tim.age)
# Or the name
print(fred.name)

# With classes we can create infinite amount of objects of that type class and have all the
# properties and attributes apply to them.

# Using method
tim.add_weight(70)
# Calling the information
print(tim.weight)
# If we do it: we have a error, because fred (or the dog object) don't have the attribute "weight"
print(fred.weight)
