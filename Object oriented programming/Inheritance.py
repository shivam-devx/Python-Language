""" 
    Inheritance means one class(child) can reue code from another class (parent)
    It help with code reusability and makes projects more organized 
    types of inheritance in python:
    1. single inheritance -> one parent, one child 
    2. Multiple inheritance -> child inherits from multiple parents 
    3. Multilevel inheritance -> chain of inheritance(grandparent-> parent -> child)
    4. Hierarchical inheritance -> multiple children inhrit from one parent
"""

# Example:

# 1. single inheritance
# code(#):

# Parent class
import code


class person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age
    
    def introduce(self):
        return f"My name is {self.name}, I am {self.age} years old."

# child class

class student(person):
    def __init__(self, name, age, course):
        super().__init__(name, age) # call parent constructor
        self.course = course
        
        # Overriding method(poly)
        
        def introduce(self):
            return f"MY name is {self.name}, I am {self.age} years old and I study in {self.course}"
        

parentobj = person("Shubham", 28)
childobj = student("Shivam", 20, "BCA")

print(parentobj.introduce())
print(childobj.introduce())



# 2. Multiple inheritance := a child inherits from multiple rearent classes 
# Code(#):

class father:
    def skill(self):
        return "Driving"
    
class mother:
    def talent(self):
        return "cooking"
    
class child(father, mother):
    def hobby(self):
        return "gaming"

obj = child()
print("skill:", obj.skill())
print("Talent:", obj.talent())
print("HObby:", obj.hobby())


# 3. MUltilevel inheritance := a chain of inheritance(grandparent-> parent -> child )
# code(#):

class Grandparent:
    def property(self):
        return "Owns land"

class Parent(Grandparent):
    def job(self):
        return "Engineer"

class Child(Parent):
    def hobby(self):
        return "Football"

c = Child()
print(c.property())
print(c.job())
print(c.hobby())


# 4. HIerarchical inhritance:= multiple child classes inhrit from the same parent

# code(#):

class Animal:
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

d = Dog()
c = Cat()
print("Dog:", d.sound())
print("Cat:", c.sound())