from collections import defaultdict

from income import get_user_incomes
from expense import get_user_expenses


# ==========================================================
#                    ANALYTICS MENU
# ==========================================================

def analytics_menu():

    while True:

        print("\n" + "=" * 60)
        print("                 📈 ANALYTICS")
        print("=" * 60)

        print("1. Spending by Category")
        print("2. Monthly Income Analysis")
        print("3. Monthly Expense Analysis")
        print("4. Savings Trend")
        print("5. Top Spending Category")
        print("6. Daily Expense History")
        print("7. Financial Overview")
        print("8. Back")

        print("=" * 60)

        choice = input("Enter Choice : ").strip()

        if choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            return choice

        print("\n❌ Invalid Choice!")
def spending_by_category(username):

    _, expenses = get_user_expenses(username)

    if not expenses:
        print("\n❌ No Expense Records Found.")
        return

    category_totals = defaultdict(float)

    for expense in expenses:

        category = expense.get("category", "Other")

        category_totals[category] += expense["amount"]

    total_expense = sum(category_totals.values())

    print("\n" + "=" * 70)
    print("                💸 SPENDING BY CATEGORY")
    print("=" * 70)

    print(
        f"{'Category':<25}"
        f"{'Amount':<20}"
        f"{'Percentage':<15}"
    )

    print("-" * 70)

    for category, amount in sorted(
        category_totals.items(),
        key=lambda item: item[1],
        reverse=True
    ):

        percentage = (amount / total_expense) * 100

        print(
            f"{category:<25}"
            f"Rs.{amount:,.2f}     "
            f"{percentage:.2f}%"
        )

    print("-" * 70)
    print(f"Total Expense : Rs.{total_expense:,.2f}")

    print("=" * 70)
def monthly_income_analysis(username):

    _, incomes = get_user_incomes(username)

    if not incomes:
        print("\n❌ No Income Records Found.")
        return

    monthly_totals = defaultdict(float)

    for income in incomes:

        date_parts = income["date"].split("-")

        year = date_parts[0]
        month = date_parts[1]

        month_key = f"{year}-{month}"

        monthly_totals[month_key] += income["amount"]

    print("\n" + "=" * 60)
    print("              💰 MONTHLY INCOME")
    print("=" * 60)

    print(f"{'Month':<20}{'Income':<20}")
    print("-" * 60)

    for month, amount in sorted(monthly_totals.items()):

        print(
            f"{month:<20}"
            f"Rs.{amount:,.2f}"
        )

    print("=" * 60)
def monthly_expense_analysis(username):

    _, expenses = get_user_expenses(username)

    if not expenses:
        print("\n❌ No Expense Records Found.")
        return

    monthly_totals = defaultdict(float)

    for expense in expenses:

        date_parts = expense["date"].split("-")

        year = date_parts[0]
        month = date_parts[1]

        month_key = f"{year}-{month}"

        monthly_totals[month_key] += expense["amount"]

    print("\n" + "=" * 65)
    print("              💸 MONTHLY EXPENSE ANALYSIS")
    print("=" * 65)

    print(f"{'Month':<20}{'Total Expense':<25}")
    print("-" * 65)

    for month, amount in sorted(monthly_totals.items()):

        print(
            f"{month:<20}"
            f"Rs.{amount:,.2f}"
        )

    print("-" * 65)

    total_expense = sum(monthly_totals.values())

    print(f"Total Expense : Rs.{total_expense:,.2f}")

    print("=" * 65)
