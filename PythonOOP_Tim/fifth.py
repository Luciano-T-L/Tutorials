# Static and class method/ class attributes

class Person:
    # Class attribute, will not change with from person to person
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

# Class methods - they act in class methods (cls)

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

"""print(Person.number_of_people)
p1 = Person("Tim")

print(p1.number_of_people)
p2 = Person("Jill")

print(p2. number_of_people)"""

p1 = Person("Tim")
p2 = Person("Jill")
print(Person.number_of_people_())