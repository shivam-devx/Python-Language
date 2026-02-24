# exits the loop immediatly when condition is met 
# useful for stopping search or terminating early
# control jumps outside the loop and often used with if insid eloops 

# Example:

# 1
for i in range(1,6):
    if i == 3:
        break
    print("Value:", i)

# 2
numbers = [10, 20, 30, 40, 50]
for n in numbers:
    if n == 30:
        print("Found 30, stopping loop")
        break
    print(n)

# 3 

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        print("Loop stopped")
        break
    print("You entered: ", num)