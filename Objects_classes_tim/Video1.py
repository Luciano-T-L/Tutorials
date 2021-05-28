# x is a object of type int
x = 5
# y is a object of type str
y = "string"
# f is a object of type float
f = 5.5

print(type(x))
print(type(y))

import turtle

# creating a new turtle object called it tim
tim = turtle.Turtle()


# Methods vs functions

# Function - Something that's gonna take an object and apply an operations
def func(x):
    return x + 1


# Calling a function func_name(argument or instance)
print(func(5))

# Method .upper() (Only works in str type) - anything you're calling on an object itself
# Calling a method instance.method()
print(y.upper())

# Passing a object of type string (s) and passing another object of type string ('')
print(y.replace('s', ''))
