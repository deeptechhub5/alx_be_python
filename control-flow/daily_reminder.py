def main():
    # Step 1: Prompt the user for inputs
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Step 2: Process based on priority using match-case
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
            if time_bound == "yes":
                reminder += " that requires immediate attention today!"
            else:
                reminder += " that should be addressed soon."
        
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
            if time_bound == "yes":
                reminder += " that needs to be completed today."
            else:
                reminder += " that should be done when possible this week."

        case "low":
            reminder = f"Reminder: '{task}' is a low priority task"
            if time_bound == "yes":
                reminder += " but still requires completion today."
            else:
                reminder += ". Consider completing it when you have free time."

        case _:
            reminder = "Invalid priority level entered. Please use high, medium, or low."

    # Step 3: Print customized reminder
    print("\n" + reminder)

if __name__ == "__main__":
    main()
