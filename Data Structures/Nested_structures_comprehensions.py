# 1. Nested lists 
# Example:

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[0][2])
print(matrix)

# 2. Nested Dictionary 
# Example:

student = {
    
    "Shivam": {"age": 20, "course": "BCA"},
    "Flashy": {"age": 20, "course": "M-TECH" }
}

print(student["Shivam"])
print(student["Shivam"]["age"])

# 3. Both connect with each other 
# Example:

students = {
    
    "Shivam": {"id": 44, "course": "BCA", "marks": [90, 85, 87]},
    "Flashy": {"id": 34, "course": "BA", "marks": [92, 96, 95]}
}

print(students)
print(students["Shivam"])
print(students["Shivam"]["marks"])

# Comprehensions 
# Comprehensions are shortcuts for creating lists, sets, or dictionaries in one line

# 1 list comprehension

squares = [x*x for x in range(1, 6)]
print(squares)

# 2 set comprehension 

unique = { x%3 for x in range(10)}
print(unique)

# 3 Dictionary comprehension

marks = { name: len(name) for name in ["Shivam", "Flashy"]}
print(marks)

# NESTED COMPREHENSIONS
# You can even nest compreshensions for advanced use cases

# Examples:

# 1. Flatten a matrix

matrix =[[1, 2],[3, 4],[5, 6]]
flat = [num for row in matrix for num in row]
print(flat)

# 2. Multiplication table

table = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(table)

# 3. Nested Dictionary Comprehension

nested_dict = {i: {j: i*j for j in range(1, 4)} for i in range(1, 4)}
print(nested_dict)
# {1: {1: 1, 2: 2, 3: 3}, 2: {1: 2, 2: 4, 3: 6}, 3: {1: 3, 2: 6, 3: 9}}