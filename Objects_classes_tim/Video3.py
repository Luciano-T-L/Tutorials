"""# Creating a class dog (is-a object)
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Hello, I'm", self.name, 'and I am', self.age, 'years old')

    def talk(self):
        print("Bark!")


# Inheritance (Cat is-a Dog)
# Every method, attributes, properties from Dog will be pass to the Cat class
class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

# We can overwrite the method talk from dog, now, when we call .talk() to Cat', it will print "Meowl!"
    def talk(self):
        print("Meow!")


tim = Cat('Tim', 5, "Blue")
# in class Cat, we didn't create the speak method, but it's was created in dog class, so Cat's
# will inherit the method speak
tim.speak()
tim.talk()

print("")

jim = Dog("Jim", 2)
jim.speak()
jim.talk()
"""

