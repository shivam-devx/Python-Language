# A class is like a blueprint for creating objects 
# it defines attributes(variable) and methods(functions)
# syntax os straighforward

"""
class Classname:
    # constructer 
    def __init__(self, attrributes ...):
        self.attribute = value 
        
        # method 
        def method_name(self):
            # code
"""

# simple Example:

class student:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
    def introduce(self):
        return f"MY name is {self.name}, I am {self.age} years old"
    
obj = student("shivam", 20)

print(obj.introduce())

# summary :

""" 
    There is class is student, and a constructor is __init__ that initializes attributes 
    object is obj its instance of the class, method (introduce) define its behavior
    Ouput: MY name is shivam, I am 20 years old
    
"""