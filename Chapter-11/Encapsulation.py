class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    def deposite(self, amount):
        self._balance += amount

    def get_balance(self):   # Data is secure, and we use getter methods (get_balance()) to retrieve values.

        return self._balance
    
account = BankAccount(800)
account.deposite(300)
print(account.get_balance())
print(account.__balance)  # ❌ Error: Cannot access private variable

