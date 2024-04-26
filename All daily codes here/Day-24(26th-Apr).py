# Day 24 notes

# Set comprehension - Set comprehension is an elegant way to define and create sets based on existing sets. Set comprehension is a concise way to create sets
'''''
s = {12, 34, 56, 78, 90, 98, 67, 45, 34, 12, 10}
x = {i/2 for i in s}
print(s)
print(x)
'''''

# Dictionary - denoted by {key:value} pair & empty dictionary is created by {}
# Dictionary is a collection of items that are unordered, changeable and indexed. No duplicate members. It is a collection of items that are unordered, changeable and indexed. It is mutable. It is a collection of items that are unordered, changeable and indexed. It is a collection of items that are unordered, changeable and indexed.

d = {'name': 'John', 'age': 25, 'city': 'New York'}
'''''
d = {}    # empty dictionary
'''''
# Reading the dictionary
'''''
print(d)
print(d["name"])
'''''
# Updating the dictionary
'''''
d['age'] = 26
'''''
# Deleting the dictionary
'''''
del d['city']
'''''

# Dictionary methods
# clear()         - removes all the elements from the dictionary
'''''
d.clear()
'''''
# copy()          - returns a copy of the dictionary
'''''
x = d.copy()
d['name'] = 'Jane'
print(d)
'''''
# get()           - returns the value of the specified key
'''''
print(d.get('name'))
'''''
# items()         - returns a list containing a tuple for each key value pair
'''''
print(d.items())
'''''
# keys()          - returns a list containing the dictionary's keys
'''''
print(d.keys())
'''''
# pop()           - removes the element with the specified key
'''''
print(d.pop('name'))
'''''
# popitem()       - removes the last inserted key-value pair
'''''
print(d.popitem())
'''''
# setdefault()    - returns the value of the specified key. If the key does not exist: insert the key, with the specified value
'''''
print(d.setdefault('name', 'Jane'))
'''''
# update()        - updates the dictionary with the specified key-value pairs
'''''
d.update({'name': 'Jane', 'age': 25, 'city': 'California'})
print(d)
'''''
# values()        - returns a list of all the values in the dictionary
'''''
print(d.values())
'''''

# Dictionary comprehension - Dictionary comprehension is an elegant way to define and create dictionaries based on existing dictionaries. Dictionary comprehension is a concise way to create dictionaries

# traversing through a dictionary
# 1) Traverse through the keys
'''''
for i in d:
    print(i)
'''''
# 2) Traverse through the values
'''''
for i in d.values():
    print(d)
'''''
# 3) Traverse through the key-value pairs
'''''
for i in d.items():
    print(i)
'''''

'''''
x = {i:d[i] for i in d}
# x = {i:d[i] for i in d if d[i] != 'Jane'}
print(x)
# print(d)
'''''