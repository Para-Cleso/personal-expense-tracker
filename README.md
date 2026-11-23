# Personal Expense Tracker
## CS 26 – Exam 2: Python Program Technical Documentation

**Program type:** Console-based Python application
**Course coverage:** Weeks 4–5 Python concepts  
**Documentation status:** Proposed design and implementation guide; update implementation and testing details after running the program.

---

## A. Program Title and Overview

The **Personal Expense Tracker** is a console-based Python application designed to help individuals monitor and organize their daily expenses. Using a simple text-based menu, users can record expenses by entering their amount, description, category, and transaction date. The application also allows users to view their transaction history, calculate total expenses, and review spending summaries grouped by category.

The application is intended for individuals who want a simple way to keep track of where their money goes. It uses Python lists and dictionaries to organize expense records, a tuple to store predefined expense categories, functions and separate modules to organize the code, and JSON file handling to preserve records between program runs. The console menu provides numbered choices so users can access these features through a command-line interface.

## B. Problem Description

Many individuals struggle to monitor and organize their daily expenses, especially when transactions are recorded manually or not tracked consistently. Without an organized system, users may find it difficult to identify where their money is being spent, determine which categories account for most of their expenses, and review their spending habits.

The Personal Expense Tracker addresses this problem by providing a console menu where users can record expenses, view transaction history, and review their spending totals. It stores expense records locally so that previously saved transactions can be loaded when the application is opened again.

### Inputs

- Expense amount
- Expense description
- Expense category
- Transaction date

### Processing

- Validate the amount, description, category, and date entered by the user.
- Add valid expenses to the expense records.
- Save and load expense records using a local JSON file.
- Calculate the total amount spent.
- Group expenses by category and calculate category totals.

### Outputs

- Updated transaction history containing recorded expenses
- Total amount of all recorded expenses
- Spending summaries grouped by category
- Error messages when invalid information is entered or file operations encounter problems

## C. Program Objectives

The objectives of the Personal Expense Tracker are:

1. To develop a Python console menu (console menu) that allows users to access the application's main features.
2. To allow users to record expenses by entering the amount, description, category, and transaction date.
3. To organize expenses into predefined categories so that transactions can be classified and reviewed easily.
4. To use file handling to save and load expense records from a local JSON file.
5. To calculate total expenses and summarize spending by category.

## D. Program Requirements and Features

### 1. Functional Requirements

The Personal Expense Tracker provides the following functions through its console menu:

| Feature | Description |
|---|---|
| Add an expense | Accept an amount, description, category, and date, validate the information, and add a valid expense record. |
| View expense history | Display recorded expense transactions in aligned console columns. |
| Calculate total expenses | Calculate and display the combined amount of recorded expenses. |
| Category summary | Calculate and display expense totals grouped by category. |
| Save records | Store expense records in a local JSON file. |
| Load records | Load previously saved expense records when the application starts. |
| Close the application | Allow users to exit through the main menu. |

The application displays category summaries as text. Pie chart visualization is not currently implemented.

The console menu offers: 1) Add an expense, 2) View transaction history, 3) View expense summary, 4) Save records, and 5) Exit.

### 2. Basic Input Requirements

- The expense amount must be numeric and greater than zero.
- The description must not be blank.
- The category must be one of the predefined categories supported by the program.
- The date must be a valid calendar date following the `YYYY-MM-DD` format.
- All required expense information must be valid before an expense can be added.

### 3. Assumptions and Limitations

- The program is designed for one user on a local computer.
- Expense records are stored locally in a JSON file rather than in an online database.
- The program does not connect to a bank account or automatically detect transactions.
- The accuracy of the summaries depends on the information entered by the user.
- Currency conversion and multiple-user accounts are outside the scope of the application.
- The application currently displays category summaries as text rather than graphical pie charts.

### 4. Implemented Features

The documented features are based on the current source code. The application has a console input and output console menu, input validation, expense history, total and category calculations, and local JSON file handling. Features not present in the source code should not be presented as implemented.

## E. Program Structure and Modules

The Personal Expense Tracker uses a modular file structure to organize the program into separate files. Each module has a specific responsibility, making the code easier to understand, maintain, and test.

### Project File Structure

```text
personal_expense_tracker/
├── main.py
├── expense_manager.py
├── file_handler.py
├── test_expense_manager.py
└── expenses.json
```

