# Q1. Please take 2 inputs for string and one for N numberof rotation, you have to rotate your string N number of times.
# Example: Input- string = "Brother" Output- "rehBrot"

string = input("Enter a string value: ")
n = int(input("Enter a number to rotate the string: "))

rotate = string[-n:] + string[:-n]

print(rotate)