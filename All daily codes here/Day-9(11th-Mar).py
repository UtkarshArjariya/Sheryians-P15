# Day 9 notes

# In this we will be practicing the conditional statements in python

# 1. Take 3 inputs from user and check and print the result of the following conditions:
#    a. All numbers are equal (Use and & or)
#    b. Any of the numbers are equal (Use and & or)
'''''
a = input("Enter the first number: ")
b = input("Enter the second number: ")
c = input("Enter the third number: ")

if a == b:
    if b == c:
        print("All numbers are equal")
    else:
        print("First two numbers are equal")
elif b == c:
    print("Last two numbers are equal")
elif a == c:
    print("First and last numbers are equal")
else:
    print("All numbers are different")
'''''
# 2. Accept two number and print the greater number
'''''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: ")) 

if num1 > num2:
    print("First input is greater ", num1)
else:
    print("Second number is greater ", num2)
'''''
# 3. Accept the gender from the user as char(string) and print the respective greeting message
'''''
print("Please enter M/m is your Male & F/f is you're female")
gen = str(input("please, enter your gender: "))

if gen == "m" or gen == "M":
    print("Please to meet you, sir")
else:
    print("Please to meet you, ma'am")
'''''
# 4. Extend the previous questions and address the wrong inputs
'''''
print("Please enter M/m is your Male & F/f is you're female")
gen = str(input("please, enter your gender: "))
# m = male
# female = fe

if gen == "m" or gen == "M":
    print("Please to meet you, sir")
elif gen == "f" or gen == "F":
    print("Please to meet you, ma'am")
else:
    print("Please re-enter your input")
'''''
# 5. Accept an integer and check whether it is an even number or odd.
'''''
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("This number is even")
else:
    print("This number is odd")
    
# print("Even number") if num % 2 == 0 else print("Odd number")  # This is a one liner code
'''''
# 6. Accept name and age from user. Check if the user is a valid voter or not
'''''
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18 and age <= 150:
    print(f"{name} you are a valid voter")
elif age < 18 and age > 0:
    print(f"{name} you can vote after {18 - age} years")
else:
    print(f"{name} please enter a valid age")
'''''