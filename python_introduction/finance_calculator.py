# assign values
monthly_income = int(input("Enter your monthly income:"))


#Ask for their total monthly expenses
monthly_expenses = int(input("Enter your total monthly expenses:"))


# calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

#assign values 
interest_rate = 0.05
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * interest_rate)

#print the result
print(f"Your monthly savings are: ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
