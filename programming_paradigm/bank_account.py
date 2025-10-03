class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        self.account_balance += float(amount)

    def withdraw(self, amount):
        amt = float(amount)
        if amt <= self.account_balance:
            self.account_balance -= amt
            return True
        return False

    def display_balance(self):
        # Always 2 decimal places
        print(f"Current Balance: ${self.account_balance:.2f}")
