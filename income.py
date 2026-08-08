from datetime import datetime
from file_handler import load_data, save_data

INCOME_FILE = "income.json"
def income_menu():

    while True:

        print("\n" + "=" * 60)
        print("               💵 INCOME MANAGEMENT")
        print("=" * 60)

        print("1. Add Income")
        print("2. View Income")
        print("3. Update Income")
        print("4. Delete Income")
        print("5. Search Income")
        print("6. Monthly Income Report")
        print("7. Total Income")
        print("8. Back")

        print("=" * 60)

        choice = input("Enter Choice : ")

        if choice in [str(i) for i in range(1, 9)]:
            return choice

        print("❌ Invalid Choice.")
def generate_income_id(incomes):

    if not incomes:
        return "INC001"

    last_id = incomes[-1]["id"]

    number = int(last_id[3:]) + 1

    return f"INC{number:03d}"
def get_user_incomes(username):

    incomes = load_data(INCOME_FILE)

    if not isinstance(incomes, list):
        incomes = []

    user_incomes = []

    for income in incomes:

        if income["username"] == username:
            user_incomes.append(income)

    return incomes, user_incomes
def display_income_table(user_incomes):

    if not user_incomes:

        print("\n❌ No Income Records Found.")
        return

    print("\n" + "=" * 115)

    print(f"{'No':<5}{'ID':<10}{'Category':<18}{'Source':<20}{'Amount':<15}{'Date':<15}")

    print("=" * 115)

    total = 0

    for i, income in enumerate(user_incomes, start=1):

        print(
            f"{i:<5}"
            f"{income['id']:<10}"
            f"{income['category']:<18}"
            f"{income['source']:<20}"
            f"Rs.{income['amount']:<12}"
            f"{income['date']:<15}"
        )

        total += income["amount"]

    print("=" * 115)

    print(f"Total Income : Rs.{total}")
def add_income(username):

    incomes, _ = get_user_incomes(username)

    print("\n" + "=" * 60)
    print("                  ADD INCOME")
    print("=" * 60)

    # Select Category First
    categories = {
        "1": "Job",
        "2": "Freelancing",
        "3": "Business",
        "4": "Investment",
        "5": "Gift",
        "6": "Other"
    }

    print("\nSelect Income Category")

    for key, value in categories.items():
        print(f"{key}. {value}")

    while True:

        choice = input("Choose Category : ")

        if choice in categories:
            category = categories[choice]
            break

        print("❌ Invalid Choice.")

    # Source
    source = input("\nIncome Source : ").strip()

    # Amount
    while True:

        try:

            amount = float(input("Amount : "))

            if amount <= 0:
                print("❌ Amount must be greater than zero.")
                continue

            break

        except ValueError:
            print("❌ Invalid Amount.")

    # Description
    description = input("Description : ").strip()

    now = datetime.now()

    income = {

        "id": generate_income_id(incomes),

        "username": username,

        "category": category,

        "source": source,

        "amount": amount,

        "description": description,

        "date": now.strftime("%Y-%m-%d"),

        "time": now.strftime("%I:%M %p")
    }

    incomes.append(income)

    save_data(INCOME_FILE, incomes)

    print("\n" + "=" * 60)
    print("          ✅ INCOME ADDED SUCCESSFULLY")
    print("=" * 60)

    print(f"Transaction ID : {income['id']}")
    print(f"Category       : {income['category']}")
    print(f"Source         : {income['source']}")
    print(f"Amount         : Rs.{income['amount']}")
    print(f"Date           : {income['date']}")
    print(f"Time           : {income['time']}")

    print("=" * 60)
def view_income(username):

    _, user_incomes = get_user_incomes(username)

    if not user_incomes:
        print("\n❌ No Income Records Found.")
        return

    print("\n")
    print("=" * 115)
    print(" " * 45 + "YOUR INCOME")
    print("=" * 115)

    display_income_table(user_incomes)
def update_income(username):

    incomes, user_incomes = get_user_incomes(username)

    if not user_incomes:
        print("\n❌ No Income Records Found.")
        return

    print("\n")
    print("=" * 115)
    print(" " * 45 + "UPDATE INCOME")
    print("=" * 115)

    display_income_table(user_incomes)

    while True:

        try:

            record = int(input("\nSelect Record Number : "))

            if 1 <= record <= len(user_incomes):
                break

            print("❌ Invalid Record Number.")

        except ValueError:
            print("❌ Enter Numbers Only.")

    income = user_incomes[record - 1]

    print("\nCurrent Details")
    print("-" * 40)
    print(f"Category    : {income['category']}")
    print(f"Source      : {income['source']}")
    print(f"Amount      : Rs.{income['amount']}")
    print(f"Description : {income['description']}")
    print("-" * 40)

    new_source = input("New Source (Enter to Skip): ").strip()

    categories = ["Job", "Freelancing", "Business", "Investment", "Gift", "Other"]

    print("\nCategories")

    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat}")

    category_choice = input("New Category (Enter to Skip): ").strip()

    while True:

        new_amount = input("New Amount (Enter to Skip): ").strip()

        if new_amount == "":
            break

        try:

            new_amount = float(new_amount)

            if new_amount <= 0:
                print("Amount must be greater than zero.")
                continue

            break

        except ValueError:

            print("Invalid Amount.")

    new_description = input("New Description (Enter to Skip): ").strip()

    if new_source:
        income["source"] = new_source

    if category_choice:

        if category_choice in ["1", "2", "3", "4", "5", "6"]:
            income["category"] = categories[int(category_choice) - 1]

    if new_amount != "":
        income["amount"] = new_amount

    if new_description:
        income["description"] = new_description

    save_data(INCOME_FILE, incomes)

    print("\n✅ Income Updated Successfully.")
