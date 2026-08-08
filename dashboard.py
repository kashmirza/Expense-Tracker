def dashboard(username):

    while True:

        print("\n" + "=" * 60)
        print("           💰 EXPENSE TRACKER DASHBOARD")
        print("=" * 60)
        print(f"👤 Logged in as : {username.title()}")
        print("=" * 60)

        print("1. Income Management")
        print("2. Expense Management")
        print("3. Budget Management")
        print("4. Reports")
        print("5. Analytics")
        print("6. Charts")
        print("7. Export CSV")
        print("8. Receipt Upload")
        print("9. Logout")

        print("=" * 60)

        choice = input("Enter your choice: ")

        if choice in ["1","2","3","4","5","6","7","8","9"]:
            return choice

        print("❌ Invalid Choice! Please try again.")
def income_menu():

    while True:

        print("\n" + "=" * 60)
        print("              💵 INCOME MANAGEMENT")
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

        choice = input("Enter your choice: ")

        if choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            return choice

        print("❌ Invalid Choice!")