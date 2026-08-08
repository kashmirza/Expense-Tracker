# 💰 Expense Tracker

A complete **Python-based Expense Tracker and Personal Financial Management System** designed to help users manage their income, expenses, budgets, financial reports, analytics, charts, CSV exports, and receipts from one application.

The project is built using Python and demonstrates practical programming concepts such as functions, modules, file handling, JSON, CSV, data analysis, data visualization, exception handling, and file management.

---

## 📌 Project Overview

The **Expense Tracker** allows users to securely manage their personal financial records after registering and logging into the system.

After login, users are provided with a dashboard containing different financial management modules:

- 💵 Income Management
- 💸 Expense Management
- 💰 Budget Management
- 📊 Reports
- 📈 Analytics
- 📉 Charts
- 📄 CSV Export
- 🧾 Receipt Upload

Each user's financial records are linked with their username, allowing users to manage their own data separately.

---

# ✨ Features

## 👤 User Authentication

The application provides a basic authentication system.

Users can:

- Register an account
- Login to the application
- Access their personal dashboard
- Logout from the system

---

## 💵 Income Management

The Income Management module allows users to manage their income records.

### Available Features

- Add Income
- View Income
- Update Income
- Delete Income
- Search Income
- Monthly Income Report
- Total Income

### Income Categories

Users can categorize their income into different categories:

- Job
- Freelancing
- Business
- Investment
- Gift
- Other

Each income record contains information such as:

- Income ID
- Username
- Category
- Source
- Amount
- Description
- Date
- Time

---

## 💸 Expense Management

The Expense Management module allows users to keep track of their spending.

### Available Features

- Add Expense
- View Expense
- Update Expense
- Delete Expense
- Search Expense
- Monthly Expense Report
- Total Expense

Expenses can be organized according to different categories, making it easier to understand spending behavior.

---

## 💰 Budget Management

The Budget Management module helps users control their spending by setting financial budgets.

### Available Features

- Set Budget
- View Budget
- Update Budget
- Delete Budget
- Check Budget Status

The budget status helps users understand how much of their allocated budget has been used.

---

# 📊 Reports

The Reports module provides useful financial summaries based on the user's income and expenses.

### Available Reports

- Financial Summary
- Monthly Report
- Income vs Expense
- Savings Report
- Highest Transactions

These reports help users understand their overall financial position.

---

# 📈 Analytics

The Analytics module provides more detailed analysis of financial data.

### Available Analytics

- Spending by Category
- Monthly Income Analysis
- Monthly Expense Analysis
- Savings Trend
- Top Spending Category
- Daily Expense History
- Financial Overview

Analytics help users identify spending patterns and understand their financial behavior.

---

# 📉 Charts

The project uses **Matplotlib** for data visualization.

### Available Charts

- Income vs Expense Chart
- Expense Category Chart
- Monthly Savings Chart

Charts provide a visual representation of financial information and make it easier to understand trends.

---

# 📄 CSV Export

The CSV Export module allows users to export their financial data into CSV files.

### Available Exports

- Income CSV
- Expense CSV
- Financial Summary CSV

CSV files can be opened using spreadsheet applications such as Microsoft Excel or Google Sheets.

---

# 🧾 Receipt Management

The Receipt Management module allows users to store and manage digital receipts.

### Available Features

- Upload Receipt
- View My Receipts
- Search Receipt
- Delete Receipt

### Supported Receipt Formats

- JPG
- JPEG
- PNG
- PDF

When a receipt is uploaded:

1. The user selects a receipt file.
2. The system validates the file type.
3. A unique Receipt ID is generated.
4. The receipt is copied into the project's receipt folder.
5. Receipt information is stored in `receipts.json`.

---

# 🛠️ Technologies Used

The project is developed using:

- **Python**
- **JSON**
- **CSV**
- **Matplotlib**
- **Tkinter**
- **OS Module**
- **Shutil Module**
- **Datetime Module**

---

