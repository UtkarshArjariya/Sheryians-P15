# Day 30 notes

from sys import getsizeof as size  # This is used to get the size of the list or tuple or any other data structure.
from timeit import timeit as time  # This is used to get the time taken by the code to execute.

# Generator 
# Generators are iterators, a kind of iterable you can only iterate over once. Generators do not store all the values in memory, they generate the values on the fly.

l = list(range(1000))
t = tuple(range(1000))

# print(l)
# print(t)

list_size = size(l)
tuple_size = size(t)

# print(list_size)
# print(tuple_size)

list_time = time(f"{l}", number=10)
tuple_time = time(f"{t}", number=10)

# print(list_time)
# print(tuple_time)

# Note - Generator is nothing but the tuple comprehension.

# Generators works as two types:
# 1. Generator function
# 2. Generator expression

# 1. Generator function
# It is a function that returns multiple values one by one. It uses yield keyword to return the values. We can get our desired output whether it is list or tuple or any other data structure. next() function is used to get the values from the generator function.

def dets():
    yield "Username"
    yield "user address"

# print(list(gets()))
x = dets()
# for i in x:
#     print(i)
    
# 2. Generator expression
# 

m = (i for i in l) # Here using the previous list l, we are creating a generator expression.
g = (i for i in l)

# print(m)
# print(g)

m_size = size(m)
g_size = size(g)

# print(m_size)
# print(g_size)

g_time = time("[i for i in list(range(1000))]", number=10)
m_time = time("(i for i in list(range(1000)))", number=10)

print(g_time)
print(m_time)