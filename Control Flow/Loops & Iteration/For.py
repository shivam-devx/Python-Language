# Iterates over a sequence (list, tuple, string, range)
# runs for a fixed number of iterations or items
# commonly used with range(start, stop, step)
# stops automatically when sequence ends

# Example:

for i in range(1, 6):
    print("Iteration:", i)



fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruits:", fruit)
    

for char in "Python":
    print("Character:", char)
    
for i in range(2, 11, 2):
    print("Even number", i)
    
squares = [x*x for x in range(1, 6)]
print("Squares", squares)
