# Student Expense Tracker
# Academic Project
# Language: Python

# Empty list to store expenses
expenses = []

while True:
    print("\n--- Student Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Add expense
    if choice == "1":
        date = input("Enter date (DD-MM-YYYY): ")
        category = input("Enter category (Food/Travel/Books/etc): ")
        amount = float(input("Enter amount: "))

        expenses.append({
            "date": date,
            "category": category,
            "amount": amount
        })

        print("Expense added successfully!")

    # View all expenses
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("\nDate\t\tCategory\tAmount")
            print("--------------------------------------")
            for exp in expenses:
                print(f"{exp['date']}\t{exp['category']}\t\t₹{exp['amount']}")

    # View total expense
    elif choice == "3":
        total = 0
        for exp in expenses:
            total += exp["amount"]
        print(f"Total Expense: ₹{total}")

    # Exit program
    elif choice == "4":
        print("Thank you for using Student Expense Tracker!")
        break

    # Wrong input
    else:
        print("Invalid choice. Please select 1 to 4.")
