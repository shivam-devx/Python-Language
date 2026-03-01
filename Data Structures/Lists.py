# LISTS := ordered, mutable(it can be changed), allow duplicates 
# defined with square brackets[]

# indexing starts at 0, supporting slicing, appending, removing, sorting 
# Example:

# 1

fruits = ["apple", "banana", "cherry"]
print(fruits[0])        # apple
print(fruits[-1])       # cherry

fruits.append("mango")
print(fruits)           # ['apple', 'banana', 'cherry', 'mango']

fruits.remove("banana")
print(fruits)           # ['apple', 'cherry', 'mango']

numbers = [10, 20, 30, 40]
print(numbers[1:3])     # [20, 30]

numbers.sort(reverse=True)
print(numbers)          # [40, 30, 20, 10]