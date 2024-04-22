# Day 20 notes

# Premitive data types 
# It is a data type that is not an object and has no methods. It is a basic data type provided by a programming language.
# These are mutable data types. It basically creates a copy of a variable and stores it in a different memory location.
'''''
a = 5 
b = a 
a = 10
print(a)
print(b)
'''''
# Reference data types

# List  - denoted by [] & empty list is created by list()
# List is a collection of items that are ordered and changeable. Allows duplicate members. This is a important data type in python. It is a sequence data type that can store a collection of items.
'''''
a = [10]
b = a
a[0] = 200
print(a)
print(b)
'''''
# For accessing the elements in a list, we use indexing to itirarte through the list. Indexing starts from 0.
# Example: print(list[start:end:step]) - in this step is the increment value.
'''''
a = [10, 20, 30, 40, 50]
print(a[0])
print(a[1:4:2])
'''''
# del - to delete the element from the list, it is same is remove() but remove() is used to remove the element by value and del is used to remove the element by index.
'''''
# In this there is a example of list slicing and deletion
l = [21, 34, 56, 78, 90, 90, 78, 56, 54, 23, 10]
# print(l[-6:-11:-1])
del l[1]
print(l)
'''''
# Set - denoted by {} & empty set is created by set()
# Set is a collection of items that are unordered and unindexed. No duplicate members. It is a collection of items that are unordered and unindexed. It is mutable. It is a collection of items that are unordered and unindexed. It is a collection of items that are unordered and unindexed.



# Dictionary - denoted by {key:value} & empty dictionary is created by {}
# Dictionary is a collection of items that are unordered, changeable and indexed. No duplicate members. It is a collection of items that are unordered, changeable and indexed. It is mutable. It is a collection of items that are unordered, changeable and indexed. It is a collection of items that are unordered, changeable and indexed.

