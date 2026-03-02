# FILE HANDLING

""" 
    File handling in python lets you open, read, write,append, and modify files
    before we perform any operation on a file, we need to open the file, this is done using the 
    open() function
    Example -> lets say we have a test file (sometext.txt) with some content in it, the open() function crates a file 
    object with a read() method for reading the content
    

 file = open("sometext.txt")
 print(file.read())
 
 there are various modes in which we can open files
 
 read(r): this mode opens the file for reding only and gives an error if the file does not exist.
 This is the default mode if no mode id passed as a parameter
 
 write(w): This mode opens the file for writing only and creates a new file if the file does not exist

append(a): This mode opens the file for appending only and crates a new file if the file does not exist

create(x): This mode creates a file and gives an error if the file already exists

text(t): used to handle text files

binary(b): used to handle binary files(images) 

"""


# WRITING FILES := writing replaces or appends content
# Example:

f = open("sample.txt", "w")
f.write("Hello, Shivam!")
f.close()

f = open("sample.txt", "a")
f.write("\nThis is appended text.")
f.close()

with open("sample.txt", "w") as f:
    f.write("Using with-statement for safe file handling.")
    
# Reading files := you can read entire file, one line, or all lines
# Example: 

f = open("sample.txt", "r")
print(f.read())   # read entire file

f.close()

f = open("sample.txt", "r")
print(f.readline())  # read one line
f.close()

f = open("sample.txt", "r")
for line in f:
    print(line.strip())   # read line by line

f.close()

# FILE OPERATIONS := you can check existence, delete, or manipulate files
# Example:
import os 
print(os.path.exists("sample.txt"))  # true and false
os.remove("sample.txt")     # delete file 

with open("data.txt", "w") as f:
    f.write("Line1\nLine2\nLine3")
    
with open("data.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    
# Perfect example of file handling 
# Step 1: creating a file is primarily done using the create(x)mode
file = open("Test.txt", "x")

# Step 2: write this method write content onto a file 
file = open("Text.txt", "w")
file.write("This is an example of file creation method to writing in file.")
file.close()
# overwrite in existing file 
file = open("Text.txt", "w")
file.write("This is overwrite text written in file")
file.close()

# Step 3: Read a file, this method allows us to read the contents of the file
file = open("Text2.txt", "r")
print(file.read())
file.close()

# Step 4: this method appends content into a file
file = open("nexText.txt", "a")
file.write("This is an example of file appending")
file.close()
