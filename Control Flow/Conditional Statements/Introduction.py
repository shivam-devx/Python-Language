"""
    Control flow in python refers to the order in which instructions are executed in a 
    program. Normally, Python runs code sequentially, but control flow 
    Statements allow us to 
    --> make decisions 
    --> repeat tasks(loops)
    --> Handle errors or special cases 
    
This makes programs dynamic and responsive insted of just static lists of instructions.

"""
# Types of control flow in python 

# 1.Sequential flow
#  --> Default execution: one statement after another.
# example : print("Hello"), print("World")

# 2. Conditinal flow (Decision making)
# --> uses if, elif, and else to choose which block of code runs
#Example :
x = 10
if x > 0:
    print("Positive")
else:
    print("Non-positive")

# 3. Iterative flow(loops)
# --> repeats code multiple times using for or while 
# Example: 
for i in range(5):
    print(i)
    
# 4. Jump statements
# --> break = exit loop early 
# --> continue = skip cuttent iteration 
# --> pass = placeholder (does nothing, used to keep structure valid)

# 5. Exception Handling 
# --> try...except...finally = controls flow when errors occur
# Example: 

try:
    num = int("abc")
except ValueError:
    print("Error: not a number")
    
# 6. Pattern Matching(Python 3.10+)

# --> match...case allows structured decision making
# --> Example:
match command:
    case "start":
        print("starting...")
    case "stop":
        print("stopping...")
        
