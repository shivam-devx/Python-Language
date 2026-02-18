# INPUT AND OUTPUT Program 

# Taking user input and printing output

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello,", name, "you are", age, "years old.")

# input() -> always returns a string 
# print() -> - displays output, supports formatting with commas, f-strings, or .format()
#  You can combine them for interactive programs

# Using f-strings for cleaner output

name = input("Enter your name: ")
marks = float(input("Enter your marks: "))

print(f"Student {name} scored {marks} marks.")

# Using .format() method

city = input("Enter your city: ")
print("You live in {}.".format(city))

