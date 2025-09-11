# Get user input for income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with a 5% simple interest rate
annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)
# A more concise way:
# annual_savings = (monthly_savings * 12) * 1.05

# Display the results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings}.")