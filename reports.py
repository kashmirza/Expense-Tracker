from income import get_user_incomes
from expense import get_user_expenses
from budget import get_user_budget
def reports_menu():

    while True:

        print("\n" + "=" * 60)
        print("               📊 REPORTS")
        print("=" * 60)

        print("1. Financial Summary")
        print("2. Monthly Report")
        print("3. Income vs Expense")
        print("4. Savings Report")
        print("5. Highest Transactions")
        print("6. Back")

        print("=" * 60)

        choice = input("Enter Choice : ")

        if choice in ["1", "2", "3", "4", "5", "6"]:
            return choice

        print("❌ Invalid Choice.")

def financial_summary(username):

    _, incomes = get_user_incomes(username)
    _, expenses = get_user_expenses(username)
    _, budget = get_user_budget(username)

    total_income = sum(item["amount"] for item in incomes)
    total_expense = sum(item["amount"] for item in expenses)

    savings = total_income - total_expense

    if budget:
        budget_amount = budget["budget"]
        remaining = budget_amount - total_expense
    else:
        budget_amount = 0
        remaining = 0

    print("\n" + "=" * 60)
    print("          📊 FINANCIAL SUMMARY")
    print("=" * 60)

    print(f"Total Income      : Rs.{total_income:,.2f}")
    print(f"Total Expense     : Rs.{total_expense:,.2f}")
    print(f"Total Savings     : Rs.{savings:,.2f}")
    print(f"Monthly Budget    : Rs.{budget_amount:,.2f}")
    print(f"Remaining Budget  : Rs.{remaining:,.2f}")

    print("=" * 60)

def monthly_report(username):

    _, incomes = get_user_incomes(username)
    _, expenses = get_user_expenses(username)

    month = input("\nEnter Month (MM): ").strip()
    year = input("Enter Year (YYYY): ").strip()

    income_total = 0
    expense_total = 0

    for income in incomes:

        date = income["date"].split("-")

        if date[0] == year and date[1] == month:
            income_total += income["amount"]

    for expense in expenses:

        date = expense["date"].split("-")

        if date[0] == year and date[1] == month:
            expense_total += expense["amount"]

    savings = income_total - expense_total

    print("\n" + "=" * 60)
    print("             MONTHLY REPORT")
    print("=" * 60)

    print(f"Month          : {month}/{year}")
    print(f"Income         : Rs.{income_total:,.2f}")
    print(f"Expense        : Rs.{expense_total:,.2f}")
    print(f"Savings        : Rs.{savings:,.2f}")

    print("=" * 60)

def income_vs_expense(username):

    _, incomes = get_user_incomes(username)
    _, expenses = get_user_expenses(username)

    total_income = sum(item["amount"] for item in incomes)
    total_expense = sum(item["amount"] for item in expenses)

    difference = total_income - total_expense

    print("\n" + "=" * 60)
    print("         INCOME VS EXPENSE")
    print("=" * 60)

    print(f"Total Income   : Rs.{total_income:,.2f}")
    print(f"Total Expense  : Rs.{total_expense:,.2f}")
    print(f"Difference     : Rs.{difference:,.2f}")

    if difference > 0:
        print("\n🟢 Great! You are saving money.")

    elif difference == 0:
        print("\n🟡 Income and Expense are Equal.")

    else:
        print("\n🔴 Warning! Expenses are greater than Income.")

    print("=" * 60)
def savings_report(username):

    _, incomes = get_user_incomes(username)
    _, expenses = get_user_expenses(username)

    total_income = sum(
        income["amount"] for income in incomes
    )

    total_expense = sum(
        expense["amount"] for expense in expenses
    )

    savings = total_income - total_expense

    print("\n" + "=" * 60)
    print("                 💰 SAVINGS REPORT")
    print("=" * 60)

    print(f"Total Income      : Rs.{total_income:,.2f}")
    print(f"Total Expense     : Rs.{total_expense:,.2f}")
    print("-" * 60)
    print(f"Total Savings     : Rs.{savings:,.2f}")

    if total_income > 0:

        savings_percentage = (
            savings / total_income
        ) * 100

        print(
            f"Savings Percentage: {savings_percentage:.2f}%"
        )

    else:

        print("Savings Percentage: 0.00%")

    print("-" * 60)

    if savings > 0:

        print("🟢 You are saving money. Great job!")

    elif savings == 0:

        print("🟡 Your income and expenses are equal.")

    else:

        print("🔴 Your expenses are greater than your income.")

    print("=" * 60)
def highest_transactions(username):

    _, incomes = get_user_incomes(username)
    _, expenses = get_user_expenses(username)

    print("\n" + "=" * 60)
    print("            🏆 HIGHEST TRANSACTIONS")
    print("=" * 60)

    # ---------------- Highest Income ----------------

    if incomes:

        highest_income = max(
            incomes,
            key=lambda income: income["amount"]
        )

        print("\n💰 HIGHEST INCOME")
        print("-" * 40)

        print(f"ID          : {highest_income['id']}")
        print(f"Category    : {highest_income['category']}")
        print(f"Source      : {highest_income['source']}")
        print(f"Amount      : Rs.{highest_income['amount']:,.2f}")
        print(f"Date        : {highest_income['date']}")

    else:

        print("\n❌ No Income Records Found.")

    # ---------------- Highest Expense ----------------

    if expenses:

        highest_expense = max(
            expenses,
            key=lambda expense: expense["amount"]
        )

        print("\n💸 HIGHEST EXPENSE")
        print("-" * 40)

        print(f"ID          : {highest_expense['id']}")
        print(f"Category    : {highest_expense['category']}")
        print(f"Title       : {highest_expense['title']}")
        print(f"Amount      : Rs.{highest_expense['amount']:,.2f}")
        print(f"Date        : {highest_expense['date']}")

    else:

        print("\n❌ No Expense Records Found.")

    print("=" * 60)