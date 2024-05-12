# Day 29 test


# 1. Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''''
a = int(input("Enter the number of elements: "))
l = []
for i in range(a):
    num = int(input("Enter a number: "))
    l.append(num)

for i in l:
    if l.count(i) > 1:
        print("True")
        break
    else:
        print("False")
        break
'''''
# 2. Given two strings ransomNote and magazine, return ture if ransomeNote can b constructedby using the letter from magazine and false otherwise. Each letter in magazine can only be used once in ransomenote.
'''''
ransomeNote = input("Enter a string for ransomeNote: ")
magazine = input("Enter a string for magazine: ")

for i in ransomeNote:
    if i in magazine:
        magazine = magazine.replace(i, '', 1)
    else:
        print("False")
        break
else:
    print("True")
'''''
# 3. You have a set of integerss, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which result in the repetitionof one number and loss of another number. You are given an integer array nums representing the data status of this set after the error. Find the number that occurs twice and the number that is missing and return them in the form of an array.
'''''
a = int(input("Enter the number of elements: "))
s = []
for i in range(a):
    num = int(input("Enter a number: "))
    s.append(num)

for i in range(len(s)-1):
    if int(s[i])+1 == int(s[i+1]):
        continue
    else:
        a = int(s[i])+1
        print(s[i],a)
        break
'''''