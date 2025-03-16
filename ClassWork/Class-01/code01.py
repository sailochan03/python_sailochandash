from decimal import Decimal as d
class Account:

    # Manage account related Data
    # object saved in heap memory
    # object's reference saved in stack memory
    # stack operates on LIFO principle

    def __init__(self, name, balance): 
        # used to initialize the attributes of class, basically like a constructor in java
        # "self" is the reference of object that is saved in the stack memory and is passed as first parameter 
        self._name = name
        self._balance = balance

    @property #decorator
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, amount):
        if amount < d('0.0'):
            raise ValueError("Balance must be non-negative!")
        self._balance = amount

    @property #decorator
    def name(self):
        return self._name
        
    def deposit(self, amount):
        if amount < d('0.0'):
            raise ValueError("Deposit amount must be positive!\n")
        else:
            self.balance += amount
            
    def withdraw(self, amount):
        if amount <= d('0.0'):
            raise ValueError("Withdraw amount must be positive!\n")
        elif amount > self.balance:
            raise ValueError("Insufficient balance.\n")
        else:
            self.balance -= amount
