# Day 10 notes

# 7. Accept the parameters and calculate the Compound Interest & print it on STDOUT (Use Math class methods)
'''''
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time period (in years): "))

compound_interest = principal * (1 + rate/100) ** time - principal

print("Compound Interest:", compound_interest)
'''''
# 8. Accept a year and check if it a leap year or not (A leap year is a year that is exactly divisible by 4 except for century years (years ending with 00). The century year is a leap year only if it is perfectly divisible by 400))
'''''
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
'''''
'''''
year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year")
    
elif year % 100 == 0 and year % 400 == 0:
    print(f"{year} is a leap year")
    
else:
    print(f"{year} is not a leap year")
'''''
# 9. Accept an english alphabet from user and check if it is a consonent or a vowel
'''''
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vow = input("Enter an alphabet: ")
if vow in vowel:
    print(f"{vow} is a vowel")
else:
    print(f"{vow} is a consonent")
'''''
'''''
alp = input("Enter an alphabet: ")
if alp in "aeiouAEIOU":
    print(f"{alp} is a vowel")
else:
    print(f"{alp} is a consonent")
'''''
'''''
alp = input("Enter an alphabet: ")
if alp.isnumeric() or len(alp) > 1:
    print("Bhaag ja lawde")
elif alp in "aeiouAEIOU":
    print(f"{alp} is a vowel")
else:
    print(f"{alp} is a consonent")
'''''