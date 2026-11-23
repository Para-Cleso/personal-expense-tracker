"""expense_manager.py
Expense logic: validation, adding expenses, totals, and category summaries.
This module has no GUI code, so every function can be tested on its own.
"""

import math
from datetime import datetime

# Tuple: the predefined categories never change while the program runs.
CATEGORIES = (
    "Food",
    "Transportation",
    "Education",
    "Bills",
    "Entertainment",
    "Other"
)

DATE_FORMAT = "%Y-%m-%d"   # the date format used by the program: YYYY-MM-DD


def parse_amount(text):
    """Convert the amount typed by the user (text) into a float.

    Raises ValueError if it is not a number or is not greater than zero.
    """
    try:
        amount = float(text.strip())
    except ValueError:
        raise ValueError("Amount must be a number (example: 150 or 49.50).")

    if not math.isfinite(amount):           # rejects "nan" and "inf"
        raise ValueError("Amount must be a number (example: 150 or 49.50).")
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    return round(amount, 2)


def validate_date(date_text):
    """Check that date_text is a real date written as YYYY-MM-DD.

    Returns the cleaned date text. Raises ValueError otherwise.
    """
    date_text = date_text.strip()
    try:
        parsed = datetime.strptime(date_text, DATE_FORMAT)
    except ValueError:
        raise ValueError("Date must be a real date in YYYY-MM-DD format.")

    # strptime accepts "2026-1-5"; this check forces the full YYYY-MM-DD form.
    if parsed.strftime(DATE_FORMAT) != date_text:
        raise ValueError("Date must be a real date in YYYY-MM-DD format.")

    return date_text


def add_expense(expenses, amount, description, category, date):
    """Validate one expense and append it (as a dictionary) to the list.

    Raises ValueError if any field is invalid. The list is not changed
    when an error is raised.
    """
    if not isinstance(amount, (int, float)) or not math.isfinite(amount) or amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    if not description.strip():
        raise ValueError("Description cannot be blank.")

    if category not in CATEGORIES:
        raise ValueError("Please select a valid category.")

    date = validate_date(date)

    expense = {
        "amount": amount,
        "description": description.strip(),
        "category": category,
        "date": date
    }

    expenses.append(expense)


def view_expenses(expenses):
    """Return the records as a list of tuples for display in the history table.

    Each tuple is (date, description, category, amount), the same column
    order as the Transaction History table.
    """
    rows = []
    for expense in expenses:
        rows.append((
            expense["date"],
            expense["description"],
            expense["category"],
            expense["amount"]
        ))
    return rows


def calculate_total(expenses):
    """Return the sum of all expense amounts."""
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def summarize_by_category(expenses):
    """Return a dictionary of {category: total amount spent}."""
    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in summary:
            summary[category] = 0

        summary[category] += amount

    return summary
