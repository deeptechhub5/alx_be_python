class BankAccount:
    def __init__(self, initial_balance=0):
        # store balance as float internally (but display without .0 when whole)
        try:
            self.account_balance = float(initial_balance)
        except Exception:
            self.account_balance = 0.0

    def deposit(self, amount):
        """Add amount to balance. (Doesn't return anything)"""
        self.account_balance += float(amount)

    def withdraw(self, amount):
        """Try to remove amount. Return True if successful, else False."""
        amt = float(amount)
        if amt <= self.account_balance:
            self.account_balance -= amt
            return True
        return False

    def display_balance(self):
        """Print balance in the exact expected format."""
        b = float(self.account_balance)
        if b.is_integer():
            b_str = str(int(b))
        else:
            b_str = ('{:.2f}'.format(b)).rstrip('0').rstrip('.')
        print(f"Current Balance: ${b_str}")
