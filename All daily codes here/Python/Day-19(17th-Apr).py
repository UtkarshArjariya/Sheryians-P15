# Day 19 notes

# Stack - LIFO (Last In First Out) or FILO (First In Last Out)
# Stack is a linear data structure which follows a particular order in which the operations are performed.
# Example-
'''''
def hello1():
    hello2()
    print(1)
    
def hello2():
    hello3()
    print(2)
    
def hello3():
    hello4()
    print(3)
    
def hello4():
    print(4)
    
hello1()
'''''
# Recursion - A function calling itself
# Example-
'''''
def hello(n):
    if n == 0:
        return
    else:
        hello(n-1)
        print(n)

hello(10)
'''''
'''''
def hello(n):
    if n == 0:
        return
    else:
        print(n)
        hello(n-1)
        
hello(10)
'''''
# Write a program using function to check if a number is pallidrome or not
'''''
def pallindrome(x):
    copy = x
    rev = 0
    while x > 0:
        rev = rev*10 + x%10
        x = x//10
        
    if copy == rev:
        return True
    else:
        return False
    
a = int(input("Enter a number: "))
if pallindrome(a):
    print("Pallindrome")
else:
    print("Not Pallindrome")
'''''


# Your task is to go through all the question that has been done in the previous days and try to solve them.
# If possible try another way to solve the same question.