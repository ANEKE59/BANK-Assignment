from bank_account import MainAccount


class ChildrensAccount(MainAccount):
    def _init_(self, balance=0):
        super().__init__(self)
        self.__interest_rate = 0.007

    def deposit(self, amount):
        interest = amount * self.__interest_rate
        self.balance += amount + interest
        print(f"deposited {amount}with {interest}interest. New balance: {self.balance}")

    def withdraw(self, amount):
        print("Withdrawals not allowed for Children's account")


children = ChildrensAccount(500)
children.deposit(1000)
children.withdraw(100)
