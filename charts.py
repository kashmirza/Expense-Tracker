import matplotlib.pyplot as plt
from collections import defaultdict

from income import get_user_incomes
from expense import get_user_expenses


# ==========================================================
#                  CHARTS MENU
# ==========================================================

def charts_menu():

    while True:

        print("\n" + "=" * 60)
        print("                    📊 CHARTS")
        print("=" * 60)

        print("1. Income vs Expense")
        print("2. Expense by Category")
        print("3. Monthly Savings Trend")
        print("4. Back")

        print("=" * 60)

        choice = input("Enter Choice : ").strip()

        if choice in ["1", "2", "3", "4"]:
            return choice

        print("\n❌ Invalid Choice!")


# ==========================================================
#                INCOME VS EXPENSE CHART
# ==========================================================

def income_vs_expense_chart(username):

    _, incomes = get_user_incomes(username)
    _, expenses = get_user_expenses(username)

    total_income = sum(
        income["amount"]
        for income in incomes
    )

    total_expense = sum(
        expense["amount"]
        for expense in expenses
    )

    if total_income == 0 and total_expense == 0:

        print("\n❌ No financial data available.")
        return

    labels = ["Income", "Expense"]
    values = [total_income, total_expense]

    plt.figure(figsize=(8, 5))

    plt.bar(labels, values)

    plt.title("Income vs Expense")
    plt.xlabel("Financial Type")
    plt.ylabel("Amount (Rs.)")

    plt.tight_layout()

    plt.show()


# ==========================================================
#                EXPENSE CATEGORY PIE CHART
# ==========================================================

def expense_category_chart(username):

    _, expenses = get_user_expenses(username)

    if not expenses:

        print("\n❌ No Expense Records Found.")
        return

    category_totals = defaultdict(float)

    for expense in expenses:

        category = expense.get(
            "category",
            "Other"
        )

        category_totals[category] += expense["amount"]

    labels = list(category_totals.keys())
    values = list(category_totals.values())

    plt.figure(figsize=(8, 8))

    plt.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Expense by Category")

    plt.tight_layout()

    plt.show()


# ==========================================================
#                MONTHLY SAVINGS TREND
# ==========================================================

def monthly_savings_chart(username):

    _, incomes = get_user_incomes(username)
    _, expenses = get_user_expenses(username)

    monthly_income = defaultdict(float)
    monthly_expense = defaultdict(float)

    for income in incomes:

        date_parts = income["date"].split("-")

        month_key = (
            f"{date_parts[0]}-{date_parts[1]}"
        )

        monthly_income[month_key] += income["amount"]

    for expense in expenses:

        date_parts = expense["date"].split("-")

        month_key = (
            f"{date_parts[0]}-{date_parts[1]}"
        )

        monthly_expense[month_key] += expense["amount"]

    months = sorted(
        set(monthly_income.keys()) |
        set(monthly_expense.keys())
    )

    if not months:

        print("\n❌ No financial data available.")
        return

    savings = []

    for month in months:

        income = monthly_income.get(
            month,
            0
        )

        expense = monthly_expense.get(
            month,
            0
        )

        savings.append(
            income - expense
        )

    plt.figure(figsize=(9, 5))

    plt.plot(
        months,
        savings,
        marker="o"
    )

    plt.title("Monthly Savings Trend")
    plt.xlabel("Month")
    plt.ylabel("Savings (Rs.)")

    plt.xticks(
        rotation=45
    )

    plt.axhline(
        y=0,
        linestyle="--"
    )

    plt.tight_layout()

    plt.show()