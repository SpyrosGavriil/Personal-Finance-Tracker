import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description
import matplotlib.pyplot as plt

class CSV:
    CSV_FILE = "finance_data.csv"  # Define the file name for storing transactions
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"  # Define the date format for consistency

    # Initialize the CSV file, ensuring it exists with the correct structure
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            # Create the file with predefined columns if it doesn't exist
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    # Add a new entry (transaction) to the CSV file
    @classmethod
    def add_entry(cls, date, amount, category, description):
        new_entry = {
            "date": date,
            "amount": amount,
            "category": category,
            "description": description,
        }

        with open(cls.CSV_FILE, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully")

    # Retrieve transactions within a specified date range
    @classmethod
    def get_transactions(cls, start_date, end_date):
        try:
            df = pd.read_csv(cls.CSV_FILE)
            df["date"] = pd.to_datetime(df["date"], format=CSV.FORMAT)
            start_date = datetime.strptime(start_date, CSV.FORMAT)
            end_date = datetime.strptime(end_date, CSV.FORMAT)

            # Filter transactions based on the date range
            mask = (df["date"] >= start_date) & (df["date"] <= end_date)
            filtered_df = df.loc[mask]

            if filtered_df.empty:
                print("No transactions found in the given date range.")
            else:
                print(f"Transactions from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(CSV.FORMAT)}")
                print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV.FORMAT)}))

                # Summary of transactions
                total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
                total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()
                print("\nSummary:")
                print(f"Total Income:  ${total_income:.2f}")
                print(f"Total Expense:  ${total_expense:.2f}")
                print(f"Net Savings: ${(total_income - total_expense):.2f}")

            return filtered_df
        except FileNotFoundError:
            print("Transaction file not found. Please add a transaction first.")
            return pd.DataFrame()

# Helper function to add a new transaction
def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or press Enter for today's date: ", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)

# Plot income and expense trends over time
def plot_transactions(df):
    try:
        df.set_index("date", inplace=True)

        # Prepare income and expense data for plotting
        income_df = df[df["category"] == "Income"].resample("D").sum().reindex(df.index, fill_value=0)
        expense_df = df[df["category"] == "Expense"].resample("D").sum().reindex(df.index, fill_value=0)

        # Create the plot
        plt.figure(figsize=(10, 5))
        plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
        plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
        plt.xlabel("Date")
        plt.ylabel("Amount")
        plt.title("Income and Expenses Over Time")
        plt.legend()
        plt.grid(True)
        plt.show()
    except KeyError:
        print("No data to plot. Please ensure valid transactions are provided.")

# Main menu for user interaction
def main():
    while True:
        print("\n1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end date (dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date, end_date)
            if not df.empty and input("Do you want to see a plot? (y/n): ").lower() == "y":
                plot_transactions(df)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.")

# Entry point for the script
if __name__ == "__main__":
    main()
