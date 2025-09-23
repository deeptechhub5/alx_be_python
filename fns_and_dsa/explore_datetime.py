from datetime import datetime, timedelta

def display_current_datetime():
    # Save the current date and time
    current_date = datetime.now()
    # Print in format YYYY-MM-DD HH:MM:SS
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date(days):
    # Get current date
    current_date = datetime.now()
    # Add days
    future_date = current_date + timedelta(days=days)
    # Print in format YYYY-MM-DD
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    # Part 1: Display current datetime
    display_current_datetime()

    # Part 2: Ask user for number of days
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_to_add)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
