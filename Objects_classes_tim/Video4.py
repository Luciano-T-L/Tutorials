class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

# Creating a way to add points
    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

# Creating a way to subtract points
    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

# Comparing two points
    # getting the hypotenuse
    def lenght(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

    # greater than...
    def __gt__(self,p):
        return self.lenght() > p.lenght()

    # greater than or equal...
    def __ge__(self, p):
        return self.lenght() >= p.lenght()

    # less than...
    def __lt__(self, p):
        return self.lenght() < p.lenght()

    # less than or equal...
    def __le__(self, p):
        return self.lenght() <= p.lenght()

    # Equal
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    # To print, as a string, de values of our math
    def __str__(self):
        return "(" + str(self.x) + ',' + str(self.y) + ')'


p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 3)
p4 = Point(0, 1)
"""p5 = p1 + p2
p6 = p4 - p1
p7 = p2 * p3

# We have to def a way to print the points, now, we just have for de objects this:
# <__main__.Point object at 0x000002582FCD7A30>
# Creating the fuction __str__, now we have our print with the points values
print(p5, p6, p7)
"""

print(p1 == p2)
print(p1 > p2)
print(p4 <= p3)