def savings_trend(username):

    _, incomes = get_user_incomes(username)
    _, expenses = get_user_expenses(username)

    if not incomes and not expenses:
        print("\n❌ No Financial Records Found.")
        return

    monthly_income = defaultdict(float)
    monthly_expense = defaultdict(float)

    for income in incomes:

        date_parts = income["date"].split("-")

        month_key = f"{date_parts[0]}-{date_parts[1]}"

        monthly_income[month_key] += income["amount"]

    for expense in expenses:

        date_parts = expense["date"].split("-")

        month_key = f"{date_parts[0]}-{date_parts[1]}"

        monthly_expense[month_key] += expense["amount"]

    months = sorted(
        set(monthly_income.keys()) |
        set(monthly_expense.keys())
    )

    print("\n" + "=" * 75)
    print("                 💰 SAVINGS TREND")
    print("=" * 75)

    print(
        f"{'Month':<15}"
        f"{'Income':<20}"
        f"{'Expense':<20}"
        f"{'Savings':<20}"
    )

    print("-" * 75)

    for month in months:

        income = monthly_income.get(month, 0)
        expense = monthly_expense.get(month, 0)

        savings = income - expense

        print(
            f"{month:<15}"
            f"Rs.{income:,.2f}      "
            f"Rs.{expense:,.2f}      "
            f"Rs.{savings:,.2f}"
        )

    print("=" * 75)
def top_spending_category(username):

    _, expenses = get_user_expenses(username)

    if not expenses:
        print("\n❌ No Expense Records Found.")
        return

    category_totals = defaultdict(float)

    for expense in expenses:

        category = expense.get("category", "Other")

        category_totals[category] += expense["amount"]

    top_category = max(
        category_totals,
        key=category_totals.get
    )

    top_amount = category_totals[top_category]

    total_expense = sum(category_totals.values())

    percentage = (
        top_amount / total_expense
    ) * 100

    print("\n" + "=" * 60)
    print("             🏆 TOP SPENDING CATEGORY")
    print("=" * 60)

    print(f"Category       : {top_category}")
    print(f"Amount         : Rs.{top_amount:,.2f}")
    print(f"Percentage     : {percentage:.2f}%")

    print("=" * 60)
def daily_expense_history(username):

    _, expenses = get_user_expenses(username)

    if not expenses:
        print("\n❌ No Expense Records Found.")
        return

    daily_totals = defaultdict(float)

    for expense in expenses:

        date = expense["date"]

        daily_totals[date] += expense["amount"]

    print("\n" + "=" * 65)
    print("              📅 DAILY EXPENSE HISTORY")
    print("=" * 65)

    print(
        f"{'Date':<20}"
        f"{'Total Expense':<20}"
    )

    print("-" * 65)

    for date, amount in sorted(
        daily_totals.items(),
        reverse=True
    ):

        print(
            f"{date:<20}"
            f"Rs.{amount:,.2f}"
        )

    print("=" * 65)
def financial_overview(username):

    _, incomes = get_user_incomes(username)
    _, expenses = get_user_expenses(username)

    total_income = sum(
        income["amount"] for income in incomes
    )

    total_expense = sum(
        expense["amount"] for expense in expenses
    )

    savings = total_income - total_expense

    income_count = len(incomes)
    expense_count = len(expenses)

    average_income = (
        total_income / income_count
        if income_count > 0
        else 0
    )

    average_expense = (
        total_expense / expense_count
        if expense_count > 0
        else 0
    )

    print("\n" + "=" * 65)
    print("               📊 FINANCIAL OVERVIEW")
    print("=" * 65)

    print(f"Total Income       : Rs.{total_income:,.2f}")
    print(f"Total Expense      : Rs.{total_expense:,.2f}")
    print(f"Total Savings      : Rs.{savings:,.2f}")

    print("-" * 65)

    print(f"Income Records     : {income_count}")
    print(f"Expense Records    : {expense_count}")

    print(f"Average Income     : Rs.{average_income:,.2f}")
    print(f"Average Expense    : Rs.{average_expense:,.2f}")

    print("-" * 65)

    if savings > 0:
        print("🟢 Financial Status : Positive")

    elif savings == 0:
        print("🟡 Financial Status : Balanced")

    else:
        print("🔴 Financial Status : Negative")

    print("=" * 65)