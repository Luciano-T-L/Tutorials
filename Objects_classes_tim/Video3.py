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


class Veichle:
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasleft(self):
        return self.gas


class Car(Veichle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        print("Beep beep")


class Truck(Veichle):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires

    def beep(self):
        print("Honk")
