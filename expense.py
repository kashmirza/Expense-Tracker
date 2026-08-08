from datetime import datetime
from file_handler import load_data, save_data
from collections import defaultdict

EXPENSE_FILE = "expense.json"

def expense_menu():

    while True:

        print("\n" + "=" * 60)
        print("             💸 EXPENSE MANAGEMENT")
        print("=" * 60)

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Search Expense")
        print("6. Monthly Expense Report")
        print("7. Total Expenses")
        print("8. Back")

        print("=" * 60)

        choice = input("Enter Choice : ")

        if choice in [str(i) for i in range(1, 9)]:
            return choice

        print("❌ Invalid Choice.")
def generate_expense_id(expenses):

    if not expenses:
        return "EXP001"

    last_id = expenses[-1]["id"]

    number = int(last_id[3:]) + 1

    return f"EXP{number:03d}"
def get_user_expenses(username):

    expenses = load_data(EXPENSE_FILE)

    if not isinstance(expenses, list):
        expenses = []

    user_expenses = []

    for expense in expenses:

        if expense["username"] == username:
            user_expenses.append(expense)

    return expenses, user_expenses
def display_expense_table(user_expenses):

    if not user_expenses:
        print("\n❌ No Expense Records Found.")
        return

    print("\n" + "=" * 115)

    print(f"{'No':<5}{'ID':<10}{'Category':<18}{'Title':<20}{'Amount':<15}{'Date':<15}")

    print("=" * 115)

    total = 0

    for i, expense in enumerate(user_expenses, start=1):

        print(
            f"{i:<5}"
            f"{expense['id']:<10}"
            f"{expense['category']:<18}"
            f"{expense['title']:<20}"
            f"Rs.{expense['amount']:<12}"
            f"{expense['date']:<15}"
        )

        total += expense["amount"]

    print("=" * 115)
    print(f"Total Expense : Rs.{total}")
def add_expense(username):

    expenses, _ = get_user_expenses(username)

    print("\n" + "=" * 60)
    print("                ADD EXPENSE")
    print("=" * 60)

    categories = {
        "1": "Food",
        "2": "Transport",
        "3": "Shopping",
        "4": "Bills",
        "5": "Education",
        "6": "Health",
        "7": "Entertainment",
        "8": "Other"
    }

    print("\nSelect Expense Category")

    for key, value in categories.items():
        print(f"{key}. {value}")

    while True:

        choice = input("Choose Category : ")

        if choice in categories:
            category = categories[choice]
            break

        print("❌ Invalid Choice.")

    while True:

        title = input("\nExpense Title : ").strip()

        if title:
            break

        print("❌ Title cannot be empty.")

    while True:

        try:

            amount = float(input("Amount : "))

            if amount <= 0:
                print("❌ Amount must be greater than zero.")
                continue

            break

        except ValueError:
            print("❌ Invalid Amount.")

    description = input("Description : ").strip()

    now = datetime.now()

    expense = {

        "id": generate_expense_id(expenses),

        "username": username,

        "category": category,

        "title": title,

        "amount": amount,

        "description": description,

        "date": now.strftime("%Y-%m-%d"),

        "time": now.strftime("%I:%M %p")
    }

    expenses.append(expense)

    save_data(EXPENSE_FILE, expenses)

    print("\n" + "=" * 60)
    print("        ✅ EXPENSE ADDED SUCCESSFULLY")
    print("=" * 60)

    print(f"Transaction ID : {expense['id']}")
    print(f"Category       : {expense['category']}")
    print(f"Title          : {expense['title']}")
    print(f"Amount         : Rs.{expense['amount']}")
    print(f"Date           : {expense['date']}")
    print(f"Time           : {expense['time']}")

    print("=" * 60)

def view_expense(username):

    _, user_expenses = get_user_expenses(username)

    if not user_expenses:
        print("\n❌ No Expense Records Found.")
        return

    print("\n" + "=" * 115)
    print(" " * 45 + "YOUR EXPENSES")
    print("=" * 115)

    display_expense_table(user_expenses)
