from bank_account import MainAccount


class SavingsAccount(MainAccount):
    def __init__(self, initial_amount):
        super().__init__(initial_amount)
        self.__interest_rate = 0.005
        self.withdrawal_limit = 700000
