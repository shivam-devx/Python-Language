# skips current iteration and moves to next  and useful for ignoring certain cases
# loop does not stop , only skip one cycle

# Example:
# 1.

for i in range(1, 6):
    if i == 3:
        continue
    print("Value:", i)

# 2. 
for char in "Python":
    if char in "aeiou":
        continue
    print("Consonant:", char)

# 3.
numbers = [1, -2, 3, -4, 5]
for n in numbers:
    if n < 0:
        continue
    print("Positive number:", n)
