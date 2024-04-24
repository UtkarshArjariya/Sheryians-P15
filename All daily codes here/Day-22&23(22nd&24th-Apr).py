# Day 22 & 23 notes

# Tuple - denoted by ()
# Tuple is a collection of items that are ordered and unchangeable. Allows duplicate members. It is a sequence data type that can store a collection of items. It is immutable. It is sequence data type that can store a collection of items.
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3)
'''''
print(t[1])
print(t[-1])
print(t[1:10:2])
'''''
# Tuple methods
# count() - returns the number of times a specified value occurs in a tuple
# index() - searches the tuple for a specified value and returns the position of where it was found
'''''    # Tuple methods
print(t.count(1))
print(t.index(1))
print(len(t))
'''''
'''''    # Traversing in tuple with for and while loop
for i in t:
    print(i)

i = 0
while i < len(t):
    print(t[i])
    i += 1
'''''


# Set - denoted by {} & empty set is created by set()
# Set is a collection of items that are unordered and unindexed. No duplicate members. It is a collection of items that are unordered and unindexed. It is mutable. It is a collection of items that are unordered and unindexed. It is a collection of items that are unordered and unindexed. Only for loop can be used to traverse the set without using len() function.
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3}
'''''
s = set()   # empty set
print(type(s))
'''''
# Set methods - visit w3schools for more detailed explanation.

# add()           - adds an element to the set
'''''
s.add(123)
print(s)
'''''
# clear()         - removes all the elements from the set
'''''
s.clear()
print(s)
'''''
# copy()          - returns a copy of the set
'''''
import numpy as np
x = [1, 2, 3, 4, 5, 6]
y = np.array(x)


'''''
# difference()    - returns a set containing the difference between two or more sets
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
'''''
print(a.difference(b))   # a - b, It will print the elements which are present in a but not in b
print(b.difference(a))   # b - a, It will print the elements which are present in b but not in a
'''''
# difference_update() - removes the items in this set that are also included in another, specified set
'''''
a.difference_update(b)
print(a)
'''''
# intersection()  - returns a set, that is the intersection of two other sets
'''''
print(a.intersection(b))
'''''
# union           - returns a set containing the union of sets
'''''
print(a.union(b))
'''''
# isdisjoint()    - returns whether two sets have a intersection or not
'''''
print(b.isdisjoint(a))  # If there is no common element between a and b then it will return True otherwise False
'''''
# issubset()      - returns whether another set contains this set or not
'''''
print(b.issubset(a))    # If all the elements of b are present in a then it will return True otherwise False
'''''
# issuperset()    - returns whether this set contains another set or not
'''''
print(b.issuperset(a))  # If all the elements of a are present in b then it will return True otherwise False
'''''
# pop()           - removes an element from the set
'''''
x = s.pop()   # It will always remove the first element from the set.
print(x)
'''''
# remove()        - removes the specified element
'''''
s.remove(123)  # if the element is not present in the set then it will give an error
'''''
# discard()       - removes the specified element
'''''
s.discard(123)  # if the element is not present in the set then it will not give an error
'''''
# update()        - updates the set with the union of this set and others
'''''
s.update({11, 12, 13, 14, 15})
print(s)
for i in s:
    print(i)
# We cannot use while loop in set because it is unordered and unindexed.
'''''