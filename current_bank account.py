from bank_account import MainAccount

class CurrentAccount(MainAccount):
    def _init_(self, balance=0):
        super().__init__(balance)
    def deposit(self, amount):
        self.balance += amount
        print(f"deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        self.balance -= amount
        print(f"withdrew{amount}.new balance{self.balance}")
current = CurrentAccount(5000)
current.deposit(2000)
current.withdraw(3000)



