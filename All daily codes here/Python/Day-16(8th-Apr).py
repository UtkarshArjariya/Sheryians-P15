# Day 16 notes

# 1. Compare two strings without using inbuilt functionsx
'''''
a = input("Enter First string value to compare: ")
b = input("Enter Second string value to compare: ")

if len(a) != len(b):
    print("Not same")
else:
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        else:
            print("Your stings are the not the same")
            break
    else:
        print("Your strings are the same")
'''''
# 2. Count Vowels from given string
# A, a, E, e, I, i, O, o, U, u
'''''
a = input("Enter a any sentence: ")
count = 0
for i in a:
    if i in "aeiouAEIOU":
        count += 1
    
print(count, "is the number of vowels in your statement/sentence")
'''''
# 3. Reverse a string
'''''
a = input("Enter a statement: ")
b = ""

for i in range(len(a)-1, -1, -1):
    b = b + a[i]
print(b)
'''''
# 4. Check string is Pallindrome or not
'''''
a = input("Enter a statement: ")
b = ""
for i in range(len(a)-1, -1, -1):
    b += a[i]

if a == b:
    print("It is pallindrome")
else:
    print("It is not pallindrome")
'''''

# 5. Write a python program to remove all the digits from a string
'''''
a = input("Enter a statement: ") # enter this as input: i love R34 And 5ou 25ve CS0
b = ""
sum = 0

for i in a:
    if i.isdigit():
        sum = sum + int(i)
    else:
        b += i
print(b)
'''''