def display_expense_table(user_expenses):

    if not user_expenses:
        print("\n❌ No Expense Records Found.")
        return

    print("\n" + "=" * 120)

    print(f"{'No':<5}{'ID':<10}{'Category':<18}{'Title':<20}{'Amount':<15}{'Date':<15}")

    print("=" * 120)

    total = 0

    for index, expense in enumerate(user_expenses, start=1):

        print(
            f"{index:<5}"
            f"{expense['id']:<10}"
            f"{expense['category']:<18}"
            f"{expense['title']:<20}"
            f"Rs.{expense['amount']:<12}"
            f"{expense['date']:<15}"
        )

        total += expense["amount"]

    print("=" * 120)

    print(f"Total Expense : Rs.{total:,.2f}")

def update_expense(username):

    expenses, user_expenses = get_user_expenses(username)

    if not user_expenses:
        print("\n❌ No Expense Records Found.")
        return

    print("\n" + "=" * 115)
    print(" " * 45 + "UPDATE EXPENSE")
    print("=" * 115)

    display_expense_table(user_expenses)

    while True:

        try:
            record = int(input("\nSelect Record Number : "))

            if 1 <= record <= len(user_expenses):
                break

            print("❌ Invalid Record Number.")

        except ValueError:
            print("❌ Please enter numbers only.")

    expense = user_expenses[record - 1]

    print("\nCurrent Details")
    print("-" * 45)
    print(f"Category    : {expense['category']}")
    print(f"Title       : {expense['title']}")
    print(f"Amount      : Rs.{expense['amount']}")
    print(f"Description : {expense['description']}")
    print("-" * 45)

    print("\nLeave blank to keep old value.")

    # Category
    categories = {
        "1": "Food",
        "2": "Transport",
        "3": "Shopping",
        "4": "Bills",
        "5": "Education",
        "6": "Health",
        "7": "Entertainment",
        "8": "Other"
    }

    print("\nExpense Categories")

    for key, value in categories.items():
        print(f"{key}. {value}")

    category_choice = input("New Category (Enter to Skip): ").strip()

    # Title
    new_title = input("New Title (Enter to Skip): ").strip()

    # Amount
    while True:

        new_amount = input("New Amount (Enter to Skip): ").strip()

        if new_amount == "":
            break

        try:

            new_amount = float(new_amount)

            if new_amount <= 0:
                print("❌ Amount must be greater than zero.")
                continue

            break

        except ValueError:
            print("❌ Invalid Amount.")

    # Description
    new_description = input("New Description (Enter to Skip): ").strip()

    # Update Data

    if category_choice in categories:
        expense["category"] = categories[category_choice]

    if new_title:
        expense["title"] = new_title

    if new_amount != "":
        expense["amount"] = new_amount

    if new_description:
        expense["description"] = new_description

    save_data(EXPENSE_FILE, expenses)

    print("\n" + "=" * 50)
    print("     ✅ EXPENSE UPDATED SUCCESSFULLY")
    print("=" * 50)

    print(f"Category : {expense['category']}")
    print(f"Title    : {expense['title']}")
    print(f"Amount   : Rs.{expense['amount']}")
    print("=" * 50)

def delete_expense(username):

    expenses, user_expenses = get_user_expenses(username)

    if not user_expenses:
        print("\n❌ No Expense Records Found.")
        return

    print("\n" + "=" * 115)
    print(" " * 45 + "DELETE EXPENSE")
    print("=" * 115)

    display_expense_table(user_expenses)

    while True:

        try:

            record = int(input("\nSelect Record Number : "))

            if 1 <= record <= len(user_expenses):
                break

            print("❌ Invalid Record Number.")

        except ValueError:

            print("❌ Please enter numbers only.")

    expense = user_expenses[record - 1]

    print("\nSelected Record")
    print("-" * 45)
    print(f"Category    : {expense['category']}")
    print(f"Title       : {expense['title']}")
    print(f"Amount      : Rs.{expense['amount']}")
    print(f"Description : {expense['description']}")
    print("-" * 45)

    confirm = input("\nDelete this expense? (Y/N): ").strip().lower()

    if confirm == "y":

        expenses.remove(expense)

        save_data(EXPENSE_FILE, expenses)

        print("\n✅ Expense Deleted Successfully.")

    else:

        print("\nDelete Cancelled.")

