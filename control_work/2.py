class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance = self._balance + amount
    
    def withdraw(self, amount):
        if self._balance - amount > 0:
            self._balance = self._balance - amount

account = BankAccount(15000)
print(account.get_balance())
account.deposit(5000)
account.withdraw(10000)
print(account.get_balance())