# Day 26 notes

# 1. Pallindromic List - Write a program to check if elements of an List are same or not it read from front or bacExample : arr= [2,3,15,15,3,2]
'''''
a = [1,2,3,3,2,1]

j = len(a)-1

for i in range(len(a)//2):
    if a[i] == a[j]:
        j -= 1
        continue
    else:
        print("Lsit is not pallindrome")
        break
else:
    print("List is pallindrome")
'''''

# Questions on Dictionary
# denoted by {key:value} pair & empty dictionary is created by {}

# 1. Write a Python program to iterate over dictionaries using for loops
'''''
a = {1:67,9:89,2:45}

for i in a.keys():
    print(a[i])
    
for j in a.values():
    print(a[i])
    
for k in a.items():
    print(a[i])
'''''
# 2. Write a Python script to merge two Python dictionaries.
'''''
a = {1:29,3:56,5:69}
b = {2:129,4:45,6:12}

# a.update(b)             # If there is a similar value in both the dictionary of the same key, it will overwrite the new value over previous one.

# print(a)

# a[7] = 89               # It will create a new value in the dictionary, if the same key exist in the dictionary it will overwrite or if not it will create a new value pair

for i in b:
    a[i] = b[i]
    
print(a)
'''''
# 3. Write a Python program to sum all the values in a dictionary.
'''''
a = {1:56,2:5,3:9,4:69}
sum = 0
for i in a.values():
    sum += i
    
print("Sum of all values is: ", sum)
'''''
# 4. Convert a list to dictionary
'''''
a = [1,23,4,45,6,7,8,9]
d = dict()

for i in range(0,len(a),1):
    d[i] = a[i]
    
print(d)
'''''
# 5. Count the frequency of each elements
'''''
a = [1,1,1,2,2,2,3,3,3]
f = {}

for a in a:
    if a in f:
        f[a] += 1
    else:
        f[a] = 1
        
print("Frequency of elements is:", f)
'''''
# 6. Write a Python program to combine two dictionary by adding values for common keys.
'''''
a = {1: 10, 2: 20, 3: 30}
b = {2: 5, 3: 15, 4: 25}

for key in b:
    if key in a:
        a[key] += b[key]
    else:
        a[key] = b[key]

print(a)
'''''