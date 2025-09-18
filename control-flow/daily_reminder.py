def main():
    # Step 1: Prompt the user for inputs
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Step 2: Process based on priority using match-case
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a High priority task"
            if time_bound == "yes":
                reminder += " that requires immediate attention today!"
            else:
                reminder += ". Try to address it soon."
        
        case "medium":
            reminder = f"Reminder: '{task}' is a Medium priority task."
            if time_bound == "yes":
                reminder += " It should be done today."
            else:
                reminder += " Complete it when possible this week."

        case "low":
            reminder = f"Note: '{task}' is a Low priority task."
            if time_bound == "yes":
                reminder += " Still, since it's time-bound, don’t forget to do it today!"
            else:
                reminder += " Consider completing it when you have free time."

        case _:
            reminder = "Invalid priority level entered. Please use high, medium, or low."

    # Step 3: Print customized reminder
    print("\n" + reminder)

if __name__ == "__main__":
    main()
