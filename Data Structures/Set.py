# SETS
# unordered, mutable, no duplicates and defined with curly braces{}
# Elements are unique and useful for membership tests and removing duplicates 
# supports union intersection, difference

# Example:

fruits = {"apple", "banana", "cherry"}
print(fruits)   # order may vary

fruits.add("mango")
print(fruits)

fruits.remove("banana")
print(fruits)

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))        # {1, 2, 3, 4, 5}
print(a.intersection(b)) # {3}

numbers = [1, 2, 2, 3, 4, 4]
unique = set(numbers)
print(unique)            # {1, 2, 3, 4}