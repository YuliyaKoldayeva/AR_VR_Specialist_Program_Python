# Create class called BankAccount

class BankAccount:
    balance = 0

    # Constructor
    def __init__(self, input_balance):
        self.balance = input_balance


    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        return self.balance


    def withdraw(self, withdraw_amount):
        self.balance -= withdraw_amount
        return self.balance


b = BankAccount(10)
b.deposit(25)
b.withdraw(1)

print("The balance of the bank account is now " + str(b.balance))