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
'''''
l = [25, 56, 45, 89, 78, 45, 12, 78, 45, 23]
sum = 0
for i in l:
    sum += i
print("Average of the list is: ",sum/len(l))
'''''
# 7. Find the greatest element and print its index too.
#    {2, 96, 69, 77, 145, 20} = Max element = 145 found at 4 index
'''''
l = [2, 96, 69, 77, 145, 20]
max = l[0]

for i in l:
    if i>max:
        max = i
        
print(f"Max element = {max} \nFound at {l.index(max)} index")
'''''
# 8. Find the smallest element and print its index too.
#    {2, 96, 69, 77, 145, 20} = Min element = 2 found at 0 index
'''''
l = [2, 96, 69, 77, 145, 20]
small = l[0]

for i in l:
    if i < small:
        small = i
        
print(f"Min element = {small} \nFound at {l.index(small)} index")
'''''
# 9. Find the second greatest element0 
#    {2, 96, 69, 77, 145, 20} = Second greatest element = 96
'''''
l = [2, 96, 69, 77, 145, 20]
smax = l[0]

for i in l:
    if i>smax:
        smax = i
        
l.remove(smax)
smax = l[0]

for i in l:
    if i>smax:
        smax = i
        
print(f"Second greatest element on the list: {smax}")

#                   or

l = [2, 56, 89, 3, 41, 66, 42]
max = l[0]
max2 = 0

for i in l:
    if i > max:
        max2 = max
        max = i
    elif i > max2:
        max2 = i
        
print(f"Second greatest element on the list: {max2}")
'''''
# 10. Check if List is sorted or not.
'''''
l = [1,2,3,4,5,6]
l1 = l.copy()

l.sort()

if l1 == l:
    print("List is sorted")
else:
    print("List is not sorted")
'''''
