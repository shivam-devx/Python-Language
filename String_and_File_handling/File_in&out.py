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

# Reading files := you can read entire file, one line, or all lines
# Example: 

f = open("sample.txt", "r")
print(f.read())   # read entire file

f.close()

f = open("sample.txt", "r")
print(f.readline())  # read one line
f.close()

f = open("samle.txt", "r")
for line in f:
    print(line.strip())   # read line by line

f.close()


# 