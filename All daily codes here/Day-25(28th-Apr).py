# Day 25 notes

# Questions on list

# 1. Accept List elements and reprint it
'''''
a = int(input("Enter the numbers you want to add: "))
l = []

for i in range(a):
    z = int(input("Enter the number: "))
    l.append(z)
    
print(l)
'''''
# 2. Print  List elements in reverse order
'''''
# a = int(input("Enter the numbers you want to add: "))
# l = []

# for i in range(a):
#     z = int(input("Enter the number: "))
#     l.append(z)

# print(l)
# print(l[::-1])

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(len(l1)-1, -1, -1):
    print(l1[i])
'''''
# 3. Print positive and negative elements of an List
'''''
l = [25, -56, 45, -89, 78, -45, 12, -78, 45, 23]
l1 = []

for i in l:
    if i >= 0:
        l1.append(i)
    
for i in l:
    if i <= 0:
        l1.append(i)

print(l1)
'''''
# 4. Print list in ascending or descending order
'''''
l = [25, 56, 45, 89, 78, 45, 12, 78, 45, 23]

print(sorted(l))
print(sorted(l, reverse=True))
'''''
# 5. Accept size n from user and create a n size List then take n inputs into the and finally 
#    Print the sum of all elements in the List in the following manner
#    10 + 20 + 30 = 60
'''''
n = int(input("Enter the size of the list: "))
l = []

for i in range(n):
    z = int(input("Enter the number: "))
    l.append(z)    
print(l)

sum = 0
# for i in l:
#     sum += i
# print(l, "=", sum)

for i in range(len(l)):
    sum = sum + l[i]
    if i == len(l)-1:
        print(l[i], "=", sum)
    else:
        print(l[i], "+", end=" ")

'''''
# 6. Mean of List elements.

# l = [25, 56, 45, 89, 78, 45, 12, 78, 45, 23]
