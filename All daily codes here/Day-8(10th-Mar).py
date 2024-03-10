# Day 8 notes

# Conditional statements: These statements are used to execute a block of code based on a condition. Example: if 9 > 0: print("Positive number") else: print("Negative number")

# Simple if statement
'''''
 if condition: 
     statement
'''''
n = 10
if n > 0:
    print("Positive number")
    
# if-else statement
'''''
 if condition:
     statement
 else:
     statement
'''''
n = -9
if n > 0:
    print("Positive number")
else:
    print("Negative number")

# Ladder/multiple if-else statement or If-elif-else statement

'''''
if condition:
    statement
elif condition:
    statement
else: 
    statement
'''''

n = 0
if n > 0:
    print("Positive number")
elif n < 0:
    print("Negative number")
else:
    print("Zero")

# Nested if-else statement

'''''
if condition:
    if condition:
        statement
    else:
        statement
else:
    statement
'''''
n = -2
if n > 0:
    if n % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
elif n < 0:
    if n % 2 != 0:
        print("Negative odd number")
    else:
        print("Negative even number")
else:
    print("Zero")
    
# Nested to ladder if-else statement
'''''
if condition:       # here we will add the both the conditions which were in nested if-else
    statement
elif condition:
    statement
else:
    statement
'''''

n = 5
if n > 0 and n % 2 == 0:
    print("Positive even number")
elif n > 0 and not(n % 2 == 0):  # not is used to reverse the condition, other way to write this is 'n % 2 != 0'
    print("Positive odd number")
elif n < 0 and n % 2 != 0:       # Check this for above comment
    print("Negative odd number")
elif n < 0 and n % 2 == 0:
    print("Negative even number")
else:
    print("Zero")

# Conditional expression or Ternary operator: It is used to assign a value to a variable based on a condition. Syntax: variable = value1 if condition else value2 
# Example: result = "Positive number" if n > 0 else "Negative number"

age = 8
res = "Can vote" if age >= 18 else "Cannot vote"
print(res)