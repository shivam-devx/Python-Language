# if elif else 

# used when you need to check multiple conditions 
# python checks conditions top to bottom, and executes the first one that is true
# if none match, else block runs

# Example:

# 1.Grading System

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
    
# 2. Temperature Check

temp = int(input("Enter temperature: "))

if temp >= 35:
    print("Hot day")
elif temp >= 20:
    print("Pleasant day")
elif temp >= 10:
    print("Cool day")
else:
    print("Cold day")

# 3. Largest of three Number

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest: ", a )
elif b >= a and b >= c:
    print("Largest: ", b)
else:
    print("Largest: ", c)
    
# 4. Age category

age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")

# 5. Day of Week

day = int(input("Enter dat number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid value entered !")

