# 
# Restaurant Tip Calculator
# 

# Prompt the user for the total bill and desired tip percentage.
total           = float(input("Please, enter the total bill amount: $"))

# Calculate tip amount and total amount including tip.
tip_15          = total * 0.15
tip_20          = total * 0.20
total_with_15   = total + tip_15
total_with_20   = total + tip_20

# Output results using f-strings for formatting.
print(f"\nSuggested 15% tip: ${tip_15:.2f}")
print(f"Suggested 20% tip: ${tip_20:.2f}")

print(f"\nTotal with 15% tip: ${total_with_15:.2f}")
print(f"Total with 20% tip: ${total_with_20:.2f}")
