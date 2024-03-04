# 3rd march notes

# Operators in python

'''''
# 1. Arithmetic operators
   +, -, *, /, %, //, **

+  = addition                   # It is used to add two numbers
-  = subtraction                # It is used to subtract two numbers
*  = multiplication             # It is used to multiply two numbers
/  = division                   # It is used to divide two numbers
%  = modulus (remainder)        # It is used to find the remainder of the division of two numbers
// = floor division (quotient)  # It is used to find the quotient of the division of two numbers
** = exponent (power)           # It is used to find the power of a number

# 2. Assignment operators 
   =, +=, -=, *=, /=, %=, //=, **=

=        # It is used to assign the value of the right side to the left side
+=       # It is used to add the value of the right side to the left side and then assign the result to the left side
-=       # It is used to subtract the value of the right side from the left side and then assign the result to the left side
*=       # It is used to multiply the value of the right side with the left side and then assign the result to the left side
/=       # It is used to divide the value of the left side by the right side and then assign the result to the left side
%=       # It is used to find the remainder of the division of the left side by the right side and then assign the result to the left side
//=      # It is used to find the quotient of the division of the left side by the right side and then assign the result to the left side
**=      # It is used to find the power of the left side by the right side and then assign the result to the left side
'''''

# When we use % operator with two numbers, in which the first number is smaller than the second number, then the result will be the first number itself. Means, the remainder will be the first number(Smaller number) itself.
# Example: 2 % 5 = 2

from math import ceil, floor, sqrt


print(2 % 5)  # 2

# Type conversion by programming language is used to help us to perform the operations on the numbers of different types.
# Example: 2 + 2.0 = 4.0, 8.5 + 5j = 8.5 + 5j

print(8.5 + 2 + 5j)  # 10.5 + 5j

# When we use / operator with two numbers, then the result will be a float number, because sometimes you divide 8 by 2 but sometimes you divide 7 by 2. So, the result will be a float number.

print(8 / 2)  # 4.0
print(7 / 2)  # 3.5

#sqrt, pow, floor, ceil is a function of math module, which is used to find the square root, power, floor, and ceiling of a number respectively.
# Example: math.sqrt(25) = 5.0, math.pow(2, 3) = 8.0, math.floor(8.5) = 8, math.ceil(8.5) = 9

# sqrt is used to find the square root of a number. It takes one argument, which is the number itself.
# Example: sqrt(25) = 5
print(sqrt(25))  # 5.0

# pow is used to find the power of a number. It takes two arguments, first is the base and the second is the power.
# Example: pow(2, 3) = 8
print(pow(2, 3))  # 8.0

# floor is used to find the floor of a number. It takes one argument, which is the number itself. // It is a example of floor division.
# Example: floor(8.5) = 8
print(floor(8.5))  # 8

# ceil is used to find the ceiling of a number. It takes one argument, which is the number itself.
# Example: ceil(8.5) = 9
print(ceil(8.5))  # 9

