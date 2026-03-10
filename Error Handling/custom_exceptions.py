"""  

- Python has built‑in exceptions (ValueError, ZeroDivisionError, etc.), but sometimes you need your own error type.
- You do this by creating a class that inherits from Exception.
- Then you can raise it when a specific condition occurs.
- Benefits:
- Makes your code more readable.
- Helps you handle domain‑specific errors (like “InsufficientBalanceError”).

"""

# Example: Custom Exception
 
# Define custom exception
class InsufficientBalanceError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw {amount}. Balance is only {balance}.")

# BankAccount class using custom exception
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            # Raise custom exception
            raise InsufficientBalanceError(self.balance, amount)
        self.balance -= amount
        return f"{amount} withdrawn. Remaining balance: {self.balance}"

# MAIN PROGRAM 
acc = BankAccount("Shivam", 500)

try:
    print(acc.withdraw(200))   # works fine
    print(acc.withdraw(400))   # raises custom exception
except InsufficientBalanceError as e:
    print("Error:", e)

#  Output
# 200 withdrawn. Remaining balance: 300
# Error: Cannot withdraw 400. Balance is only 300.

