import sys
from bank_account import BankAccount

def main():
    # Example starting balance (you can adjust for testing)
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>[:amount]")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Split the command and possible amount
    command_parts = sys.argv[1].split(":")
    command = command_parts[0]
    amount = float(command_parts[1]) if len(command_parts) > 1 else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
