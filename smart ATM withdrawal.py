# 1. Set the initial bank balance
balance = 500.0

# 2. Ask the user for the withdrawal amount and convert it to a float
withdrawal_input = input("Enter the amount you want to withdraw (R): ")
request = float(withdrawal_input)

# 4. Check for invalid amounts (zero or negative)
if request <= 0:
    print("Invalid amount. You must withdraw more than R0.")

# 3. Check if there are enough funds for the withdrawal
elif request <= balance:
    balance -= request
    print(f"Withdrawal successful! Remaining balance: R{balance:.2f}")

# 5. Handle cases where the request exceeds the balance
else:
    print("Declined. Insufficient funds.")
