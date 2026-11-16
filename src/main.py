from src.storage import add_expense, load_expenses
from src.analytics import generate_summary

def get_valid_amount() -> float:
    while True:
        raw_input = input("Enter amount (e.g. 150.50): ").strip()
        try:
            amount = float(raw_input)
            if amount <= 0:
                print("Amount must be greater than zero.")
                continue
            return amount
        except ValueError:
            print("Invalid number. Please enter digits only.")

def main():
    while True:
        print("\n=== Personal Expense Analyzer ===")
        print("1. Add new expense")
        print("2. View recent expenses")
        print("3. Generate summary & chart")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            category = input("Category (e.g. Food, Transport, Data): ").strip()
            if not category:
                print("Category cannot be empty.")
                continue
            amount = get_valid_amount()
            note = input("Optional note: ")
            add_expense(category, amount, note)
            print("Expense saved.")
            
        elif choice == "2":
            expenses = load_expenses()
            if not expenses:
                print("\nNo expenses found.")
            else:
                print("\n--- Recent Expenses ---")
                for row in expenses[-10:]:
                    print(f"{row['Date']} | {row['Category']:<12} | R{float(row['Amount']):,.2f} | {row['Note']}")
                    
        elif choice == "3":
            generate_summary()
            
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
