class Account:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Cannot withdraw negative amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit negative amount")
        elif amount == 0:
            raise ValueError("Cannot deposit zero amount")
        self.balance += amount

    def transfer(self, amount, acc):
        if amount < 0:
            raise ValueError("Cannot transfer negative amount")
        if acc is None:
            raise NotExistingAccount("Account does not exist")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        acc.balance += amount

class NotExistingAccount(Exception):
    pass    