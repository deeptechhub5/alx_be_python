def main():
    while True:
        try:
            n = int(input("Enter the size of the pattern: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("That's not an integer. Try again.")

    row = 0
    while row < n:
        for _ in range(n):
            print("*", end="")
        print()  # newline after each row
        row += 1

if __name__ == "__main__":
    main()
