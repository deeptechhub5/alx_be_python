import sys
from bank_account import BankAccount

def _fmt_amt(a):
    v = float(a)
    if v.is_integer():
        return str(int(v))
    return ('{:.2f}'.format(v)).rstrip('0').rstrip('.')

def parse_input(argv):
    if len(argv) < 2:
        return None, None
    raw = argv[1]
    if ':' in raw:
        cmd, amt = raw.split(':', 1)
        return cmd.lower(), amt if amt != '' else None
    # allow space separated: python main-0.py deposit 50
    cmd = raw.lower()
    amt = argv[2] if len(argv) > 2 else None
    return cmd, amt

def main():
    # This starting balance only affects command-line runs; default class init is 0.
    account = BankAccount(100)

    command, amount = parse_input(sys.argv)
    if command is None:
        print("Usage: python main-0.py <command>[:amount]")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${_fmt_amt(amount)}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${_fmt_amt(amount)}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
