"""main.py
Console menu for the Personal Expense Tracker.
Run with: python main.py
"""

import os
from datetime import date

from expense_manager import (
    CATEGORIES,
    add_expense,
    view_expenses,
    calculate_total,
    summarize_by_category,
    parse_amount,
)
from file_handler import load_expenses, save_expenses

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.json")


def load_saved_expenses():
    """Load records at startup and preserve damaged data when possible."""
    try:
        return load_expenses(DATA_FILE)
    except ValueError as error:
        backup = DATA_FILE + ".bak"
        try:
            os.replace(DATA_FILE, backup)
            print(f"Data file problem: {error}")
            print(f"Damaged file was preserved as {os.path.basename(backup)}.")
        except OSError:
            print(f"Data file problem: {error}")
            print("Could not create a backup of the damaged file.")
        print("Starting with an empty expense list.")
        return []
    except OSError as error:
        print(f"File error: Could not read the data file: {error}")
        return []


def prompt_amount():
    while True:
        try:
            return parse_amount(input("Amount: "))
        except ValueError as error:
            print(f"Invalid amount: {error}")


def prompt_category():
    print("\nCategories:")
    for index, category in enumerate(CATEGORIES, start=1):
        print(f"  {index}. {category}")
    while True:
        choice = input("Choose a category number: ").strip()
        try:
            index = int(choice)
            if 1 <= index <= len(CATEGORIES):
                return CATEGORIES[index - 1]
        except ValueError:
            pass
        print("Please enter a number from the list.")


def add_expense_menu(expenses):
    print("\n--- Add Expense ---")
    amount = prompt_amount()
    description = input("Description: ")
    category = prompt_category()
    transaction_date = input(f"Date (YYYY-MM-DD) [{date.today().isoformat()}]: ").strip()
    if not transaction_date:
        transaction_date = date.today().isoformat()

    try:
        add_expense(expenses, amount, description, category, transaction_date)
    except ValueError as error:
        print(f"Could not add expense: {error}")
        return

    try:
        save_expenses(expenses, DATA_FILE)
    except OSError as error:
        print(f"Expense added for this session, but could not be saved: {error}")
    else:
        print("Expense recorded and saved.")


def show_history(expenses):
    print("\n--- Transaction History ---")
    rows = view_expenses(expenses)
    if not rows:
        print("No expenses recorded yet.")
        return

    print(f"{'Date':<12} {'Description':<30} {'Category':<18} {'Amount':>12}")
    print("-" * 76)
    for row_date, description, category, amount in rows:
        print(f"{row_date:<12} {description[:30]:<30} {category:<18} {amount:>12,.2f}")


def show_summary(expenses):
    print("\n--- Expense Summary ---")
    print(f"Total Expenses: {calculate_total(expenses):,.2f}")
    summary = summarize_by_category(expenses)
    print("By category:")
    for category in CATEGORIES:
        print(f"  {category:<18} {summary.get(category, 0):,.2f}")


def main():
    expenses = load_saved_expenses()
    print("Personal Expense Tracker")
    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Add an expense")
        print("2. View transaction history")
        print("3. View expense summary")
        print("4. Save records")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_expense_menu(expenses)
        elif choice == "2":
            show_history(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            try:
                save_expenses(expenses, DATA_FILE)
            except OSError as error:
                print(f"Could not save records: {error}")
            else:
                print("Records saved.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
