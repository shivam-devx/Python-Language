# Encapsulation means wrapping data and methods together inside a class
# it also allow data hiding: you can make attributes private so they can't be accessed directly
# instead, you use getter and setter methods to safely access or modify data 
# Benefits , 
        # protects data from accidental changes and gives control over how attributes are upadated
        # makes code more secure and professional

# Example:

class student: 
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    def get_name(self):
        return self.__name 
    
    def get_age(self):
        return self.__age 
    
    
    def  set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")
    
    def info(self):
        return f"Name: {self.__name}, Age: {self.__age}"
    
obj = student("Shivam", 20)

print(obj.info())
print("Name:", obj.get_name())
print("Age:", obj.get_age())

obj.set_age(-3)

# Summary:

# OUTPUT:
"""
    Name: Shivam, Age: 20
    Name: Shivam
    Age: 20
    Invalid age!
"""

