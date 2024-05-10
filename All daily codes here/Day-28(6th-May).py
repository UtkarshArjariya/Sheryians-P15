# Day 28 notes

#  Map, Filter

# Map - map(function, iterable)
# Map is a function that takes in two arguments: a function and a sequence iterable. In the form: map(function, sequence)
# 

l = [21, 34, 56, 78, 90]
lc = [l for i in l if i % 2 == 0]
m = list(map(lambda i:i * 2 / 4, l))  # When we call map function, it is automatically calling lambda function for each element of the list.

# print(lc)
# print(m)

# Filter - filter(function, iterable)
# The filter() function in Python takes in a function and a list as arguments. This offers an elegant way to filter out all the elements of a sequence "sequence", for which the function returns True.
#

f = list(filter(lambda i:i % 2 == 0, l))

# print(f)

''' Higher order functions(HOF) - A function which takes functions as a parameter or returns a function or both is known as higher order function. '''
'''''
def hof():
    return "Hi"

print(hof)   # This will give the memory location of the function
print(hof()) # This will give the whatever is the return value
'''''
'''''
def hof():
    def func():
        return "Hi"
    # return func   # This will return the memory location of the function
    return func()   # This will return the whatever is the return value of the inner function

print(hof())
'''''
# Zip, Enumerate

# Zip - zip(iterable1, iterable2)

l1 = [1, 2, 3, 4, 5]
t = (1, 2, 3, 4, 5)
s = "Hello"
s1 = {1, 2, 3, 4, 5}
d = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}

x = dict(zip(l1, t))

# print(x)