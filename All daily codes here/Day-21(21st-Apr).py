# Day 21 notes

# Traversing in the list or Traversing List
l = [10, 51, 875, 452, 111, 41, 56, 2, 1]
'''''
for i in l:
    print(i/2)

i = 0
while i < len(l):
    print(l[i])
    i += 1
'''''
# List comprehension
# With list comprehension you can write all the above code in one line. It is a compact way to create a list and filter it.
'''''
copy = [i for i in l] # map - manuplation(updation)
copy1 = [i for i in l if i % 2 == 0] # filter - selection
copy2 = [i * 2 for i in l if i % 2 == 0] # map + filter
print(copy)
print(copy1)
print(copy2)
'''''
# List methods 
# append(), extend(), insert()
'''''
l.append(159)            # Add the element at the end of the list
l.extend([1, 2, 3])      # Adds multiple elements at the end of the list. It takes an iterable as an argument.
l.insert(2, 100)         # Adds the element at the specified index.
print(l)
'''''
# remove(), pop(), clear()
'''''
l.clear()                # It will remove all the elements of the list
x = l.pop(2)             # It will remove the element at the specified index and you can store it in a variable.
l.remove(100)            # It will remove the element by value.
print(l)
print(x)
'''''
# index(), count(), sort(), reverse(), copy()
'''''
print(l.index(21))               # It will return the index of the element.
print(l.index(21, 0, 5))         # It will return the index of the element in the specified range.
print(l.count(10))               # It will return the number of times the element is present in the list.
print(l.sort())                  # It will sort the list in ascending order.
print(l.sort(reverse=True))      # It will sort the list in descending order.
print(l.reverse())               # It will reverse the list.

m = l.copy()                     # It will create a copy of the list.
m[1] = 123456
print(l)
print(m)
'''''