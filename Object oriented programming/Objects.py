""" 
    An object is an instance of a class
    when you create and object, python call the class's __init__ constructer to intialize attributes
    each object has its own data, but shares the class's structure
    you can  create multiple objects from the same class
"""

# simple Example:

class bankaccount:
    def __init__(self, owner, balance=0):
        self.owner = owner  # that is attribute
        self.balance = balance 
        
    def deposit(self, amount):
        self.balance += amount
        return f"{amount} deposited. New balance: {self.balance}"
    
    def withdraw(self, amount):
        if amount<= self.balance:
            self.balance -= amount
            return f"{amount} withdrawn. Remaining balance: {self.balance}"
        else: 
            return "Insufficient funds!"
        
    def account_info(self):
        return f"Owner: {self.owner}, Balance: {self.balance}"
    
account_01 = bankaccount("Shivam", 10000)
account_02 = bankaccount("Shubham", 15000)

print(account_01.account_info())
print(account_01.deposit(5000))
print(account_01.withdraw(4500))

print(account_02.account_info())
print(account_02.deposit(5000))
print(account_02.withdraw(4500))

# summary:

# OUTPUT: 
""" 
    Owner: Shivam, Balance: 10000
    5000 deposited. New balance: 15000
    4500 withdrawn. Remaining balance: 10500
    Owner: Shubham, Balance: 15000
    5000 deposited. New balance: 20000
    4500 withdrawn. Remaining balance: 15500
"""

# show attributes (owner, balance)
# shows methods (deposit, withdraw, account_info)
# Demonstrates how different objects (account1 and account2) have their own data but share the same class structure