def search_expense(username):

    _, user_expenses = get_user_expenses(username)

    if not user_expenses:
        print("\n❌ No Expense Records Found.")
        return

    while True:

        print("\n" + "=" * 70)
        print("                 🔍 SEARCH EXPENSE")
        print("=" * 70)

        print("1. Search by Title")
        print("2. Search by Category")
        print("3. Search by Date")
        print("4. Search by Amount")
        print("5. Search by Description")
        print("6. Back")

        print("=" * 70)

        choice = input("Enter Choice : ")

        if choice == "1":

            keyword = input("Enter Title : ").strip().lower()

            results = [
                expense for expense in user_expenses
                if keyword in expense["title"].lower()
            ]

        elif choice == "2":

            keyword = input("Enter Category : ").strip().lower()

            results = [
                expense for expense in user_expenses
                if keyword == expense["category"].lower()
            ]

        elif choice == "3":

            keyword = input("Enter Date (YYYY-MM-DD): ").strip()

            results = [
                expense for expense in user_expenses
                if keyword == expense["date"]
            ]

        elif choice == "4":

            try:

                amount = float(input("Enter Amount : "))

                results = [
                    expense for expense in user_expenses
                    if expense["amount"] == amount
                ]

            except ValueError:

                print("❌ Invalid Amount.")
                continue

        elif choice == "5":

            keyword = input("Enter Description : ").strip().lower()

            results = [
                expense for expense in user_expenses
                if keyword in expense["description"].lower()
            ]

        elif choice == "6":

            return

        else:

            print("❌ Invalid Choice.")
            continue

        if not results:

            print("\n❌ No Matching Records Found.")

        else:

            display_expense_table(results)




def monthly_expense_report(username):

    _, user_expenses = get_user_expenses(username)

    if not user_expenses:
        print("\n❌ No Expense Records Found.")
        return

    month = input("\nEnter Month (MM): ").strip()
    year = input("Enter Year (YYYY): ").strip()

    monthly_records = []

    for expense in user_expenses:

        date = expense["date"].split("-")

        if date[0] == year and date[1] == month:
            monthly_records.append(expense)

    if not monthly_records:
        print("\n❌ No Expense Records Found For This Month.")
        return

    total = 0

    highest = monthly_records[0]

    category_summary = defaultdict(float)

    for expense in monthly_records:

        total += expense["amount"]

        category_summary[expense["category"]] += expense["amount"]

        if expense["amount"] > highest["amount"]:
            highest = expense

    average = total / len(monthly_records)

    print("\n" + "=" * 60)
    print("            MONTHLY EXPENSE REPORT")
    print("=" * 60)

    print(f"Month               : {month}/{year}")
    print(f"Total Transactions  : {len(monthly_records)}")
    print(f"Total Expense       : Rs.{total:,.2f}")
    print(f"Highest Expense     : {highest['title']} (Rs.{highest['amount']:,.2f})")
    print(f"Average Expense     : Rs.{average:,.2f}")

    print("\nCategory Summary")
    print("-" * 40)

    for category, amount in category_summary.items():

        print(f"{category:<20} Rs.{amount:,.2f}")

    print("=" * 60)

def total_expense(username):

    _, user_expenses = get_user_expenses(username)

    if not user_expenses:
        print("\n❌ No Expense Records Found.")
        return

    total = sum(expense["amount"] for expense in user_expenses)

    highest = max(user_expenses, key=lambda x: x["amount"])

    lowest = min(user_expenses, key=lambda x: x["amount"])

    average = total / len(user_expenses)

    print("\n" + "=" * 60)
    print("             TOTAL EXPENSE SUMMARY")
    print("=" * 60)

    print(f"Total Transactions : {len(user_expenses)}")
    print(f"Total Expense      : Rs.{total:,.2f}")
    print(f"Average Expense    : Rs.{average:,.2f}")
    print(f"Highest Expense    : {highest['title']} (Rs.{highest['amount']:,.2f})")
    print(f"Lowest Expense     : {lowest['title']} (Rs.{lowest['amount']:,.2f})")

    print("=" * 60)