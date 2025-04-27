import csv
from datetime import datetime

def main():
    """Main function to run the finance tracker"""
    print("Welcome to Personal Finance Tracker")
    transactions = load_transactions("transactions.csv")

    while True:
        print("\nMenu:")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Balance")
        print("4. View Spending by Category")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_transactions(transactions)
        elif choice == "3":
            view_balance(transactions)
        elif choice == "4":
            view_spending_by_category(transactions)
        elif choice == "5":
            save_transactions(transactions, "transactions.csv")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def load_transactions(filename):
    """Load transactions from CSV file"""
    transactions = []
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append({
                    "date": row["date"],
                    "amount": float(row["amount"]),
                    "category": row["category"],
                    "description": row["description"]
                })
    except FileNotFoundError:
        pass  # Return empty list if file doesn't exist yet
    return transactions

def add_transaction(transactions):
    """Add a new transaction"""
    date = input("Enter date (YYYY-MM-DD) [today]: ") or datetime.now().strftime("%Y-%m-%d")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    transactions.append({
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    })
    print("Transaction added successfully!")

def view_transactions(transactions):
    """Display all transactions"""
    if not transactions:
        print("No transactions found.")
        return

    print("\nAll Transactions:")
    print("-" * 60)
    print(f"{'Date':<12} {'Amount':<10} {'Category':<15} {'Description':<20}")
    print("-" * 60)

    for t in transactions:
        print(f"{t['date']:<12} ${t['amount']:<9.2f} {t['category']:<15} {t['description']:<20}")

def view_balance(transactions):
    """Calculate and display current balance"""
    income = sum(t["amount"] for t in transactions if t["amount"] > 0)
    expenses = sum(t["amount"] for t in transactions if t["amount"] < 0)
    balance = income + expenses

    print("\nFinancial Summary:")
    print(f"Income: ${income:.2f}")
    print(f"Expenses: ${abs(expenses):.2f}")
    print(f"Current Balance: ${balance:.2f}")

def view_spending_by_category(transactions):
    """Show spending breakdown by category"""
    if not transactions:
        print("No transactions found.")
        return

    categories = {}
    for t in transactions:
        if t["amount"] < 0:  # Only count expenses
            categories[t["category"]] = categories.get(t["category"], 0) + abs(t["amount"])

    if not categories:
        print("No expense transactions found.")
        return

    print("\nSpending by Category:")
    for category, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"{category}: ${amount:.2f}")

def save_transactions(transactions, filename):
    """Save transactions to CSV file"""
    with open(filename, "w", newline="") as file:
        fieldnames = ["date", "amount", "category", "description"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)

if __name__ == "__main__":
    main()
