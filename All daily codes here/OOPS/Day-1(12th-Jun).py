# OOPS Day 1 notes

# PPP(Procedural Programming Paradigm)
# In this, we write the code in a sequence of steps. It is a top-down approach. It increases the lines of code and decreases the reusability of the code.

# FPP(Functional Programming Paradigm)
# In this, we write the code in the form of functions. It is a bottom-up approach. It increases the reusability of the code and decreases the lines of code. It does not have security.

# OOPS(Object-Oriented Programming Paradigm)
# In this, we write the code in the form of classes and objects. It is a bottom-up approach. It increases the reusability of the code and decreases the lines of code. It encapsulates the data and functions. It has security.

#------------------------------------------------------------------------------------------------------------------------

# OOPS Concepts

# 1. Encapsulation
# It is the process of binding the data and functions together in a class. It is also known as data hiding. It is used to restrict the access to the data and functions. It is used to protect the data from the outside world.
# Ex - In this data leak is impossible, as it stops the extrernal access to the data and implements the security. User can only access the data through the functions. It uses class and objects.

# 2. Abstraction or Data Abstraction/Hiding
# It hides the complex implementation of the data and shows only the necessary details to the user. By only showing the necessary details, it increases the security of the data.

# 3. Polymorphism
# In this Poly means many and morphism means forms. It is the ability of a function to perform in different ways. 
# Ex - "+" operator is used for addition and concatenation. It is used to perform the same function in different ways.

# 4. Inheritance
# It is the process of acquiring the properties of one class by another class. It is used to implement the parent-child relationship.

# 5. Class & Object
# Class is a blueprint of an object. It is a user-defined data type. It is a collection of objects. It is a template of an object. It is a logical entity. It is a reference data type.
# Object is an instance of a class. It is a real entity. It is a physical entity. It is a memory entity. It is a value data type.


class Factory:
    a = 12 #(If this is defined inside of the class it is called as attribute)
    # __a = 12 #(If this is defined inside of the class it is called as private attribute)
    # _a = 12 #(If this is defined inside of the class it is called as protected attribute)
    # __ we can put this before function also like __hello() and it is called as private function

    def hello():
        print("Hello")

a = 23 #(If this is defined outside of the class it is called as variable)

def hello():   # This is a function in which a is a global variable which can be accessed from anywhere
    global a
    print(a)
    
# hello()

# print(Factory.a) # This is a class attribute which can be accessed by the class name


# Let's make an object
# Object are only made when you call the class, it can access all items of a class which makes it a child in a way

obj = Factory()

# print(obj.a)

# Constructor

class Factory:
    def __init__(self,BT,T,ET):  # This is a constructor, in this "self" is a reference to the object or the class itself
        self.BodyType = BT
        self.Tyres = T
        self.EngineType = ET
        
    
Ferarri = Factory("Covered",4,"8-Cycle")
Lord_Alto = Factory("Covered",4,"4-Cycle")
# Sigma_Splender = Factory("Open",2,"6-Cycle")

print(Ferarri.BodyType,Ferarri.Tyres,Ferarri.EngineType)