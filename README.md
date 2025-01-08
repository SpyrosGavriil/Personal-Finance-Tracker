
# Personal Finance Tracker

This is a **Personal Finance Tracker** application built in Python. It allows you to manage your income and expenses, view financial summaries, and visualize your transactions over time. The program uses a CSV file to store transaction data and provides a user-friendly interface for adding transactions and analyzing your financial habits.

## Features

- **Add Transactions**: Record income or expenses with details like date, amount, category, and description.
- **View Transactions**: Filter and view transactions within a specific date range.
- **Financial Summary**: Calculate total income, total expenses, and net savings for a given period.
- **Visualizations**: Plot income and expenses over time using Matplotlib.

## How to Run

1. **Clone the Repository**
   ```bash
   git clone <repository_url>
   cd Personal-Finance-Tracker
   ```

2. **Install Dependencies**
   Ensure you have Python installed. Then install the required packages:
   ```bash
   pip install pandas matplotlib
   ```

3. **Run the Program**
   Execute the `main.py` script:
   ```bash
   python main.py
   ```

## Usage

### 1. Add a New Transaction
- You will be prompted to enter:
  - **Date**: Enter the transaction date in `dd-mm-yyyy` format, or press Enter to use today's date.
  - **Amount**: Enter the transaction amount (must be a positive number).
  - **Category**: Choose 'I' for Income or 'E' for Expense.
  - **Description**: Optionally, add a description for the transaction.
- The transaction will be saved in the `finance_data.csv` file.

### 2. View Transactions and Summary
- Enter a start and end date to filter transactions within that range.
- The program will display:
  - A list of transactions with date, amount, category, and description.
  - A summary of total income, total expenses, and net savings.
- You will also be asked if you want to see a plot of your income and expenses over time.

### 3. Exit
- Exits the program.

## Data Storage
- Transactions are stored in a CSV file named `finance_data.csv` in the project directory.
- The CSV file includes the following columns:
  - `date`: The transaction date.
  - `amount`: The transaction amount.
  - `category`: Either "Income" or "Expense".
  - `description`: Optional transaction details.

## Example Usage

### Adding a Transaction
```
Enter the date of the transaction (dd-mm-yyyy) or press Enter for today's date: 10-08-2024
Enter the amount: 150.75
Enter the category ('I' for Income or 'E' for Expense): I
Enter a description (optional): Freelance work
Entry added successfully.
```

### Viewing Transactions and Summary
```
Enter the start date (dd-mm-yyyy): 01-08-2024
Enter the end date (dd-mm-yyyy): 31-08-2024
Transactions from 01-08-2024 to 31-08-2024:
 date         amount  category      description
01-08-2024   150.00  Expense       Groceries
08-08-2024   300.00  Income        Freelance
...
Summary:
Total Income:  $450.00
Total Expense: $150.00
Net Savings:   $300.00
Do you want to see a plot? (y/n): y
# (A plot will be displayed)
```

## Requirements
- Python 3.6+
- Libraries:
  - `pandas`: For data manipulation.
  - `matplotlib`: For data visualization.

## Notes
- Ensure the `finance_data.csv` file is in the same directory as the script. If it doesn't exist, the program will automatically create it.
- Use consistent date formats (`dd-mm-yyyy`) when entering dates.

## License
This project is free to use and modify.

---

Feel free to edit or enhance this README file as needed for your project! Let me know if you need further help. 😊
