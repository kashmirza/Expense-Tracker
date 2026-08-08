from auth import register, login
from dashboard import dashboard

# ======================= INCOME MODULE =======================

from income import (
    income_menu,
    add_income,
    view_income,
    update_income,
    delete_income,
    search_income,
    monthly_income_report,
    total_income
)

# ======================= EXPENSE MODULE =======================

from expense import (
    expense_menu,
    add_expense,
    view_expense,
    update_expense,
    delete_expense,
    search_expense,
    monthly_expense_report,
    total_expense
)

# ======================= BUDGET MODULE =======================

from budget import (
    budget_menu,
    set_budget,
    view_budget,
    update_budget,
    delete_budget,
    budget_status
)

# ======================= REPORTS MODULE =======================

from reports import (
    reports_menu,
    financial_summary,
    monthly_report,
    income_vs_expense,
    savings_report,
    highest_transactions
)

# ======================= ANALYTICS MODULE =======================

from analytics import (
    analytics_menu,
    spending_by_category,
    monthly_income_analysis,
    monthly_expense_analysis,
    savings_trend,
    top_spending_category,
    daily_expense_history,
    financial_overview
)

# ======================= CHARTS MODULE =======================

from charts import (
    charts_menu,
    income_vs_expense_chart,
    expense_category_chart,
    monthly_savings_chart
)

# ======================= CSV EXPORT MODULE =======================

from export import (
    csv_export_menu,
    export_income_csv,
    export_expense_csv,
    export_financial_summary_csv
)
# ======================= RECEIPT MODULE =======================

from receipt import (
    receipt_management
)

# ==========================================================
#                      MAIN PROGRAM
# ==========================================================

while True:

    print("\n" + "=" * 55)
    print("              💰 EXPENSE TRACKER")
    print("=" * 55)

    print("1. Register")
    print("2. Login")
    print("3. Exit")

    print("=" * 55)

    choice = input("Enter your choice: ").strip()


    # ======================================================
    #                      REGISTER
    # ======================================================

    if choice == "1":

        register()


    # ======================================================
    #                        LOGIN
    # ======================================================

    elif choice == "2":

        username = login()

        if username:

            while True:

                option = dashboard(username)


                # ==================================================
                #                 INCOME MANAGEMENT
                # ==================================================

                if option == "1":

                    while True:

                        income_choice = income_menu()

                        if income_choice == "1":
                            add_income(username)

                        elif income_choice == "2":
                            view_income(username)

                        elif income_choice == "3":
                            update_income(username)

                        elif income_choice == "4":
                            delete_income(username)

                        elif income_choice == "5":
                            search_income(username)

                        elif income_choice == "6":
                            monthly_income_report(username)

                        elif income_choice == "7":
                            total_income(username)

                        elif income_choice == "8":
                            break

                        else:
                            print("\n❌ Invalid Choice!")


                # ==================================================
                #                 EXPENSE MANAGEMENT
                # ==================================================

                elif option == "2":

                    while True:

                        expense_choice = expense_menu()

                        if expense_choice == "1":
                            add_expense(username)

                        elif expense_choice == "2":
                            view_expense(username)

                        elif expense_choice == "3":
                            update_expense(username)

                        elif expense_choice == "4":
                            delete_expense(username)

                        elif expense_choice == "5":
                            search_expense(username)

                        elif expense_choice == "6":
                            monthly_expense_report(username)

                        elif expense_choice == "7":
                            total_expense(username)

                        elif expense_choice == "8":
                            break

                        else:
                            print("\n❌ Invalid Choice!")


                # ==================================================
                #                 BUDGET MANAGEMENT
                # ==================================================

                elif option == "3":

                    while True:

                        budget_choice = budget_menu()

                        if budget_choice == "1":
                            set_budget(username)

                        elif budget_choice == "2":
                            view_budget(username)

                        elif budget_choice == "3":
                            update_budget(username)

                        elif budget_choice == "4":
                            delete_budget(username)

                        elif budget_choice == "5":
                            budget_status(username)

                        elif budget_choice == "6":
                            break

                        else:
                            print("\n❌ Invalid Choice!")


                # ==================================================
                #                       REPORTS
                # ==================================================

                elif option == "4":

                    while True:

                        report_choice = reports_menu()

                        if report_choice == "1":
                            financial_summary(username)

                        elif report_choice == "2":
                            monthly_report(username)

                        elif report_choice == "3":
                            income_vs_expense(username)

                        elif report_choice == "4":
                            savings_report(username)

                        elif report_choice == "5":
                            highest_transactions(username)

                        elif report_choice == "6":
                            break

                        else:
                            print("\n❌ Invalid Choice!")


                # ==================================================
                #                      ANALYTICS
                # ==================================================

                elif option == "5":

                    while True:

                        analytics_choice = analytics_menu()

                        if analytics_choice == "1":
                            spending_by_category(username)

                        elif analytics_choice == "2":
                            monthly_income_analysis(username)

                        elif analytics_choice == "3":
                            monthly_expense_analysis(username)

                        elif analytics_choice == "4":
                            savings_trend(username)

                        elif analytics_choice == "5":
                            top_spending_category(username)

                        elif analytics_choice == "6":
                            daily_expense_history(username)

                        elif analytics_choice == "7":
                            financial_overview(username)

                        elif analytics_choice == "8":
                            break

                        else:
                            print("\n❌ Invalid Choice!")


                # ==================================================
                #                       CHARTS
                # ==================================================

                elif option == "6":

                    while True:

                        chart_choice = charts_menu()

                        if chart_choice == "1":
                            income_vs_expense_chart(username)

                        elif chart_choice == "2":
                            expense_category_chart(username)

                        elif chart_choice == "3":
                            monthly_savings_chart(username)

                        elif chart_choice == "4":
                            break

                        else:
                            print("\n❌ Invalid Choice!")


                # ==================================================
                #                    EXPORT CSV
                # ==================================================

                elif option == "7":

                    while True:

                        csv_choice = csv_export_menu()

                        if csv_choice == "1":
                            export_income_csv(username)

                        elif csv_choice == "2":
                            export_expense_csv(username)

                        elif csv_choice == "3":
                            export_financial_summary_csv(username)

                        elif csv_choice == "4":
                            break

                        else:
                            print("\n❌ Invalid Choice!")


                # ==================================================
                #                   RECEIPT UPLOAD
                # ==================================================

                elif option == "8":

                   receipt_management(username)


                # ==================================================
                #                        LOGOUT
                # ==================================================

                elif option == "9":

                    print("\n" + "=" * 55)
                    print("       ✅ LOGGED OUT SUCCESSFULLY")
                    print("=" * 55)

                    break


                # ==================================================
                #                INVALID DASHBOARD CHOICE
                # ==================================================

                else:

                    print("\n❌ Invalid Choice!")


    # ======================================================
    #                         EXIT
    # ======================================================

    elif choice == "3":

        print("\n" + "=" * 55)
        print("     👋 THANK YOU FOR USING EXPENSE TRACKER")
        print("              Have a Nice Day 😊")
        print("=" * 55)

        break


    # ======================================================
    #                  INVALID MAIN CHOICE
    # ======================================================

    else:

        print("\n❌ Invalid Choice!")