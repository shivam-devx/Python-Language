# Runs until condition becomes False
# useful when number of iterations is not fixed
# often used with counters or user input

# Example:

count = 1
while count <= 5:
    print("Count:", count)
    count += 1
    
num = 10 

while num > 0:
    print("Number:", num)
    num -= 2

while True:
    name = input("Enter name (q to quit):")
    if name == "q":
        break
    print("Hello,", name)

i = 1
while i <= 10:
    if i % 2 == 0:
        print("Even:", i)
    i += 1
    
password = ""
while password != "1234":
    password = input("Enter password: ")
print("Access Granted")