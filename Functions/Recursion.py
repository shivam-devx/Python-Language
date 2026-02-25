# We can let the function call itself, such a process is known as calling a function recursively in python

# Syntax:

""" 
    def function_name(parameters):
        if base_condition:
            return value  # stop recursion
        else:
            # recursive call with updated parameters
            
            return function_name(modified_parameters)
            
"""

# Example

# 1 factorial 
def factorial(n):
    if n == 0 or n == 1: 
        return 1
    
    return (n * factorial(n-1)) # recurcive call 

num = 5

print("number: ",num)
print("Factorial: ", factorial(num))

# 2 fibonacci number

def fibonacci(m):
    if m <= 1:
        return m
    
    return fibonacci(m-1) + fibonacci(m - 2)

print("Fibonacci(6):", fibonacci(6))

# 3 sum of n number

def sum_n(n):
    if n == 0:
        return 0
    
    return n + sum_n(n-1)
print("Sum of first 5 numbers:", sum_n(5))

# 4 Reverse string

def reverse_string(s):
    if len(s) == 0:   # base case
        return s
    return reverse_string(s[1:]) + s[0]

print("Reverse:", reverse_string("Shivam"))

# 5 countdown

def countdown(n):
    if n == 0:   # base case
        print("Blast Off!")
    else:
        print(n)
        countdown(n-1)

countdown(5)