| File | Purpose |
|---|---|
| `main.py` | Creates the console input and output console menu, handles user interactions, and coordinates the application's features. |
| `expense_manager.py` | Contains functions for validating, adding, viewing, and summarizing expense records. |
| `file_handler.py` | Contains functions for saving and loading expense records using JSON file handling. |
| `test_expense_manager.py` | Contains automated unit tests for the expense management and file handling functions. |
| `expenses.json` | Stores expense records so they can be loaded when the application is opened again. |

### Example of Modular Programming

The `main.py` module imports functions and data from the other modules to access expense management and file handling features:

```python
from expense_manager import (
    CATEGORIES,
    add_expense,
    view_expenses,
    calculate_total,
    summarize_by_category,
    parse_amount,
)

from file_handler import load_expenses, save_expenses
```

This arrangement separates the console menu and user interaction from expense calculations and file operations. It also makes individual functions easier to locate, maintain, and test.

## F. Data Structures Used

The Personal Expense Tracker uses Python lists, dictionaries, and tuples to organize and manage expense information.

### 1. List

A list stores multiple expense records. The application uses a list to keep track of all recorded expenses.

```python
expenses = []
```

Each new expense is added to this list.

### 2. Dictionary

A dictionary represents an individual expense record. It stores information using key-value pairs.

```python
expense = {
    "amount": 150.00,
    "description": "Lunch",
    "category": "Food",
    "date": "2026-11-17"
}
```

Each key identifies a particular piece of expense information.

### 3. Tuple

A tuple stores the predefined expense categories. Since these categories are fixed in the program, a tuple is suitable for organizing them.

```python
CATEGORIES = (
    "Food",
    "Transportation",
    "Education",
    "Bills",
    "Entertainment",
    "Other"
)
```

### 4. List of Dictionaries

The application combines lists and dictionaries to store multiple expense records. Each item in the list represents one expense.

```python
expenses = [
    {
        "amount": 150.00,
        "description": "Lunch",
        "category": "Food",
        "date": "2026-11-17"
    },
    {
        "amount": 50.00,
        "description": "Bus fare",
        "category": "Transportation",
        "date": "2026-11-17"
    }
]
```

### 5. Dictionary for Category Summaries

The application uses a dictionary to organize calculated spending totals by category.

For example:

```python
{
    "Food": 150.00,
    "Transportation": 50.00
}
```

This makes it easier to retrieve and display the total expenses for each category.  

## G. Functions and Responsibilities

The following table describes suggested functions for the proposed design. Keep only the functions that exist in the final program and update their parameters and return values to match the code.

| Function | Parameters | Return value | Purpose |
|---|---|---|---|
| `parse_amount` | `text` | Validated numeric amount | Converts the entered text into a number, checks that it is finite and greater than zero, and rounds it to two decimal places. |
| `validate_date` | `date_text` | Validated date string | Checks whether the entered date is a valid calendar date in `YYYY-MM-DD` format. |
| `add_expense` | `expenses`, `amount`, `description`, `category`, `date` | None | Validates the expense information, creates an expense dictionary, and appends it to the expense list. |
| `view_expenses` | `expenses` | List of tuples | Returns expense records as tuples containing the date, description, category, and amount. |
| `calculate_total` | `expenses` | Numeric total | Calculates the combined amount of all recorded expenses. |
| `summarize_by_category` | `expenses` | Dictionary | Calculates the total expenses for each category. |
| `save_expenses` | `expenses`, `filename` | None | Saves expense records to a JSON file. |
| `load_expenses` | `filename` | List | Loads expense records from a JSON file. |

### Code excerpt 1: Calculating total expenses

```python
def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total
```

The function starts with a total of zero. It loops through the list of expense dictionaries, adds each record's amount, and returns the final total. This avoids repeating the same calculation in different parts of the program.

### Code excerpt 2: Summarizing expenses by category

```python
def summarize_by_category(expenses):
    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in summary:
            summary[category] = 0

        summary[category] += amount

    return summary
```

The function creates a dictionary named `summary`. For each expense, it checks whether the category already exists. If it does not, the function initializes its total to zero. It then adds the expense amount to that category and returns the completed summary.

### Code Excerpt 3: Adding an Expense

```python
def add_expense(expenses, amount, description, category, date):
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
```

The function validates the amount by checking that it is numeric, finite, and greater than zero. It also checks that the description is not blank, verifies that the category belongs to the predefined categories, and validates the date using `validate_date()`.