# 🧠 Python Concepts Used

This project demonstrates the following Python programming concepts:

- Variables
- Data Types
- Conditional Statements
- Loops
- Functions
- Lists
- Dictionaries
- Modules
- Imports
- File Handling
- JSON Data Handling
- CSV Data Handling
- Exception Handling
- Input Validation
- Date and Time Handling
- String Formatting
- Data Analysis
- Data Visualization
- File Management

---
# 📦 Requirements

The project requires:

- **Python 3.x**
- **Matplotlib**
- **Tkinter**

Tkinter is generally included with standard Python installations on Windows.

---

# 🧪 Input Validation

The application includes input validation to prevent invalid data.

Examples include:

- Checking invalid menu choices
- Validating numerical amounts
- Preventing negative income
- Preventing negative expenses
- Handling invalid numeric input
- Checking receipt file types
- Checking whether files exist
- Handling empty search values

---

# 🎯 Purpose of the Project

The main purpose of this project is to build a practical financial management application while applying Python programming concepts in a real-world project.

The project combines:

- **User Authentication**
- **Income Management**
- **Expense Management**
- **Budget Management**
- **Financial Reports**
- **Financial Analytics**
- **Data Visualization**
- **CSV Export**
- **Receipt Management**
- **File Handling**

into one complete application.

---

# 🎓 Learning Outcomes

Through this project, the following practical skills are demonstrated:

- Designing a modular Python application
- Creating reusable functions
- Working with multiple Python modules
- Reading and writing JSON files
- Working with CSV files
- Managing files and folders
- Validating user input
- Handling exceptions
- Performing financial calculations
- Analyzing financial data
- Creating charts with Matplotlib
- Building a menu-driven application
- Using Git and GitHub for project management

---

# 🔮 Future Improvements

The project can be further improved by adding:

- SQLite Database
- MySQL Database
- Secure Password Hashing
- Graphical User Interface (GUI)
- PDF Financial Reports
- Recurring Income and Expenses
- Expense Reminders
- Advanced Financial Forecasting
- Cloud Data Synchronization
- Mobile Application
- Interactive Dashboard
- Advanced Budget Notifications
- Better Authentication and Security
- Database Backup and Restore
- More Advanced Financial Charts

---

# 🔒 Security Improvements

For a production-level application, additional security features could be implemented, including:

- Password Hashing
- Secure Authentication
- Database-Based User Management
- Session Management
- Input Sanitization
- Secure File Handling
- Access Control

---

# 📌 Project Status

🚧 **Active Development**

The core financial management features have been implemented, including:

- Income Management
- Expense Management
- Budget Management
- Financial Reports
- Analytics
- Charts
- CSV Export
- Receipt Management

Additional improvements and features can be added in future versions.

---

# 👩‍💻 Author

## Kashmala Akram

**Python Developer | Software Development | Financial Applications**

# 💾 Data Storage

The application uses **JSON files** for storing financial information.

Example data files:

```text
income.json
expense.json
budget.json
receipts.json

Expense-Tracker/
│
├── main.py
├── auth.py
├── dashboard.py
├── file_handler.py
│
├── income.py
├── expense.py
├── budget.py
├── reports.py
├── analytics.py
├── charts.py
├── csv_export.py
├── receipt.py
│
├── income.json
├── expense.json
├── budget.json
├── receipts.json
│
├── receipts/
│
├── README.md
└── ...

Register
   ↓
Login
   ↓
Dashboard
   ↓
┌─────────────────────────┐
│    Expense Tracker      │
└─────────────────────────┘
   ↓
Income Management
   ↓
Expense Management
   ↓
Budget Management
   ↓
Reports
   ↓
Analytics
   ↓
Charts
   ↓
CSV Export
   ↓
Receipt Upload
   ↓
Logout

1. Income Management
2. Expense Management
3. Budget Management
4. Reports
5. Analytics
6. Charts
7. Export CSV
8. Receipt Upload
9. Logout

