# Type casting is method to convert data types from existing variable

# There are two type of casting 

# Explicit Casting: int(), float(), str(), bool()
# Implicit Casting: Python automatically converts types in some operations (e.g., int + float → float)
# Always validate input before casting to avoid errors.

# Program to converting string to int and float

num_str = "100"     
num_int = int(num_str)     # string → int

num_float = float(num_str) # string → float

print("Integer:", num_int + 39)
print("Float:", num_float + 89.74)

# Taking numeric input safely

num1 = int(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum =", num1 + num2)

# Boolean casting

print(bool(0))     # False
print(bool(1))     # True
print(bool(""))    # False (empty string)
print(bool("Hi"))  # True (non-empty string)

# Implicit casting 
# convert small data type into large data type there has no lost data 

# Explicit casting 
# convert large data type into small data type there has lost data because a variable have
#  3.14 value then convert into int so 0.14 lost this data 