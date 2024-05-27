# Day 12 notes

# Keywords in loops

# There are 4 keywords in loops
# i) break
# ii) continue
# iii) else
# iv) pass


# i) break: It is used to break the loop and come out of the loop
'''''
example -  
n = 11
while n >= 1:
    n = n - 1
    if i == 5:  # if i becomes 5, then break the loop
        break   # stops the loop and take the control out of the loop
        print(n)
        # This runs after the break statement
    print("Loop is broken")
'''''

# ii) continue: It is used to skip the current iteration and continue with the next iteration
'''''
example - 
n = 11
while n >= 1:
    n = n - 1
    if n == 5:
        continue  # if n becomes 5, then skip the current iteration and continue with the next iteration
    print(n)
'''''

# iii) else: It is used to execute a block of code when the loop is finished
'''''
example - 
n = 11
while n >= 1:
    n = n - 1
    if n == 5:
        continue
    print(n)
else:
    print("Else ran...")
'''''

# iv) pass: It is used to write an empty loop
'''''
example - # Below is an infinite loop be becasue there is no condition to break the loop
n = 11
while n >= 1:
    pass
    
if n % 2 == 0:
    pass
else:
    print(n)
'''''