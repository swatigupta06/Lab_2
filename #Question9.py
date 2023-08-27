#Question9
print("Welcome to the Bank RD Calculator")
principal = float(input("Enter your monthly installment amount (minimum 500): "))
duration = int(input("Enter the duration in months (minimum 6 months): "))
    
if principal < 500 and duration<6:
    print("Minimum monthly installment is 500. Please enter a valid amount.")
    print("Minimum RD duration is 6 months. Please enter a valid duration.")
else:
    interest_rate = 7.1 / 100
    total_amount = principal * duration + (duration * (duration + 1) / 2) * (interest_rate / 12)
    print("Total amount at maturity:",total_amount)