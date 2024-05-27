# Day 13 notes

# Range function: range(start, stop, step)

# Example - printing the table of 5
# for i in range(5, 51, 5):
#     print(i)

# Example - Taking number input from user and printing the table of that number
# n = int(input("Enter a number: "))
# for i in range(n, (n*10)+1, n):
    # print(i)

# Starting question for iteration operations

# 1. Take any number input from user and print "Hello World!" that many times
'''''
n = int(input("Enter a number: "))
for i in range(0, n):
    print("Hello World!")
'''''
# 2. Take number input from user and print natural number n times
'''''
n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(i)
'''''
# 3. Reverse loop from n to 1.
'''''
n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    print(i)
'''''
# 4. Take nuber input from user and print its table like 5 * 1 = 5
'''''
n = int(input("Enter a number: "))
for i in range(1, 11, 1):
    # print(n,"*",i,"=",n*i)
    print(f"{n} * {i} = {n*i}")
'''''
# 5. Take number input from user and sum upto n terms
'''''
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1, 1):
    sum += i
print(sum)
'''''
# 6. Factorial of n terms
'''''
n = int(input("Enter a number: "))
fact = 1
for i in range(1,n+1,1):
    fact *= i
print(fact)
'''''