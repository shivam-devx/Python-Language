# Simple if 
# Theory : Runs a block only if condition is true 
# important info: condition must evaluate to true or false 

# Example:

num = 10 
if num > 5:
    print("Number is greater than 5")
    
# 1. check positive number
num2 = 20
if num > 0:
    print("Number is positive")

# 2. Check even number

num3 = 8
if num3 % 2 == 0:
    print("Number is even")

# 3. check string Length

name = "shivam"
if len(name) > 5:
    print("Name haas more than 5 characters")
    
# 4. Check membership in list 

fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list")
    
# 5. Check age eligibility 

age = 20 
if age >= 18:
    print("Eligible to vote")