# 1.Positional arguments := values are passed in the same order as parameters are defined and order matters a lot 
# some example:
# 1
def divide(a, b):
    print("Division:", a / b)

divide(4, 2)

# 2

def rectangle_area(length , width):
    print("Area of rectangle:", length * width)

rectangle_area(5,3)

# 3

def message(fname, lname):
    print("Hello,", fname, lname)
    
message("Shivam", "Dohare")

# 2. keyword argument:= argument are passed using parameter names and order doesn't matter

# 1

def student_data(name, age, course):
    print(f"{name} is {age} years old and percuing in {course}")

student_data("Shivam", 20, "BCA")

# 2
def power(base, exp):
    print(f"Power of {base} is", base ** exp)

power(2,5)

# 3
def book_details(title, author, year):
    print(f"{title} by {author}, published in {year}")

book_details(title="Python basics", author="John doe", year=2013)

# 3. default arguments:= parameter can have default values and if no value if passed default is used

# 1
def greetmassage(name="Shivam"):
    print("Hello,",name)
    
greetmassage()

# 2
def interest(principle, rate=5, time=2):
    print("simple interest:", (principle * rate * time) / 100)

interest(1000)
interest(1000, rate= 10, time= 5)

# 3
def profile(name, age= 20, city="Ahemdabad"):
    print(f"{name}, Age:{age}, City:{city}")

profile("Shivam")


# 4.variable length arguments := allow passing multiple values as a tuple and useful when number of arguments is not fixed

# 1
def add_allnumbers(*args):
    print("Sum:", sum(args))

add_allnumbers(1,2,3,4,5,6,6,7,8,8,9)

# 2
def multiply_all(*args):
    result = 1
    for n in args:
        result *= n
    print("Product:", result)

multiply_all(2, 3, 4, 5, 6)

# 3
def print_names(*args):
    for name in args:
        print("Name:", name)
print_names("Shivam", "flashy", "Ram")

# 5.Keyword variable length argument (like **)
# allows passing multiple keyword arguments as a dictionary and useful for flexible functions

# 1 

def show_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
show_details(name="shivam", age=20, course="BCA")

# 2

def config_settings(**kwargs):
    print("Configuration:")
    for k, v in kwargs.items():
        print(f"{k} = {v}")

config_settings(resolution="1080p", brightness=70, volume=50)

# 3
def order_summary(**kwargs):
    print("Order Summary:")
    for item, qty in kwargs.items():
        print(f"{item}: {qty}")

order_summary(apple=2, banana=5, mango=3)


# Now return statement in function how these work in function body 
# example:

def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname 

print(name("James", "Bachanan", "Barnes"))

