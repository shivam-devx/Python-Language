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
print("List: ", fruits)

# -> tuple = Ordered, immutable collection.

coordinates = (10, 20)
print("Tuple: ", coordinates)

# -> range = Generates a sequence of numbers.

nums = range(1, 10)
print("Range Number: ", nums)

# 4. Mapping Type 

# -> Dict(Dictionary) -> key-value pairs.

student = {"name": "Shivam", "age": 20,"course": "BCA" }
print("Dictionary: ",student["name"]) # Shivam

# 5. Set Types 

# -> Set = Unordered, mutable collection of unique elenments.

numbers = {1, 3, 2, 4, 2, 4, 5}
print("Set: ",numbers)

# -> frozenset = immutable version of a set. 

frozen = frozenset([1, 2, 3])
print("Frozenset: ", frozen)

# 6. Boolean Type = (bool) represent truth values.

is_active = True
print("Boolean: ", is_active)

# 7. Binary Types 

# -> bytes = immutabel sequence of bytes.

data = "Hello bro"
print("bytes: ", data)

# -> bytefarray = Mutable sequence of bytes.

arr = bytearray([900, 880, 769])
print("Bytearray: ", bytearray)

# -> memoryview = provides a view of memory for binary data. 

mv = memoryview(b"google")
print("Memoryview: ", memoryview)

# 8.None Type = (None)Represents"no value" or null using in class check variable type

x = None
print("In Your mind have a skill: ", x)

#  This are all data types in python language in next topic cover all of this in advance 
#  with a him operation and its methods