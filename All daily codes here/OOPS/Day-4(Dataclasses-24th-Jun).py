# Data classes 

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    
    def __str__(self):
        return f'{self.name} is {self.age} years old'
        
# p = Person('John', 30)
# print(p)


from collections import namedtuple

Det = namedtuple("Details", ["name", "age"])
x = Det('John', 30)
# print(type(x))
# print(x)

