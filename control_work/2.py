class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if self.__balance - amount > 0:
            self.__balance = self.__balance - amount

account = BankAccount(15000)
print(account.get_balance())
account.deposit(5000)
account.withdraw(10000)
print(account.get_balance())
# print(account.__balance) Выведет ошибку, т. к. __balance - приватный атрибут
print(account._BankAccount__balance)
