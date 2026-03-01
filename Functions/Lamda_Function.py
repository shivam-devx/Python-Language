# A lambda function is a small anonymous function defined using the lambda keyword

# Syntax:

# lambda argruments: expression

# it can take any number of arguments but only one expression 
# the result of that expression is automatically returned
# using for quick,one time use functions and cleaner code for simple operations
# often used with map(), filter(), reduce() and sorting 

# Example:
# 1.Square of a Number
square = lambda x: x * x
print(square(5))   # Output: 25

# 2.Add Two Numbers
add = lambda a, b: a + b
print(add(10, 20))

# 3.Check Even Number
is_even = lambda x: x % 2 == 0 
print(is_even(6))

print(is_even(7))

# 4.Reverse a String
reverse = lambda s: s[::-1]
print(reverse("Shivam"))   # Output: mavihS

# 5.Find Maximum of Two Numbers
maximum = lambda a, b: a if a > b else b
print(maximum(15, 25))   # Output: 25

# 6.Use with map()
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x*x, numbers))
print(squares)   # Output: [1, 4, 9, 16, 25]

# 7.Use with filter()
numbers = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # Output: [10, 20, 30]

# 8.Use with sorted()
students = [("Shivam", 20), ("Flashhy", 18), ("Builder", 22)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
# Output: [('Flashhy', 18), ('Shivam', 20), ('Buider', 22)]
