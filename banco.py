def show_balance(balance):

    print(f"Your current balance is: {balance:.2f}$")

def deposit():
    try:
        amount = float(input("Enter an amount to deposit: "))
        if amount < 0:
            print("The entered amount cannot be negative.")
            return 0
        return amount
    except ValueError:
        print("Please enter a valid number.")
        return 0

def withdraw(balance):
    try:
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds.")
            return 0
        elif amount < 0:
            print("The amount must be greater than or equal to 0.")
            return 0
        return amount
    except ValueError:
        print("Please enter a valid number.")
        return 0

def main_menu():
    balance = 0.0
    is_running = True

    while is_running:
        print("\nBANKING PROGRAM")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        option = input("Enter an option (1-4): ")

        if option == '1':
            show_balance(balance)
        elif option == '2':
            balance += deposit()
        elif option == '3':
            balance -= withdraw(balance)
        elif option == '4':
            is_running = False
            print("Have a great day!")
        else:
            print("Invalid option. Please choose an option between 1 and 4.")

if __name__ == "__main__":
    main_menu()

