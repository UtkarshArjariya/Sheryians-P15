# Day 17

# Functions in python 
# Functions are a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable, reuse it and save some time. Also functions are a key way to define interfaces so programmers can share their code.

# Their are two types of functions in python
# 1. Built-in functions
# 2. User-defined functions

# Built-in functions
# Functions that are built into Python that are always available for use. Some of the most common built-in functions include print(), input(), len(), int(), float(), str(), list(), dict(), set(), and tuple().
# Example:
'''''
print("Hello World")
print(len("Hello World"))
print(int(5.6))
print(float(5))
print(str(5))
print(list("Hello World"))
print(dict(name="John", age=36))
print(set("Hello World"))                  # etc.
'''''
# User-defined functions
# Functions that users create themselves to perform specific tasks. These functions can be reused in other parts of the program.
# non - parameterized function / impure function / function without argument 
# These functions do not take any arguments. They are called impure functions because they depend on variables that are not passed as arguments.
'''''
x = 12
y = 13
def add():
    a = x 
    b = y
    print(a+b)
add()
'''''
# parameterized function / function with argument / pure function
# These functions take arguments. They are called pure functions because they depend only on the arguments passed to them.
'''''
def addd(c, d):
    sum = c + d
    print(sum)
addd(12, 13)
'''''
# Function with return statement
# Functions can return a value to the caller. It will retrun the result of the function out of the function scope. In this function call is replaced by its return value.
'''''
def product(e, f):
    r = e * f
    return r
e = 12 
f = 4
res = product(e, f)
c = 2
print(res / c)
'''''
'''''
# Rules of functions

1. A function can only have one return and that must be the last statement/line in the function.
2. we can return only single entity from the function.
'''''
# Variable length parameter/arguments
'''''
def apnaprint(*a):
    print(a)
    
# *args must be the last statement in the function definition.
# We can use only 1 *args in a function definition.
'''''
# Example of variable length parameter/arguments
'''''
def dets(name, batch, *hobbies):
    print("Name:", name)
    print("Batch:", batch)
    print("Hobbies:", hobbies)
    
dets("John", 2020, "Reading", "Writing", "Coding")
dets("Amir", 2021, "Reading", "Writing")
'''''
