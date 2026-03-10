# Abstraction means hiding implementation details an showing only the essentials
# in python, abstraction is achieved using abstract classes and abstract methods (via the abc module)
# abstract classes cannot be instantiated directly they act as blueprints for other classes
# child classes must implement the abstract methods, ensuring consistency

# Example:

from abc import ABC, abstractmethod 

# abstract class 
class shape(ABC):
    @abstractmethod
    def area(self):
        pass 



# child class
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius 


# child class
class rectangle(shape):
    def __init__(self, length, width):
        self.length = length 
        self.width = width
        
    def area(self):
        return  self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
#  Main program 

c = circle(5)
r = rectangle(4, 6)

print("Circle area:", c.area())
print("Circle Perimeter:", c.perimeter())
print("Rectangle Area:", r.area())
print("Rectangle Perimeter:", r.perimeter())
    
""" 
    OUTPUT:
    
    Circle area: 78.5
    Circle Perimeter: 31.400000000000002
    Rectangle Area: 24
    Rectangle Perimeter: 20
    
    
"""