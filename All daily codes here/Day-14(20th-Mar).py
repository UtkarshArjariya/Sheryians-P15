# Day 14 notes

# Question on Conditional statement

# 7. Print the sum of all even & odd numbers in a range seperately.
'''''
n=int(input("Enter a number: "))
sum_even = 0
sum_odd = 0
for i in range(1,n+1,1):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
        
print(sum_even)
print(sum_odd)
'''''
# 8. Print all the numbers which are either divisible by 3 or 5 in a range
'''''
n = int(input("Enter a number: "))
for i in range(1, n+1, 1):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
'''''
# 9. Print all the factor of a number
'''''
n = int(input("Enter a number: "))
print("The factor of",n,"are:")
for i in range(1, n+1):
    if n % i == 0:
        print(i)
'''''
# 10. Print the sum of all factors of a number, 50 - 1 + 2 + 5 + 10 + 25 = 43
'''''
n = int(input("Enter a number: "))
fact_sum=0
for i in range(1, n+1):
    if n % i == 0:
        fact_sum += i
print("The sum of factor of",n,"is:",fact_sum)
'''''
# 11. Accept a number and check if it a perfect number or not.
#     A number whose sum of factors(excluding number itself)  = Number 
#     Ex -  6 = 1, 2, 3 = 6
'''''
n = int(input("Enter a number: "))
sum_factors = 0
for i in range(1, n):
    if n % i == 0:
        sum_factors += i

if sum_factors == n:
    print("It is a perfect number")
else:
    print("It is not a perfect number")
'''''
# 12. Seprate each digit of a number and print it on the new line
'''''
n = int(input("Enter a number: "))
while n > 0:
    sep = n % 10
    print(sep)
    n = n//10
'''''
# 13. Check if the number is Prime or not.
'''''
n = int(input("Enter a number: "))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        count += 1
if count == 2:
    print("It is a prime number")
else:
    print("It is not a prime number")
'''''
# 14. Accept a number and print its reverse
'''''
n = int(input("Enter a number: "))
while n > 0:
    rev = n % 10
    print(rev, end="")
    n = n//10
'''''
# 15. Accept a number and check if it is a pallindromic number (If number and its reverse are equal)
# Ex - 12321 - Rerverse - 12321
'''''
n = int(input("Enter a number: "))
temp = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n//10
if temp == rev:
    print("It is a pallindromic number")
else:
    print("It is not a pallindromic number")
'''''
