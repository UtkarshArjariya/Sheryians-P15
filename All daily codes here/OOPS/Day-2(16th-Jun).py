# OOPS Day 2 notes - Polymorphism

class Animal:
    def __init__(self,name):
        self.name = name
    
    def show(self):
        print(self.name)
        
class Human:
    def __init__(self,name):
        self.name = name
        
    def show(self):
        print(self.name)
        
        
obj1 = Animal("Lion")
obj2 = Human("Utkarsh")

# obj1.show()
# obj2.show()


# Inheritance
# Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).

# Below is an exampple of "Single Level Inheritance"

class Reebook:
    def __init__(self,zips,pockets,material):
        self.zips = zips
        self.pockets = pockets
        self.material = material
        
    def show(self):
        print("Your bag has",self.zips, self.pockets, self.material)
        
        
class Hrx(Reebook):    # This is an example of inheritance
    def __init__(self,zips,pockets,material,laptop):
        super().__init__(zips,pockets,material)      # Super function is used to call the parent class constructor
        self.laptop = laptop
        
    def show(self):   # This is an example of method overriding, because the method is already present in the parent class but we are defining it again in the child class
        print("Your bag has",self.zips, self.pockets, self.material, self.laptop)
        
class Zara(Hrx):   # This is an example of Multilevel Inheritance, as Zara is inheriting from Hrx and Hrx is inheriting from Reebook
    def __init__(self, zips, pockets, material, laptop, wp):
        super().__init__(zips, pockets, material, laptop)
        self.wp = wp
        
    def show(self):
        print("Your bag has",self.zips, self.pockets, self.material, self.laptop, self.wp)

bag1 = Reebook(2,3,"Leather")
bag2 = Hrx(3,4,"Cloth","Yes")
bag3 = Zara(4,5,"Plastic","Yes","Yes")

# bag1.show()
# bag2.show()
# bag3.show()


# Abstraction
# Abstraction is the concept of hiding the complex implementation or hiding unecessary details from the user. 

# Below is an example of Abstraction

from abc import ABC, abstractmethod

class Area(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    
    
class square(Area):
    def __init__(self,side):
        self.side = side
        
    def show(self):
        print("Side of the square is",self.side)
        
    def area(self):
        pass
    
    def perimeter(self):
        pass

     
area1 = square(5)