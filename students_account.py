from bank_account import MainAccount

class StudentAccount(MainAccount):
    def _init_(self, balance=0):
        super()._init_(self)
    def withdraw(self, amount):
        if amount > 2000:
            print('withdrawal limit exceeded')
        else:
            self.balance -= amount
            print(f"withdrew{amount}.new balance{self.balance}")
    def deposit(self, amount):
        if amount > 50000:
            print('can not be deposited')
        else:
            self.balance += amount
            print(f"deposited {amount}. New balance: {self.balance}")

student_account = StudentAccount()
student_account.deposit(1003983)
student_account.withdraw(8099)