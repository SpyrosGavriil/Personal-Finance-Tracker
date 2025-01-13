# Personal Finance Tracker

This project is a **Personal Finance Tracker** built with Python using **Tkinter** for the user interface and **pandas** for data handling. It allows users to record and track their income and expenses conveniently with CSV file storage.

---

## 📦 **Features:**
- ✅ **Add Transactions:** Add income and expense entries with date, amount, category, and description.
- ✅ **View Transactions:** Display transactions within a specified date range in a tabular format.
- ✅ **Plot Transactions:** Generate a graph showing income and expense trends over time.
- ✅ **CSV-Based Storage:** Transactions are stored in a CSV file (`finance_data.csv`).

---

## 📂 **Project Structure:**
```plaintext
📁 finance_tracker
├── 📄 main.py              # CSV management and data handling
├── 📄 data_entry.py        # User input validation functions
├── 📄 finance_tracker_gui.py  # Tkinter-based GUI for the finance tracker
├── 📄 finance_data.csv     # CSV file for storing transactions
├── 📄 README.md            # Project documentation
```

---

## 🚀 **Installation Instructions:**

1. **Clone the repository:**
```bash
 git clone <repository_url>
```

2. **Navigate to the project folder:**
```bash
cd finance_tracker
```

3. **Install required packages:**
```bash
pip install pandas matplotlib
```

4. **Run the Tkinter GUI:**
```bash
python finance_tracker_gui.py
```

---

## 🎯 **Usage Guide:**

### ✅ **Adding a New Transaction:**
1. Open the **Tkinter GUI** using the command above.
2. Enter the **date** (dd-mm-yyyy format).
3. Enter the **amount**.
4. Select the **category** (Income or Expense).
5. Add a brief **description**.
6. Click **Add Transaction**.

### ✅ **Viewing Transactions:**
1. Enter a **start date** and **end date** (dd-mm-yyyy format).
2. Click **View Transactions**.
3. Transactions will be displayed in a table below.

### ✅ **Plotting Income and Expense Trends:**
- After viewing transactions, click **Plot Transactions** to generate a graph.

---

## ⚙️ **CSV File Handling:**
- Transactions are stored in `finance_data.csv`.
- The CSV columns are: `date`, `amount`, `category`, `description`.
- Date format used is: `dd-mm-yyyy`.

---

## 📊 **Key Changes in this Version:**
- Added a **Tkinter GUI** (`finance_tracker_gui.py`) for better usability.
- Automated date validation using the **dd-mm-yyyy** format.
- Enhanced error handling for invalid date and amount inputs.
- Improved CSV handling with **pandas** for filtering and plotting transactions.

---

## 🛠️ **Possible Improvements:**
- Exporting the project as an executable (`.exe` file).
- Adding monthly summary reports.
- Implementing data encryption for sensitive financial data.

---

## 📃 **License:**
This project is intended for educational purposes and personal use only.

---

**Feel free to contribute to this project!** 🚀
