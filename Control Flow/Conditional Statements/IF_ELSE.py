# if else allows you to handle two possiblities
# if condition is true, run one block 
# else run another block 

# Example:

# 1. Even or odd 

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
    
# 2. Pass or Fail

marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
else: 
    print("Fail")
    
# 3.Voting Eligibility

Age = int(input("Enter age: "))
if Age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# 4. Largest of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)
    
# 5. Positive or Negative

num1 = int(input("Enter a number: "))
if num1 >= 0:
    print("Positive or zero")
else:
    print("Negative")

