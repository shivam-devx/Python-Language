# operator_precedence.py
# Demonstrating operator precedence in Python

a = 5
b = 2
c = 3

# Parentheses
print("Parentheses:", (a + b) * c)   # (5+2)*3 = 21

# Exponential
print("Exponential:", a ** b ** c)   # 5 ** (2 ** 3) = 5 ** 8 = 390625

# Unary operators
print("Unary minus:", -a)            # -5
print("Unary plus:", +a)             # 5
print("Bitwise NOT:", ~a)            # -6

# Multiplication, Division, Modulus, Floor Division
print("Multiplication:", a * b)      # 10
print("Division:", a / b)            # 2.5
print("Modulus:", a % b)             # 1
print("Floor Division:", a // b)     # 2

# Addition/Subtraction
print("Addition:", a + b)            # 7
print("Subtraction:", a - b)         # 3

# Shifts
print("Left Shift:", a << 1)         # 10 (binary shift)
print("Right Shift:", a >> 1)        # 2

# Bitwise AND, OR, XOR
print("Bitwise AND:", a & b)         # 0b101 & 0b010 = 0
print("Bitwise OR:", a | b)          # 0b101 | 0b010 = 7
print("Bitwise XOR:", a ^ b)         # 0b101 ^ 0b010 = 7

# Comparison
print("Comparison (a < b):", a < b)  # False
print("Comparison (a > b):", a > b)  # True

# Equality
print("Equality (a == b):", a == b)  # False
print("Not Equal (a != b):", a != b) # True

# Identity
print("Identity (a is b):", a is b)  # False
print("Identity (a is not b):", a is not b) # True

# Membership
nums = [1, 2, 3, 5]
print("Membership (a in nums):", a in nums)       # True
print("Membership (b not in nums):", b not in nums) # False

# Logical
print("Logical AND:", (a > b) and (c > b))  # True
print("Logical OR:", (a < b) or (c > b))    # True
print("Logical NOT:", not (a == b))         # True