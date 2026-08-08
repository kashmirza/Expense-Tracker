import csv
import os

from income import get_user_incomes
from expense import get_user_expenses


# ==========================================================
#                    CSV EXPORT MENU
# ==========================================================

def csv_export_menu():

    while True:

        print("\n" + "=" * 60)
        print("                  📄 EXPORT CSV")
        print("=" * 60)

        print("1. Export Income")
        print("2. Export Expenses")
        print("3. Export Financial Summary")
        print("4. Back")

        print("=" * 60)

        choice = input("Enter Choice : ").strip()

        if choice in ["1", "2", "3", "4"]:
            return choice

        print("\n❌ Invalid Choice!")


# ==========================================================
#                    EXPORT INCOME
# ==========================================================

def export_income_csv(username):

    _, incomes = get_user_incomes(username)

    if not incomes:

        print("\n❌ No income records found.")
        return

    filename = f"{username}_income_report.csv"

    fieldnames = [
        "ID",
        "Category",
        "Source",
        "Amount",
        "Description",
        "Date",
        "Time"
    ]

    try:

        with open(
            filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            for income in incomes:

                writer.writerow({
                    "ID": income.get("id", ""),
                    "Category": income.get("category", "Other"),
                    "Source": income.get("source", ""),
                    "Amount": income.get("amount", 0),
                    "Description": income.get("description", ""),
                    "Date": income.get("date", ""),
                    "Time": income.get("time", "")
                })

        print("\n" + "=" * 60)
        print("       ✅ INCOME CSV EXPORTED SUCCESSFULLY")
        print("=" * 60)
        print(f"File Name : {filename}")
        print(f"Location  : {os.path.abspath(filename)}")
        print("=" * 60)

    except OSError as error:

        print(f"\n❌ Error creating CSV file: {error}")


# ==========================================================
#                    EXPORT EXPENSES
# ==========================================================

def export_expense_csv(username):

    _, expenses = get_user_expenses(username)

    if not expenses:

        print("\n❌ No expense records found.")
        return

    filename = f"{username}_expense_report.csv"

    fieldnames = [
        "ID",
        "Category",
        "Description",
        "Amount",
        "Date",
        "Time"
    ]

    try:

        with open(
            filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()

            for expense in expenses:

                writer.writerow({
                    "ID": expense.get("id", ""),
                    "Category": expense.get("category", "Other"),
                    "Description": expense.get("description", ""),
                    "Amount": expense.get("amount", 0),
                    "Date": expense.get("date", ""),
                    "Time": expense.get("time", "")
                })

        print("\n" + "=" * 60)
        print("      ✅ EXPENSE CSV EXPORTED SUCCESSFULLY")
        print("=" * 60)
        print(f"File Name : {filename}")
        print(f"Location  : {os.path.abspath(filename)}")
        print("=" * 60)

    except OSError as error:

        print(f"\n❌ Error creating CSV file: {error}")


# ==========================================================
#                EXPORT FINANCIAL SUMMARY
# ==========================================================

def export_financial_summary_csv(username):

    _, incomes = get_user_incomes(username)
    _, expenses = get_user_expenses(username)

    if not incomes and not expenses:

        print("\n❌ No financial records found.")
        return

    total_income = sum(
        income.get("amount", 0)
        for income in incomes
    )

    total_expense = sum(
        expense.get("amount", 0)
        for expense in expenses
    )

    savings = total_income - total_expense

    filename = f"{username}_financial_summary.csv"

    try:

        with open(
            filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Financial Summary"
            ])

            writer.writerow([])

            writer.writerow([
                "Total Income",
                total_income
            ])

            writer.writerow([
                "Total Expense",
                total_expense
            ])

            writer.writerow([
                "Savings",
                savings
            ])

        print("\n" + "=" * 60)
        print("   ✅ FINANCIAL SUMMARY EXPORTED SUCCESSFULLY")
        print("=" * 60)
        print(f"File Name : {filename}")
        print(f"Location  : {os.path.abspath(filename)}")
        print("=" * 60)

    except OSError as error:

        print(f"\n❌ Error creating CSV file: {error}")