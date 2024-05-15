# Day 31 notes

# Exception Handling
# try, except, finally, else
# It is a way to handle the errors in the code
'''
try:
    try-block
    code which can raise error
catch Exception as err:
    err holds the error message
'''
# Below is a example of exception handling
'''''
try:
    a = 10
    print(a/b)
    print("All done")
except Exception as err:
    print("Error occured", err)
    
    
print("Hello there!")
'''''
# Another example as different type of errors
'''''
try:
    a = 12
    # b = 'v'
    # print(a/b)
    print(a/0)
    # print("All done")
except NameError as err:
    print("Error >>>", "Variable not defined")
except ZeroDivisionError as err:
    print("Error >>>", "Division by zero")
except TypeError as err:
    print("Error >>>", "Type error")
except Exception as err:
    print("Error >>>", err)
else:
    print("No error")
finally:
    print("Finally block")
'''''

# Creating custom exceptions
# raise keyword is used to raise the exception

# Example of custom exception
'''''
try:
    a = 12
    b = 23
    sum = a + b
    if sum % 2 != 0:
        raise ArithmeticError("Result cannot be odd")
    print(sum)
except ArithmeticError as err:
    print("Error >>>", err)
'''''