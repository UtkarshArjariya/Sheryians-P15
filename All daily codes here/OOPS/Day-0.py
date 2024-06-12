# OOPS Day 0 notes(This is ahead part of OOPS)

   
# Q. Update this code and add more details
# 1. add "price" as a private object variable and user from outside must access with object method only
# 2. add "description" as a private object variable and user from outside must access with object method only
# 3. at last create a public object method which will show all the details of calling object
# for eg. -> p1.productdetails()
#  output ->
# Product Name: Iphone,
# Product Price: 123000,
# Product Description: color is ... abc ...

class Products:
    __count = 0

    def __init__(self,name,price,description):
        self.__name = name
        self.__price = price
        self.__description = description
        Products.__count += 1
    
    def __str__(self):
        return f"{self.productdetails()}"
        
    @classmethod
    def productcount(cls):
        return cls.__count
    
    def productname(self):
        return self.__name

    def productprice(self):
        return self.__price
    
    def productdescription(self):
        return self.__description

    def productdetails(self):
        return f"Product Name : {self.__name} \nProduct Price : {self.__price} \nProduct Description : {self.__description}"


class Refurbished(Products):
    __count = 0
    
    def __init__(self,product,discount):
        self.__product = product
        self.__discount = discount
        Refurbished.__count += 1
        
    def productdetails(self):
        return f"Product Name : {self.__product.productname()} \nProduct Price : {self.__product.productprice() - self.__discount} \nProduct Description : {self.__product.productdescription()} \nDiscount : {self.__discount}"
    
    def __str__(self):
        return f"{self.__product.productname()}"
    
    @classmethod
    def productcount(cls):
        return cls.__count
    
    @classmethod
    def productcount(cls):
        return cls.__count
    
p1 = Products("1) Iphone",150000,"black colour, 128 gb storage, A15 bionic Chip")
p2 = Products("2) Samsung S24", 125000,"leather background, 256 storage, SD 8 Gen 3 Processor")
p3 = Products("3) Boat Airpods",2700,"Noise cancellation, Boat Signature sound, Beast Mode, 120 hrs battery")

print("Total product =",Products.productcount())
print(p1.productdetails())
print(p2.productdetails())
print(p3.productdetails())

print("\nRefurbished Products:")
r1 = Refurbished(p1,5000)
r2 = Refurbished(p2,10000)
r3 = Refurbished(p3,200)

print(r1.productdetails())
print(r2.productdetails())
print(r3.productdetails())

print("Total refurbished products =",Refurbished.productcount())
    

# p1 = Products("1) Iphone",150000,"black colour, 128 gb storage, A15 bionic Chip")
# p2 = Products("2) Samsung S24", 125000,"leather background, 256 storage, SD 8 Gen 3 Processor")
# p3 = Products("3) Boat Airpods",2700,"Noise cancellation, Boat Signature sound, Beast Mode, 120 hrs battery")

# print("Total product =",Products.productcount())    
# print(p1.productdetails())
# print(p2.productdetails())
# print(p3.productdetails())


'''''
# Polymorphism Example:-

class Add:
    def __init__(self,n):
        self.__n = n 
    
    def __str__(self):
        return f"{self.__n}"
    
    def showN(self):
        return self.__n

    def __add__(self,other):
        return Add(self.__n + other.__n)
    
n1 = Add(12)
n2 = Add(10)
print(n1 +n2)
'''''