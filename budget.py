from file_handler import load_data, save_data
from expense import get_user_expenses

BUDGET_FILE = "budget.json"
def budget_menu():

    while True:

        print("\n" + "=" * 60)
        print("             💰 BUDGET MANAGEMENT")
        print("=" * 60)

        print("1. Set Budget")
        print("2. View Budget")
        print("3. Update Budget")
        print("4. Delete Budget")
        print("5. Budget Status")
        print("6. Back")

        print("=" * 60)

        choice = input("Enter Choice : ")

        if choice in ["1", "2", "3", "4", "5", "6"]:
            return choice

        print("❌ Invalid Choice.")
def get_user_budget(username):

    budgets = load_data(BUDGET_FILE)

    if not isinstance(budgets, list):
        budgets = []

    for budget in budgets:

        if budget["username"] == username:
            return budgets, budget

    return budgets, None
def set_budget(username):

    budgets, budget = get_user_budget(username)

    if budget:

        print("\n❌ Budget already exists.")
        print("Use Update Budget.")
        return

    while True:

        try:

            amount = float(input("\nEnter Monthly Budget : Rs."))

            if amount <= 0:
                print("❌ Budget must be greater than zero.")
                continue

            break

        except ValueError:

            print("❌ Invalid Amount.")

    budgets.append({

        "username": username,

        "budget": amount

    })

    save_data(BUDGET_FILE, budgets)

    print("\n✅ Budget Set Successfully.")
def view_budget(username):

    _, budget = get_user_budget(username)

    if not budget:

        print("\n❌ No Budget Found.")
        return

    print("\n" + "=" * 50)
    print("             YOUR BUDGET")
    print("=" * 50)

    print(f"Monthly Budget : Rs.{budget['budget']:,.2f}")

    print("=" * 50)
def update_budget(username):

    budgets, budget = get_user_budget(username)

    if not budget:

        print("\n❌ No Budget Found.")
        return

    print(f"\nCurrent Budget : Rs.{budget['budget']:,.2f}")

    while True:

        try:

            new_budget = float(input("New Budget : Rs."))

            if new_budget <= 0:
                print("❌ Budget must be greater than zero.")
                continue

            break

        except ValueError:

            print("❌ Invalid Amount.")

    budget["budget"] = new_budget

    save_data(BUDGET_FILE, budgets)

    print("\n✅ Budget Updated Successfully.")
def delete_budget(username):

    budgets, budget = get_user_budget(username)

    if not budget:

        print("\n❌ No Budget Found.")
        return

    confirm = input("\nDelete Budget? (Y/N): ").lower()

    if confirm == "y":

        budgets.remove(budget)

        save_data(BUDGET_FILE, budgets)

        print("\n✅ Budget Deleted Successfully.")

    else:

        print("\nDelete Cancelled.")




def budget_status(username):

    _, budget = get_user_budget(username)

    if not budget:

        print("\n❌ No Budget Set.")
        return

    _, expenses = get_user_expenses(username)

    total_expense = sum(expense["amount"] for expense in expenses)

    remaining = budget["budget"] - total_expense

    percentage = (total_expense / budget["budget"]) * 100

    print("\n" + "=" * 60)
    print("              BUDGET STATUS")
    print("=" * 60)

    print(f"Budget           : Rs.{budget['budget']:,.2f}")
    print(f"Spent            : Rs.{total_expense:,.2f}")
    print(f"Remaining        : Rs.{remaining:,.2f}")
    print(f"Used             : {percentage:.2f}%")

    print("-" * 60)

    if percentage >= 100:

        print("🔴 Budget Exceeded!")

    elif percentage >= 90:

        print("🟠 Warning! Budget almost finished.")

    elif percentage >= 80:

        print("🟡 You have used 80% of your budget.")

    else:

        print("🟢 Budget is Healthy.")

    print("=" * 60)