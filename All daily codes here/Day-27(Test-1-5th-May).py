# Day 27 - Test till loop, if-else and string

# 1. Create a python program to calculatethe total tax payable to all the government if the salary is below 3 lakhs the person has to pay no tax if the salary is above 3 lakhs 10% above 5 lakhs 15% tax above 7 lakhs 20% tax.
'''''
s = int(input("Enter your salary: "))

if s <= 300000:
    print("No need to pay tax")
elif 300000 < s <= 499999:
    s1 = (10 / 100) * s
    print(f"The tax payable at {s} is {s1}")
elif 500000 < s <= 699999:
    s2 = (15 / 100) * s
    print(f"The tax payable at {s} is {s2}")
elif s > 700000:
    s3 = (20 / 100) * s
    print(f"The tax payable at {s} is {s3}")
'''''

# 2. Reverse the number without using string function
'''''
a = int(input("Enter your number: "))

rev = 0
while a > 0:
    remainder = a % 10
    rev = (rev * 10) + remainder
    a = a // 10

print("Reversed number: ", rev)
'''''

# 3. Take a string input and remove spaces from that string without using replace() or any functions.
'''''
b = input("Enter you sentence to remove spaces: ")

spaces = ""
for char in b:
    if char != " ":
        spaces += char

print("sentence without spaces:", spaces)
'''''
# 4. Print prime number to a range
'''''
p = int(input("Enter the range to print prime number: "))

for num in range(2, p+1):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)
'''''
# 5. Check whether the number is armstrong or not
'''''
num = int(input("Enter the number: "))
sum = 0

for i in str(num):
    sum += int(i) ** 3
    
if sum == num:
    print("Armstrong number")
else:
    print("Not an armstrong number")
'''''