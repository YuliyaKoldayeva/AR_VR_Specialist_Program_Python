class BankAccount:
    balance = 0

    # Constructor
    def __init__(self, input_balance):
        self.__balance = input_balance


    def deposit(self, deposit_amount):
        self.__balance += deposit_amount



    def withdraw(self, withdraw_amount):
        self.__balance -= withdraw_amount

    # def __g


b = BankAccount(10)
b.deposit(25)
b.withdraw(1)

print("The balance of the bank account is now " + str(b.balance))