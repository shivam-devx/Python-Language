# try block  -> contains code that might cause an error 
# Except block -> runs if an error occurs, preventing the program from crashing
# This is the most basic way to handle errors in python 

# Example:

try: 
    num = int(input("Enter a number: "))
    print("YOU ENTERED: ", num )
except ValueError:
    print("Error: Please enter a valid integer!")

# a main code block concept when it become fail and crash then they raise a error what you type 
#  in except code of block 

