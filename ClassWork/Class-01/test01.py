from decimal import Decimal as d
from code01 import Account
# Define a function to create and manage accounts
def manage_accounts():
    # Create instances of the Account class
    acc01 = Account('SMiX', d('1000.0'))
    acc02 = Account('Guddu', d('1000.0'))

    # Print account names
    print(acc01.name)
    print(acc02.name)

    # Perform transactions
    acc01.deposit(500)
    acc02.withdraw(500)

    # Print updated balances
    print(acc01.balance)
    print(acc02.balance)

# Call the function to manage accounts
manage_accounts()
