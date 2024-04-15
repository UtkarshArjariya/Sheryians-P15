# Day 15 notes

# Lambda function
'''''
sum = lambda a, b: a + b
#  variable = lambda arguments: retrun_value

print(sum(5, 6))
'''''
# Default parameter
'''''
# Default parameter must be the last parameter
# There should be one default parameter in a function

def dets(name, age, batchcode="P15"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Batch: {batchcode}")
    
dets("Rahul", 20, "Python")
dets("Rahul", 20)
'''''
# Keyword arguments/named parameters
'''''
# Given parameteres are -> batchcode, name and age
def dets(name, age, batchcode="P15"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Batch: {batchcode}")
    
dets(age=20, name="Rahul", batchcode="Python")
'''''
