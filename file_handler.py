"""file_handler.py
Saving and loading expense records using a local JSON file.
"""

import json


def save_expenses(expenses, filename="expenses.json"):
    """Write the list of expense dictionaries to a JSON file.

    Mode "w" creates the file if needed and replaces old contents.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


def load_expenses(filename="expenses.json"):
    """Read expense records from a JSON file and return them as a list.

    - Missing file       -> returns an empty list (first run of the program).
    - Damaged/invalid file -> raises ValueError with a clear message, so
      corrupted data is never treated as valid records.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            records = json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        raise ValueError("The data file is not valid JSON (it may be damaged).")

    if not isinstance(records, list):
        raise ValueError("Expense data must be a list.")

    # Every record must be a dictionary that has the four expected keys.
    required_keys = ("amount", "description", "category", "date")
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("Each expense record must be a dictionary.")
        for key in required_keys:
            if key not in record:
                raise ValueError("An expense record is missing the '" + key + "' field.")
        if not isinstance(record["amount"], (int, float)):
            raise ValueError("An expense record has a non-numeric amount.")

    return records