Once all information passes validation, the function creates an expense dictionary and appends it to the expense list. If any required information is invalid, a `ValueError` is raised and the expense is not added.

### Excerpt 4 – Viewing Expenses

```python
def view_expenses(expenses):
    rows = []

    for expense in expenses:
        rows.append((
            expense["date"],
            expense["description"],
            expense["category"],
            expense["amount"]
        ))

    return rows
```

The `view_expenses()` function creates an empty list named `rows`. It loops through the expense records and appends each record as a tuple containing its date, description, category, and amount.

The function returns the completed list of tuples, which the console menu uses to display transaction history. This separates data preparation from user-facing output.

## H. File Handling and Data Storage

The Personal Expense Tracker uses a local JSON file named `expenses.json` to store expense records. JSON is suitable for this program because it can represent the lists and dictionaries used to organize expense information.

The file is stored in the same directory as `main.py`, allowing the application to access saved records when it starts.

### 1. Saving records

The `save_expenses()` function in `file_handler.py` writes the expense list into the JSON file.

- It uses write mode (`"w"`) to create or overwrite the file.
- It uses UTF-8 encoding when opening the file.
- It uses `json.dump()` with an indentation of 4 spaces to make the stored data easier to read.

When new expenses are saved, the JSON file is updated with the current expense list.

### 2. Loading records

The `load_expenses()` function reads the saved records from `expenses.json`.

- It uses read mode (`"r"`) with UTF-8 encoding.
- It uses `json.load()` to convert the JSON data into Python objects.
- If the file does not exist, the function returns an empty list.
- It checks that the loaded data is a list and that its records have the required structure, including the `amount`, `description`, `category`, and `date` fields.
- It also checks that the amount is numeric.

This validation helps prevent incorrectly structured data from being used as valid expense records.

### 3. Handling missing or damaged files

The application handles file-related problems so that missing or damaged data does not unnecessarily prevent the program from starting.

| Situation | Application behavior |
|---|---|
| `expenses.json` does not exist | Starts with an empty expense list. |
| JSON data is malformed or invalid | Reports a data error and attempts to preserve the damaged file as a `.bak` backup before starting with an empty list. |
| A file operation fails | Handles the `OSError` and displays an appropriate error message. |
| Saving fails after an expense is added | Warns the user that the expense was added in the current session but was not saved to the file. |

The application does not silently treat damaged JSON data as valid. Its recovery behavior attempts to preserve the original file before continuing.

### 4. File modes used

| Mode | Purpose |
|---|---|
| `r` | Reads an existing file. |
| `w` | Writes data and replaces the existing file contents. |
| `a` | Adds data to the end of a file. |

The project uses `r` and `w` for loading and saving expense records. It does not use append mode (`a`) for its JSON storage.

### 5. Example of stored JSON data

A saved expense record follows this general structure:

```json
[
    {
        "amount": 150.0,
        "description": "School supplies",
        "category": "Education",
        "date": "2026-11-13"
    }
]
```

Each expense is represented as a JSON object containing its amount, description, category, and date. Multiple expense records can be stored together in the same JSON list.

The data remains available between program runs when saving and loading complete successfully.

## I. Error Handling

The Personal Expense Tracker uses input validation and exception handling to prevent invalid expense records and handle file-related problems. Since the application uses a console menu (console menu), errors are communicated through console input and output message boxes instead of console messages.

### 1. Input validation

The application checks the information entered before adding an expense.

| Possible error | Example cause | Application behavior |
|---|---|---|
| Invalid amount | User enters letters or other non-numeric text. | Rejects the input and displays an error message. |
| Invalid amount value | User enters zero, a negative number, or a non-finite value. | Rejects the amount because it must be greater than zero. |
| Blank description | User leaves the description empty or enters only spaces. | Rejects the expense and displays an error message. |
| Invalid category | The selected category is not in the predefined category list. | Rejects the expense. |
| Invalid date | The date is not a valid calendar date or does not follow `YYYY-MM-DD`. | Rejects the expense. |

### 2. File-related error handling

The application also handles problems involving the local `expenses.json` file.

| Possible error | Example cause | Application behavior |
|---|---|---|
| `FileNotFoundError` | The expense file does not exist yet. | Starts with an empty expense list. |
| `ValueError` | The JSON data is damaged or does not follow the expected structure. | Attempts to rename the damaged file with a `.bak` extension, displays an error message, and starts with an empty list. |
| `OSError` | A file operation fails because of a system or file-access problem. | Handles the error and displays an appropriate message. |
| Save failure | The application cannot write the updated expense list. | Warns the user that the expense was added to the current session but was not saved to the file. |

