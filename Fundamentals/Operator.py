# Operators In Python 

# --> Python has different types of operators for different operations. They are as follows
print("========= Arithmetic operators =========\n")

# Arithmetic operators are used to perform arithmetic/mathematical operations

a, b = 10, 3
print("Addition:", a + b)         # Add two numbers
print("Substraction:", a - b)     # Minus two numbers
print("Multiplication:", a * b)   # Multiply two numbers
print("Division:", a / b)         # Divide two numbers(floating result in decimal)
print("Floor Division:", a // b)  # Give a integer result by division 
print("Modulus:", a % b)          # Remainider in numbers by division
print("Exponent:", a ** b)        # Give a power of first number and power is second number

# Assignment operators 
# --> These operators are used to assign values to variables.

print("\n======== Assignment Operators =========\n")

# Basic assignment
a = 10
print("= :", a)   # 10

# Add and assign
a = 10
a += 5   # a = a + 5
print("+= :", a)  # 15

# Subtract and assign
a = 10
a -= 3   # a = a - 3
print("-= :", a)  # 7

# Multiply and assign
a = 10
a *= 2   # a = a * 2
print("*= :", a)  # 20

# Exponent and assign
a = 2
a **= 3  # a = a ** 3
print("**= :", a) # 8

# Divide and assign
a = 10
a /= 4   # a = a / 4
print("/= :", a)  # 2.5

# Floor divide and assign
a = 10
a //= 3  # a = a // 3
print("//= :", a) # 3

# Modulus and assign
a = 10
a %= 3   # a = a % 3
print("%= :", a)  # 1

# Bitwise AND and assign
a = 5    # binary: 0101
a &= 3   # a = a & 3 (0011)
print("&= :", a)  # 1

# Bitwise OR and assign
a = 5
a |= 3   # a = a | 3
print("|= :", a)  # 7

# Bitwise XOR and assign
a = 5
a ^= 3   # a = a ^ 3
print("^= :", a)  # 6

# Right shift and assign
a = 8    # binary: 1000
a >>= 2  # a = a >> 2
print(">>= :", a) # 2 (0010)

# Left shift and assign
a = 3    # binary: 0011
a <<= 2  # a = a << 2
print("<<= :", a) # 12 (1100)

print("\n======== Bitwise operators ========\n")
# --> Bitwise operators are used to deal with binary operations
# Demonstrating all bitwise operators in one program

a = 5   # binary: 0101
b = 3   # binary: 0011

print("a =", a, "binary:", bin(a))
print("b =", b, "binary:", bin(b))

# Bitwise AND
print("a & b =", a & b, "binary:", bin(a & b))

# Bitwise OR
print("a | b =", a | b, "binary:", bin(a | b))

# Bitwise NOT
print("~a =", ~a, "binary:", bin(~a))

# Bitwise XOR
print("a ^ b =", a ^ b, "binary:", bin(a ^ b))

# Right Shift
print("a >> 1 =", a >> 1, "binary:", bin(a >> 1))
print("a >> 2 =", a >> 2, "binary:", bin(a >> 2))

# Left Shift
print("a << 1 =", a << 1, "binary:", bin(a << 1))
print("a << 2 =", a << 2, "binary:", bin(a << 2))

print("\n========= Comparison operators =========\n")
# --> These operators are used to compare values.

# Demonstrating all comparison operators in Python

a = 10
b = 20

print("a =", a)
print("b =", b)

# Equal
print("a == b:", a == b)   # False

# Not Equal
print("a != b:", a != b)   # True

# Less Than
print("a < b:", a < b)     # True

# Greater Than
print("a > b:", a > b)     # False

# Less Than or Equal To
print("a <= b:", a <= b)   # True

# Greater Than or Equal To
print("a >= b:", a >= b)   # False

print("\n======== Identity & Membership Operators =========\n")
# -> Identity: is, is not → check if two objects point to same memory
# -> Membership: in, not in → check if value exists in sequence

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("x is y:", x is y)       # False (different objects)
print("x is z:", x is z)       # True (same object)
print("2 in x:", 2 in x)       # True
print("5 not in x:", 5 not in x) # True

print("\n======== Logical operator =========\n")
# -> and → True if both are true
# -> or → True if at least one is true
# -> not → Negates the condition

# logical.py
a, b = True, False

print("a and b:", a and b)  # False
print("a or b:", a or b)    # True
print("not a:", not a)      # False