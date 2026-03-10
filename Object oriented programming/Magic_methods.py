#  Magic methods

""" 
    Magic methods are predefined in python, but you can override them in your class
    They allow objects to ineract with operators, functions, and built in behavior
    Example:
    
    -> __init__ = constructor runs when object is created
    -> __str__ = string representation print(object)
    -> __add__ = defines behavior of + operator
    -> __len__ =  defines behavior of length object(len(obj))
    -> __eq__ = defines behavior of ==

"""

# A Example of magic methods

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student: {self.name}, Marks: {self.marks}"
    
    # def __len__(self):
    #     return len(self.marks)
    
    def __add__(self, other):
        return self.marks + other.marks
    
    def __eq__(self, other):
        return self.marks == other.marks
    
s1 = student("shivam", 86)
s2 = student("Jatin", 86)

print(s1)

# print("Marks length:", len(s1)) # len 
print("Total marks:", s1 + s2) # operator 
print("Are marks are equal?", s1 == s2) # equal 

""" 
    OUTPUT:
    
    Student: shivam, Marks: 86
    Total marks: 172
    Are marks are equal? True
    
"""