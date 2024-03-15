# Day 11 notes

# Loops in python
'''''
i) Loop variable - A variable that changes each time the loop is executed or iterated.
ii) Condition expression - A boolean expression that determines whether the loop should continue.
iii) Updation expression - An expression that changes the loop variable each time the loop is iterated.
iv) Body of loop - The code that is executed each time the loop is iterated.
'''''

# Types of loops - There are two types of loops
'''''
i) Entry controlled loop - In this type of loop, the condition is checked before the execution of the loop body.
Ex - while loop, for loop
ii) Exit controlled loop - In this type of loop, the condition is checked after the execution of the loop body.
Ex - do-while loop

Note - Python does not have exit controlled loop. which means python does not have do-while loop. Because the creators of python doesn't want to add that, it her choice.
'''''

# While loop
'''''
Syntax:
 
loop variable
while(condition expression):
    body of loop
    updation expression
'''''
i = 1
while i <= 10:
    print(i)
    i += 1
print("End of while loop")

# For loop
'''''
Note - i) We ca directly use sequencial & non-sequencial data types in for loop.
ii) When we don't know the number of times a loop will be run, we use while loop.
iii) When we know the number of times a loop will be run, we use for loop.
iv) the range function only use integer values.

Syntax:

for loop variable in range(start, stop, step): # Ex - for i in range(1, 11, 1): or for i in range(1, 11): or for i in range(11):
    body of loop
    
Ex - range(start, end + 1, update)
        - for i in range(1, 11, 1):
     range(start, end + 1) by default update is 1
        - for i in range(1, 11):
     range(end + 1) by default start is 0 and update is 1
        - for i in range(11):
'''''

for i in range(11):
    print(i)
print("End of for loop")

'''''
Note - i) If we wanted to go from 10 to 1, we can use range(10, 0, -1)
ii) By default, the start value is 0 and the update value is 1.
iii) By default the update value is 1.
'''''