class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance
    def deposit(self, amount):
        if amount > 0:
         self.__balance += amount
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    def show_balance(self):
       return self.__balance
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.show_balance())