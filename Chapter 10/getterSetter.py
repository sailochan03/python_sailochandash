from decimal import Decimal as d

class Account:
    """Manage account-related data"""
    def __init__(self, n, b):
        self._name = n  # Internal storage for name
        self._balance = d(b)  # Internal storage for balance

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    # Getter for balance
    @property
    def balance(self):
        return self._balance

    # Setter for balance
    @balance.setter
    def balance(self, amount):
        if amount < d('0.00'):
            raise ValueError("Balance cannot be negative.")
        self._balance = d(amount)

    def deposit(self, amount):
        amount = d(amount)
        if amount <= d('0.00'):
            raise ValueError("Invalid deposit amount.")
        else:
            self.balance += amount  # Use the setter to update balance
            print(f"The amount in the account after deposit is: {self.balance}")

    def withdraw(self, amount):
        amount = d(amount)
        if amount <= d('0.00'):
            raise ValueError("Invalid withdrawal amount.")
        else:
            if amount > self.balance:
                raise ValueError("Insufficient balance.")
            else:
                self.balance -= amount  # Use the setter to update balance
                print(f"The amount in the account after withdrawal is: {self.balance}")


# Accepting input for account creation using setter methods
name_input = input("Enter the name: ")
balance_input = input("Enter the balance in the account: ")

# Create Account instance using setter methods for both name and balance
acc = Account(name_input, balance_input)

# Display account information using getter methods
print(f"Account holder's name is: {acc.name}")
print(f"Initial balance is: {acc.balance}")

# Deposit money
dep_input = input("Enter the deposit amount: ")
acc.deposit(dep_input)

# Withdraw money
wit_input = input("Enter the withdrawal amount: ")
acc.withdraw(wit_input)

# Final balance after transactions using getter method
print(f"Final balance is: {acc.balance}")
