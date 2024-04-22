# Day 22 notes

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
# Set is a collection of items that are unordered and unindexed. No duplicate members. It is a collection of items that are unordered and unindexed. It is mutable. It is a collection of items that are unordered and unindexed. It is a collection of items that are unordered and unindexed.
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3}
'''''
s = set()   # empty set
print(type(s))
'''''
# Set methods

# add()           - adds an element to the set
# clear()         - removes all the elements from the set
# copy()          - returns a copy of the set
# difference()    - returns a set containing the difference between two or more sets
# intersection()  - returns a set, that is the intersection of two other sets
# isdisjoint()    - returns whether two sets have a intersection or not
# issubset()      - returns whether another set contains this set or not
# issuperset()    - returns whether this set contains another set or not
# pop()           - removes an element from the set
'''''
x = s.pop()   # It will always remove the last element from the set, it will be random.
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