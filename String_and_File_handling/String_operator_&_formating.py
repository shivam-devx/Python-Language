# Strings 
""" 
    in python, anything enclosed within single or double quotion marks in considered a 
    string. A string is essentially a sequence of characters 
    strings are used when working with unicode characters 
    They are immutable(cannot be changed directly)
    

"""

# Example:
# You can access, slice, and iterate over them

text = "Hello world"
print(text[0])
for ch in text:
    print(ch)
    
print(text[0:6])

# length of a string
# we can find the length of a string using the len() function
# Example:
fruit = "Mango"
lis = len(fruit)
print("Mango is a", lis, "letter word.")

# String as an array
""" 
    a string is essentially a sequence of characters and can be accessed like an 
    array, although it is not technically one. thus, we can access the element of this array
    
"""
# Example:
pie = "Applepie"
print(pie[:4])  # slicing from 
# start 
print(pie[4:])   # slicing till 
# end
print(pie[2:6])   #slicing in 
# between
print(pie[-8:-3])   # slicing using negative index

# Loop through a string 
""" 
     string are arrays, and arrays are iterable, thus, we can loop through strings
     
""" 
# Example:
aplabets ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in aplabets:
    print(i)
    
# STRING METHODS

""" 
    python provides a set of built in methods that we can use to modify and maniputlate strings
    
"""

# UPPERCASE: The upper() method converts a string to upper case

# Example:

str1 = "abcdefghijKLMNOpqrstuvwxyz"
print(str1.upper())

# LOWERCASE : The lower() method converts a string to lower case

# Example:
print(str1.lower())

# Capitalize example: first letter uppercase, rest lowercase
print(text.capitalize()) # Hello world
# swapcase ex: swaping on between each other upper to lower and lower to upper
print(text.swapcase())  # HELLO WORLD → hello world
# Title ex: first letter of each word uppercase
print(text.title())

# Seaching & checking := used to find substrings or check sonditions 

# startswith -> checks if string start with substring 
# endswith -> checks if string end with substring 
# find -> returns index of substring 
# index -> like find, but error if not found 
# count -> counts occurrences of substring 

# Now Example:

tex = "Python Programming"
print(tex.startswith("Py")) # true

print(tex.endswith("ing"))

print(tex.find("gram"))

print(tex.index("Pro"))

print(tex.count("m"))

# Validation methods: used to check the type of characters in a string 

# isalnum -> only letters and numbers
# isalpha -> only letters
# isdigit -> only digits
# isspace -> only whitespace
# islower -> all lowercase
# isupper -> all uppercase

# Example:

print("Python3".isalnum())  # TRUE

print("Python".isalpha())   # TRUE

print("12345".isdigit())    # TRUE

print("    ".isspace())     # TRUE

print("hello".islower())    # TRUE

print("HELLO".isupper())    # TRUE


# MODIFICATION METHODS : used to modify or clean strings

# replace -> replace substring 
# strip -> remove spaces or charaters from both ends
# lstrip -> remove from left side 
# rstrip -> remove from right side

# Example:

test = "     hello world     "
print(text.strip())  # "hello world"
print(text.lstrip())  # "hello world     "
print(text.rstrip())   # "   hello world"
print("Python is fun programming language".replace("fun", "Higher level")) 

# SPLITTING & JOINING := used to break or combine strings 

# split -> split into list
# splitliness -> split by line breaks 
# join -> join list into string 

# Example:

words = "apple,banana,cherry,mango"
print(words.split(","))

line = "Line1\nLine2\nLine3"
print(line.splitlines())

items = ["Python book", "Java book", "C book"]
print(" - ".join(items))

# STRING FORMATTING := used to insert variable into strings

# f-strings -> modern, readable
# foramat -> flexible
# % formatting ->  older style

# Example:

name = "Shivam"
age = 20 
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name,age))

pi = 3.145577
print("Pi value: %.2f" % pi)


# OTHER USEFUL METHODS:= utility methods for alignment and padding

# center(width,char) -> center string
# zfill(width) -> pad with zeros
# rjust(width, char) -> right align

# Example:

book = "Python"
print(book.center(20, "*"))
print(book.zfill(10))
print("123".rjust(5, "0"))

