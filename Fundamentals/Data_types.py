"""
    Data types in python 
    
    -> Every value has a datatypes, and variable can hold values.
       Python is a powerfully composed language; consequently,
       we don't have to charaterize the sort of varable while annoucing it.
       
    -> The interpreter binds the value implicitly to its type.
    
    like  a = 5 
"""

# Standard data types 
"""
    A variable can contain a variety of values. ON the other hand, a person's id must be 
    Stored as an integer, while their name must be stored as a string.
    
    The storage method for each of the standard data types that python provides is specified 
    by python is specified by python.
    
    -> Numbers
    -> Sequence Type
    -> Boolean 
    -> Set 
    -> Dictionary
"""

# 1. Text Type

# -> Str(String) stores text data. write in "String"
Name = "Shivam"
print(Name.upper()) # SHIVAM 
print(Name.lower()) # shivam
print(Name.split()) # ['Shivam']

# 2. Numeric Types 

# -> Int(integer) --> Whole numbers, positive or negative.

Age = 20 
print("Your Age: ", Age)

# -> Float(Floating-point) --> Decimal numbers.

Percentage = 93.9
print("Student percentage: ", Percentage)

# -> Complex(Complex numbers) --> Numbers with real and imaginary parts.

method = 5 + 4j

# 3. Sequence Types

# -> list -> Ordered, mutable collection.

fruits = ["apple" ,"banana", "cherry"]
fruits.append("mango")

print("List:", fruits)

# -> tuple = Ordered, immutable collection.

coordinates = (10, 20)
print("Tuple:", coordinates)

# -> range = Generates a sequence of numbers.

nums = range(1, 10)

print("Range Number:", nums)
