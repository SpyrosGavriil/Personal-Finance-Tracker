import tkinter as tk
from tkinter import ttk, messagebox
from data_entry import get_date, get_amount, get_category, get_description
from main import CSV, plot_transactions
import pandas as pd

# Initialize the Tkinter window
root = tk.Tk()
root.title("Personal Finance Tracker")
root.geometry("650x500")

# Global Variables
category_var = tk.StringVar(value="Income")


from datetime import datetime


def add_transaction():
    try:
        date = datetime.strptime(date_entry.get(), "%d-%m-%Y").strftime("%d-%m-%Y")
        amount = float(amount_entry.get())
        category = category_var.get()
        description = description_entry.get()

        CSV.add_entry(date, amount, category, description)
        messagebox.showinfo("Success", "Transaction added successfully!")
        date_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        description_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use dd-mm-yyyy.")


def view_transactions():
    try:
        start_date = datetime.strptime(start_date_entry.get(), "%d-%m-%Y").strftime(
            "%d-%m-%Y"
        )
        end_date = datetime.strptime(end_date_entry.get(), "%d-%m-%Y").strftime(
            "%d-%m-%Y"
        )
        df = CSV.get_transactions(start_date, end_date)

        # Clear the table before inserting new data
        for row in transactions_table.get_children():
            transactions_table.delete(row)

        if not df.empty:
            for _, row in df.iterrows():
                transactions_table.insert(
                    "",
                    "end",
                    values=(
                        row["date"],
                        row["amount"],
                        row["category"],
                        row["description"],
                    ),
                )
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use dd-mm-yyyy.")


# Plot Transactions Function
def plot_transactions_ui():
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    df = CSV.get_transactions(start_date, end_date)
    if not df.empty:
        plot_transactions(df)


# ---------------- Layout Configuration -------------------

# Add Transaction Section
tk.Label(root, text="Add New Transaction", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text="Date (dd-mm-yyyy):").pack()
date_entry = tk.Entry(root)
date_entry.pack()

tk.Label(root, text="Amount:").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category:").pack()
category_menu = ttk.Combobox(
    root, textvariable=category_var, values=["Income", "Expense"]
)
category_menu.pack()

tk.Label(root, text="Description:").pack()
description_entry = tk.Entry(root)
description_entry.pack()

tk.Button(root, text="Add Transaction", command=add_transaction).pack(pady=5)

# Date Range for Viewing Transactions
tk.Label(root, text="View Transactions", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text="Start Date (dd-mm-yyyy):").pack()
start_date_entry = tk.Entry(root)
start_date_entry.pack()

tk.Label(root, text="End Date (dd-mm-yyyy):").pack()
end_date_entry = tk.Entry(root)
end_date_entry.pack()

tk.Button(root, text="View Transactions", command=view_transactions).pack(pady=5)

# Transactions Table (Treeview)
transactions_table = ttk.Treeview(
    root, columns=("date", "amount", "category", "description"), show="headings"
)
transactions_table.heading("date", text="Date")
transactions_table.heading("amount", text="Amount")
transactions_table.heading("category", text="Category")
transactions_table.heading("description", text="Description")
transactions_table.pack(pady=10)

# Plot Button
tk.Button(root, text="Plot Transactions", command=plot_transactions_ui).pack(pady=5)

# Exit Button
tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

# Run the Tkinter Loop
root.mainloop()
