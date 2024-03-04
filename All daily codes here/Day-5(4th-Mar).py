# Day 5 notes


# Shorthand operators
# +=, -=, *=, /=, %=, **=, //=

a = 12
#a += 2
#a **= 2
a //= 2 # a = a // 2, it is because of the floor division , in which the result is rounded off to the nearest whole number
print(a)


# Comparison operators (It will always return a boolean value, it also binary operators)
# ==, !=, >, <, >=, <=  ----- Boolean return

# == # It is used to check whether the two numbers are equal or not
print(2 == 2)  # True

# != # It is used to check whether the two numbers are not equal or not
print(2 != 2)  # False

# >  # It is used to check whether the first number is greater than the second number or not
print(2 > 2)   # False

# <  # It is used to check whether the first number is smaller than the second number or not
print(2 < 2)   # False

# >= # It is used to check whether the first number is greater than or equal to the second number or not
print(2 >= 2)  # True

# <= # It is used to check whether the first number is smaller than or equal to the second number or not
print(2 <= 2)  # True

'''''
# Note: i) If we compare a string with another string, then it will only comapre the first non equal character from the left side of the string to the right side of the string.
ii) In ASCII code capital letter starts from 65 and small letter starts from 97, so the capital letter is always smaller than the small letter.
'''''

# Logical operators (Result always come according to the value)
# and(&&), or(||), not(!)

a = 12 > 15
b = 10 > 8
c = 5 > 8
print(a and b) 
print(a or b)
print(b or a)

# Note: Short circuiting of and operator: If the first condition is false in the and operator, then the second condition will not be checked because the result will be false.

# Falsy values
# 0, 0.0, "", [], {}, None, False

print(0 and 5)  # 0