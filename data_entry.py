from datetime import datetime

# Define the date format for consistency across functions
date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}

# Get a valid date from the user, with an option to use today's date as the default
def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        # Provide user-friendly error message for invalid date input
        print("Invalid date format. Please enter the date in dd-mm-yyyy format")
        return get_date(prompt, allow_default)

# Get a positive, non-zero amount from the user
def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            # Ensure amounts are valid for financial transactions
            raise ValueError("Amount must be a positive non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

# Get a category ('Income' or 'Expense') based on user input
def get_category():
    category = input("Enter the category ('I' for Income or 'E' for Expense): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    # Ensure user chooses a valid category
    print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()

# Get an optional description from the user
def get_description():
    return input("Enter a description (optional): ")
