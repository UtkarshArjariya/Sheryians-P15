# Making a school admission system

class twelth:
    def __init__(self, percentage):
        if percentage > 50:
            self.percentage = percentage
            self.is_admission = True
        else:
            print("You are not eligible for the admission")
            self.is_admission = False
            
    @property        
    def admission(self):
        if self.is_admission == True:
            print("You are eligible for the admission")
        else:
            print("You are not eligible for the admission")
            
utkarsh = twelth(60)

# utkarsh.admission()  # This is used to call the function
# utkarsh.admission    # This is a property which is used to call the function without using the brackets



# Animal program building with magic method


class Animal:
    def __init__(self,name):
        self.name = name
        
    def __str__(self) -> str:    # This is a magic method which is used to print the object without calling the function directly instead just by calling the variable name
        return self.name    
    
        
animal1 = Animal("Dog")
animal2 = Animal("Lion")
animal3 = Animal("Tiger")

# print(animal1)

# Using __add__ magic method

class number:
    def __init__(self,num):
        self.num = num
        
    def __add__(self, num2):
        return self.num + num2.num
    
    def __eq__(self,Object):
        print(self.num == Object.num)
    
# n1 = number(int(input("Enter the number : ")))
# n2 = number(int(input("Enter the number : ")))

n1 = number(4)
n2 = number(5)

## Output of __add__ magic method
# print(n1 + n2) 
n1 + n2 # It can also be written like this

## Output of __eq__ magic method
# print(n1 == n2)
# n1 == n2
