# TUPLES
# ordered, immutable(cannot be changed), allow duplicates
# definded with parentheses()
# faster than lists because they are immutable 
# useful for fixed collections of data

# Example:

coordinates = (10, 20)
print(coordinates[0])   # 10

numbers = (1, 2, 3, 4)
print(numbers[1:3])     # (2, 3)

nested = (("a", "b"), (1, 2))
print(nested[1])        # (1, 2)

single = (5,)
print(type(single))     # <class 'tuple'>

fruits = ("apple", "banana", "apple")
print(fruits.count("apple"))   # 2