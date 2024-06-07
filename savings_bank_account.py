from bank_account import MainAccount


class SavingsAccount(MainAccount):
    def __init__(self, initial_amount):
        super().__init__(initial_amount)
        self.__interest_rate = 0.005
        self.withdrawal_limit = 700000

    def deposit(self, amount):
        interest = amount * self.__interest_rate
        self.balance += amount + interest
        print(f"deposited {amount}with {interest}interest. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            print("Withdrawal limit of exceeded")
        elif amount > self.balance:
            print("insufficient funds")
        else:
            self.balance -= amount
            print(f"withdrew{amount}.new balance{self.balance}")


savings_account = SavingsAccount(1000000)
savings_account.display_balance()

action = input("Welcome to Marvel's bank , would you like to 'withdraw' or 'deposit'?(type 'Exit' to quit): ")
if action == 'withdraw':
    amount = float(input('ënter the amount you wish to withdraw'))
    savings_account.withdraw(amount)
elif action == 'deposit':
    amount = float(input('ënter the amount you wish to deposit'))
    savings_account.deposit(amount)
elif action == 'Exit':
    print("Thank's for stopping by")
else:
    print("Invalid action, please try again")

savings_account.display_balance()
