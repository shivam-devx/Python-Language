""" 
    Errors happern when code runs into unexpected situations like dividing by zero and wrong input and missing files
    Python provides try and except blocks to handle errors gracefully instead of crashing 
    
    try -> code that may cause error 
    except -> handles the error 
    else -> runs if no error occurs 
    finally -> always runs cleanup code 
    
    prevents program crashes 
    gives user-friendly error messages 
    makes code more reliable 

"""

# Example: 

try:
    num1 = int(input("Enter first number: "))
    num2 =- int(input("Enter second number: "))
    result = num1 / num2 
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid integers!")
else:
    print("Result: ", result)
finally: 
    print("Program finished.")
    
    