def delete_income(username):

    incomes, user_incomes = get_user_incomes(username)

    if not user_incomes:
        print("\n❌ No Income Records Found.")
        return

    print("\n")
    print("=" * 115)
    print(" " * 45 + "DELETE INCOME")
    print("=" * 115)

    display_income_table(user_incomes)

    while True:

        try:

            record = int(input("\nSelect Record Number : "))

            if 1 <= record <= len(user_incomes):
                break

            print("❌ Invalid Record.")

        except ValueError:

            print("❌ Numbers Only.")

    income = user_incomes[record - 1]

    confirm = input(
        f"\nDelete '{income['source']}' (Rs.{income['amount']}) ? (Y/N): "
    ).strip().lower()

    if confirm == "y":

        incomes.remove(income)

        save_data(INCOME_FILE, incomes)

        print("\n✅ Income Deleted Successfully.")

    else:

        print("\nDelete Cancelled.")
def search_income(username):

    _, user_incomes = get_user_incomes(username)

    if not user_incomes:
        print("\n❌ No Income Records Found.")
        return

    while True:

        print("\n" + "=" * 60)
        print("                 SEARCH INCOME")
        print("=" * 60)

        print("1. Search by Source")
        print("2. Search by Category")
        print("3. Search by Date")
        print("4. Search by Amount")
        print("5. Back")

        print("=" * 60)

        choice = input("Enter Choice : ")

        if choice == "1":

            key = input("Source : ").lower()

            result = [
                i for i in user_incomes
                if key in i["source"].lower()
            ]

        elif choice == "2":

            key = input("Category : ").lower()

            result = [
                i for i in user_incomes
                if key == i["category"].lower()
            ]

        elif choice == "3":

            key = input("Date (YYYY-MM-DD): ")

            result = [
                i for i in user_incomes
                if key == i["date"]
            ]

        elif choice == "4":

            try:

                amount = float(input("Amount : "))

                result = [
                    i for i in user_incomes
                    if i["amount"] == amount
                ]

            except ValueError:

                print("Invalid Amount.")
                continue

        elif choice == "5":

            return

        else:

            print("Invalid Choice.")
            continue

        if not result:

            print("\n❌ No Matching Records Found.")

        else:

            display_income_table(result)

from collections import defaultdict


def monthly_income_report(username):

    _, user_incomes = get_user_incomes(username)

    if not user_incomes:
        print("\n❌ No Income Records Found.")
        return

    month = input("\nEnter Month (MM): ").strip()
    year = input("Enter Year (YYYY): ").strip()

    monthly_records = []

    for income in user_incomes:

        date = income["date"].split("-")

        if date[0] == year and date[1] == month:
            monthly_records.append(income)

    if not monthly_records:
        print("\n❌ No Income Found For This Month.")
        return

    total_income = 0

    highest_income = monthly_records[0]

    category_summary = defaultdict(float)

    for income in monthly_records:

        total_income += income["amount"]

        category_summary[income["category"]] += income["amount"]

        if income["amount"] > highest_income["amount"]:
            highest_income = income

    average = total_income / len(monthly_records)

    print("\n" + "=" * 60)
    print("              MONTHLY INCOME REPORT")
    print("=" * 60)

    print(f"Month                : {month}/{year}")
    print(f"Total Transactions   : {len(monthly_records)}")
    print(f"Total Income         : Rs.{total_income:,.2f}")
    print(f"Highest Income       : {highest_income['source']} (Rs.{highest_income['amount']:,.2f})")
    print(f"Average Income       : Rs.{average:,.2f}")

    print("\nCategory Summary")
    print("-" * 40)

    for category, amount in category_summary.items():
        print(f"{category:<20} Rs.{amount:,.2f}")

    print("=" * 60)

def total_income(username):

    _, user_incomes = get_user_incomes(username)

    if not user_incomes:
        print("\n❌ No Income Records Found.")
        return

    total = sum(income["amount"] for income in user_incomes)

    highest = max(user_incomes, key=lambda x: x["amount"])

    lowest = min(user_incomes, key=lambda x: x["amount"])

    average = total / len(user_incomes)

    print("\n" + "=" * 60)
    print("               TOTAL INCOME SUMMARY")
    print("=" * 60)

    print(f"Total Transactions : {len(user_incomes)}")
    print(f"Total Income       : Rs.{total:,.2f}")
    print(f"Average Income     : Rs.{average:,.2f}")
    print(f"Highest Income     : {highest['source']} (Rs.{highest['amount']:,.2f})")
    print(f"Lowest Income      : {lowest['source']} (Rs.{lowest['amount']:,.2f})")

    print("=" * 60)