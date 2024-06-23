# OOPS Day 3 notes

import string
import random

def password_generator():
    lower = random.choices(string.ascii_lowercase, k=3)
    upper = random.choices(string.ascii_uppercase, k=2)
    digit = random.choices(string.digits, k=2)
    symbol = random.choices("!@#$%^&*()_+", k=1)

    password = lower + upper + digit + symbol
    print(password)
    # random.shuffle(password)
    # return "".join(password)

print(password_generator())

# Converting a this code to a package, so that we can use it in other files as well by importing it

# Create a folder named "password_generator" and create a file named "__init__.py" inside it
# Create a file named "generate.py" and paste the above code in it
# Now you can use this code in other files by importing it as: from password_generator.generate import password_generator