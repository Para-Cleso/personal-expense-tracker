"""test_expense_manager.py
Automated tests for expense_manager.py and file_handler.py.
Run with:  python -m unittest test_expense_manager -v
"""

import os
import tempfile
import unittest

from expense_manager import (
    add_expense,
    calculate_total,
    summarize_by_category,
    view_expenses,
    parse_amount,
    validate_date,
)
from file_handler import save_expenses, load_expenses


class TestExpenseManager(unittest.TestCase):

    def test_T01_add_valid_expense(self):
        """T01 (normal): a valid expense is added to the list."""
        expenses = []
        add_expense(expenses, 150, "School supplies", "Education", "2026-11-13")
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0]["amount"], 150)
        self.assertEqual(expenses[0]["category"], "Education")

    def test_T02_calculate_total(self):
        """T02 (normal): total of 150 and 50 is 200."""
        expenses = []
        add_expense(expenses, 150, "Books", "Education", "2026-11-13")
        add_expense(expenses, 50, "Snacks", "Food", "2026-11-14")
        self.assertEqual(calculate_total(expenses), 200)

    def test_T03_negative_amount_rejected(self):
        """T03 (invalid): a negative amount is rejected and nothing is added."""
        expenses = []
        with self.assertRaises(ValueError):
            add_expense(expenses, -100, "Refund?", "Other", "2026-11-13")
        self.assertEqual(expenses, [])

    def test_T04_non_numeric_amount(self):
        """T04 (invalid): 'abc' raises ValueError instead of crashing the program."""
        with self.assertRaises(ValueError):
            parse_amount("abc")

    def test_T05_load_missing_file(self):
        """T05 (failure): loading a file that does not exist gives an empty list."""
        missing = os.path.join(tempfile.gettempdir(), "no_such_expenses_file.json")
        if os.path.exists(missing):
            os.remove(missing)
        self.assertEqual(load_expenses(missing), [])

    def test_T06_summarize_by_category(self):
        """T06 (normal): Food 100+50 = 150, Education 200."""
        expenses = []
        add_expense(expenses, 100, "Lunch", "Food", "2026-11-10")
        add_expense(expenses, 50, "Dinner", "Food", "2026-11-11")
        add_expense(expenses, 200, "Tuition fee", "Education", "2026-11-12")
        summary = summarize_by_category(expenses)
        self.assertEqual(summary["Food"], 150)
        self.assertEqual(summary["Education"], 200)

    def test_T07_boundary_amount(self):
        """T07 (boundary): 0.01 is accepted, 0 is rejected."""
        self.assertEqual(parse_amount("0.01"), 0.01)
        with self.assertRaises(ValueError):
            parse_amount("0")

    def test_T08_blank_description(self):
        """T08 (invalid): a blank description is rejected."""
        expenses = []
        with self.assertRaises(ValueError):
            add_expense(expenses, 20, "   ", "Food", "2026-11-13")
        self.assertEqual(expenses, [])

    def test_T09_invalid_date(self):
        """T09 (invalid/boundary): impossible and badly formatted dates are rejected."""
        with self.assertRaises(ValueError):
            validate_date("2026-02-30")      # February 30 does not exist
        with self.assertRaises(ValueError):
            validate_date("13/11/2026")      # wrong format
        self.assertEqual(validate_date("2026-02-28"), "2026-02-28")

    def test_T10_invalid_category(self):
        """T10 (invalid): a category outside the CATEGORIES tuple is rejected."""
        expenses = []
        with self.assertRaises(ValueError):
            add_expense(expenses, 20, "Gym", "Fitness", "2026-11-13")
        self.assertEqual(expenses, [])

    def test_T11_save_and_load_round_trip(self):
        """T11 (normal): saved records are the same after loading them again."""
        expenses = []
        add_expense(expenses, 150, "School supplies", "Education", "2026-11-13")
        add_expense(expenses, 75.5, "Jeepney fare", "Transportation", "2026-11-14")
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "expenses.json")
            save_expenses(expenses, path)
            loaded = load_expenses(path)
        self.assertEqual(loaded, expenses)

    def test_T12_damaged_file(self):
        """T12 (failure): a file with invalid JSON raises ValueError, not wrong data."""
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "expenses.json")
            with open(path, "w", encoding="utf-8") as file:
                file.write("{ this is not valid json")
            with self.assertRaises(ValueError):
                load_expenses(path)

    def test_T13_empty_list_totals(self):
        """T13 (boundary): no expenses gives total 0 and an empty summary."""
        self.assertEqual(calculate_total([]), 0)
        self.assertEqual(summarize_by_category([]), {})

    def test_T14_view_expenses_rows(self):
        """T14 (normal): history rows are tuples in (date, description, category, amount) order."""
        expenses = []
        add_expense(expenses, 150, "School supplies", "Education", "2026-11-13")
        self.assertEqual(view_expenses(expenses),
                         [("2026-11-13", "School supplies", "Education", 150)])


if __name__ == "__main__":
    unittest.main()
