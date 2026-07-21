# We want to simulate a smart ATM Withdrawal

# Setting the bank balance
bank_balance = 700

# Asking the user to withdraw
withdraw = float(input("How much do you want to withdraw : R"))

# Check the request and respond accordingly
if withdraw <= 0:
    print("Invalid amount. You must withdraw more than R0")

elif withdraw <= bank_balance:
    remaining_balance = bank_balance - withdraw
    print(f"Withdrawal successful! Remaining balance: R{remaining_balance}")

else:
    print("Declined. Insufficient funds.")
