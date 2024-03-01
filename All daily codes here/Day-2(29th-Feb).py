# 29 feb python notes


# 3 naming conventions
# snake_case_pattern
# camelCasePattern
# PascalCasePattern

# we use decimal number system in our real life

print(ord("a")) #print ascii code of a

# data types

# Primitive data types, it can make a copy of itself are called premitive data types 
x = 5 # int data type, from negative infinity to positive infinity, it can be any whole number
v = 5.5 # float data type, from negative infinity to positive infinity, it can be any decimal number
y = "Hello" # str data type, it can be any set of words and characters, it will be under '' or ""
z = True # boolean data type, it can be either True or False
w = 1 + 2j # complex data type, it can be any complex number

# Non-primitive data types, 
a = [1, 2, 3]  # List, it can be any set of values, it will be under []
b = {"name": "John", "age": 25}  # Dictionary, it can be any set of key-value pairs, it will be under {}
c = ("apple", "banana", "cherry")  # Tuple, it can be any set of values, it will be under ()
d = {"apple", "banana", "cherry"}  # Set, it can be any set of values, it will be under {}

s = nve # None data type, it will clear/empty any variable or object 

print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'str'>
print(type(z))  # Output: <class 'bool'>
print(type(a))  # Output: <class 'list'>
print(type(b))  # Output: <class 'dict'>
print(type(c))  # Output: <class 'tuple'>
print(type(d))  # Output: <class 'set'>
print(type(w))  # Output: <class 'complex'>
print(type(v))  # Output: <class 'float'>
print(type(s))  # Output: <class 'NoneType'>