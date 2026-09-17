
class User:
    def __init__(self, username:str, password:str, bank_balance:float=0.0):
        self.username = username
        self.passowrd = password
        self.bank_balance = bank_balance

    def deposit(self, deposit_amt:float):
        self.bank_balance += deposit_amt

    def withdraw(self, withdrawl_amt:float):
        self.bank_balance -= withdrawl_amt
