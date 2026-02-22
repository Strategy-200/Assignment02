# Simple ATM Simulator
# Initial balance is ₹10,000 with minimum balance rule ₹500

balance = 10000   # Initial account balance
minimum_balance = 500

while True:
    print("\n=== ATM SIMULATOR ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    # Check Balance
    if choice == 1:
        print(f"Current Balance: ₹{balance:.2f}")

    # Deposit Money
    elif choice == 2:
        deposit_amount = float(input("Enter amount to deposit: "))
        
        if deposit_amount > 0:
            balance += deposit_amount
            print("Deposit successful!")
            print(f"Updated Balance: ₹{balance:.2f}")
        else:
            print("Invalid deposit amount")

    # Withdraw Money
    elif choice == 3:
        withdraw_amount = float(input("Enter amount to withdraw: "))

        # Check sufficient balance and minimum balance rule
        if withdraw_amount <= 0:
            print("Invalid withdrawal amount")

        elif withdraw_amount > balance:
            print("Insufficient balance!")

        elif balance - withdraw_amount < minimum_balance:
            print("Cannot withdraw! Minimum balance of ₹500 must remain.")

        else:
            balance -= withdraw_amount
            print("Withdrawal successful!")
            print(f"New Balance: ₹{balance:.2f}")

    # Exit
    elif choice == 4:
        print("Thank you for using ATM. Goodbye!")
        break

    else:
        print("Invalid choice! Please select from menu.")