### 3. Exception handling

The program uses `try` and `except` blocks to handle operations that may fail, such as converting the amount into a number and reading or writing the JSON file.

For example, the amount entered by the user is passed to `parse_amount()`. If it cannot be converted into a valid positive numeric amount, the function raises a `ValueError`. The console menu handles this error and informs the user instead of allowing the application to terminate unexpectedly.

### 4. Importance of error handling

Error handling helps the application remain usable when users enter incorrect information or when file operations fail. It also helps protect saved expense records by attempting to preserve damaged data before starting with an empty list.

The application focuses on expected input and file-related errors rather than hiding all possible programming errors with a broad exception handler.

## J. Testing and Results

The Personal Expense Tracker was tested using Python's built-in `unittest` framework to verify the functionality of its expense management and file handling modules.

### 1. Testing method

The project uses automated unit tests to check individual functions and confirm that they behave as expected.

The tests are executed using the following command:

```bash
python -m unittest test_expense_manager -v
```

### 2. Test cases

The project contains 14 unit tests covering the following cases:

| Test case | Expected result |
|---|---|
| Adding a valid expense | Expense is added successfully. |
| Calculating the total | Returns the correct sum of expenses. |
| Adding a negative amount | Rejects the invalid amount. |
| Adding a nonnumeric amount | Rejects the invalid amount. |
| Loading a missing file | Returns an empty list. |
| Summarizing expenses by category | Returns the correct category totals. |
| Adding a boundary amount | Accepts a valid positive amount. |
| Adding a blank description | Rejects the expense. |
| Adding an invalid date | Rejects the expense. |
| Adding an invalid category | Rejects the expense. |
| Saving and loading expenses | Restores the saved expense records correctly. |
| Loading damaged JSON data | Detects invalid JSON data. |
| Calculating the total of an empty list | Returns zero. |
| Viewing expenses | Returns the expected tuple rows. |

### 3. Test results

All 14 unit tests passed when executed using the `unittest` framework.

This indicates that the tested expense management and file handling functions behaved as expected under the tested conditions.

### 4. Testing limitations

The automated tests focus on the expense management and file handling functions. They do not automatically test the console input and output console menu.

The console menu should also be checked manually to verify that users can enter expenses, view transaction history, see expense summaries, and receive appropriate error messages.

### 5. Conclusion of testing

The successful unit tests provide evidence that the core functions of the application work as intended. Additional manual testing of the console menu helps verify the overall user experience.

## K. Conclusion and Future Improvements

### 1. Conclusion

The Personal Expense Tracker is a Python-based console application designed to help users record and monitor their personal expenses.

The program allows users to enter expense amounts, descriptions, categories, and dates through a console input and output interface. It also provides a transaction history, calculates total expenses, and displays expense summaries grouped by category.

The application uses Python data structures such as lists, dictionaries, and tuples to organize expense information. Its modular design separates the console menu, expense management functions, and JSON file handling. Expense records are stored locally in a JSON file so they can be loaded again when the application starts.

The project demonstrates the use of Python functions, data structures, input validation, exception handling, file operations, modular programming, and automated unit testing.

### 2. Future Improvements

Although the current application provides its main expense-tracking features, several improvements could be added in future versions:

1. **Pie Chart Visualization** – Add graphical charts to make category-based expense comparisons easier to understand.
2. **Expense Editing and Deletion** – Allow users to modify or remove existing expense records.
3. **Search and Filtering** – Allow users to find expenses by description, category, or date.
4. **Monthly and Yearly Reports** – Provide summaries for specific time periods.
5. **Data Export** – Allow users to export expense records into formats such as CSV or Excel.

These improvements could make the application more flexible and useful while building upon its existing functionality.

## L. References

- Python Software Foundation. *Python 3 Documentation*. https://docs.python.org/3/
- Python Software Foundation. *Python Tutorial — Input and Output*. https://docs.python.org/3/tutorial/inputoutput.html
- Python Software Foundation. *unittest — Unit Testing Framework*. https://docs.python.org/3/library/unittest.html
- Python Software Foundation. *json — JSON Encoder and Decoder*. https://docs.python.org/3/library/json.html

---


