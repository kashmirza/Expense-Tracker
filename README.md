# 💰 Expense Tracker

A Python-based Expense Tracker application designed to help users manage their personal finances in an organized and efficient way.

The system allows users to manage income, expenses, budgets, financial reports, analytics, charts, CSV exports, and receipts through a simple menu-driven interface.

---

## 📌 Overview

The Expense Tracker provides a complete solution for recording and monitoring financial activities.

After creating an account and logging in, users can access a personalized dashboard where they can:

- Manage income
- Manage expenses
- Set and monitor budgets
- Generate financial reports
- Analyze financial data
- View financial charts
- Export data to CSV
- Upload and manage receipts

The application stores user records using JSON files and provides separate financial data for each logged-in user.

---

## ✨ Features

### 👤 Authentication

- User Registration
- User Login
- User Logout
- User-specific financial records

---

### 💵 Income Management

Users can manage their income through:

- Add Income
- View Income
- Update Income
- Delete Income
- Search Income
- Monthly Income Report
- Total Income

#### Income Categories

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

### 💸 Expense Management

Users can manage their expenses through:

- Add Expense
- View Expense
- Update Expense
- Delete Expense
- Search Expense
- Monthly Expense Report
- Total Expense

Expenses can be organized using different categories, making it easier to understand spending habits.

---

### 💰 Budget Management

The Budget Management module allows users to:

- Set Budget
- View Budget
- Update Budget
- Delete Budget
- Check Budget Status

This helps users monitor their spending against their planned budget.

---

### 📊 Reports

The Reports module provides useful financial summaries.

Available reports include:

- Financial Summary
- Monthly Report
- Income vs Expense
- Savings Report
- Highest Transactions

These reports help users understand their overall financial position.

---

### 📈 Analytics

The Analytics module provides detailed analysis of financial data.

Available analytics include:

- Spending by Category
- Monthly Income Analysis
- Monthly Expense Analysis
- Savings Trend
- Top Spending Category
- Daily Expense History
- Financial Overview

---

### 📉 Charts

The project uses **Matplotlib** for financial data visualization.

Available charts include:

- Income vs Expense Chart
- Expense Category Chart
- Monthly Savings Chart

Charts make financial information easier to understand visually.

---

### 📄 CSV Export

Users can export their financial information into CSV files.

Available exports include:

- Income CSV
- Expense CSV
- Financial Summary CSV

CSV files can be opened using spreadsheet applications such as Microsoft Excel.

---

### 🧾 Receipt Management

The Receipt Management module allows users to store and manage receipts.

Features include:

- Upload Receipt
- View My Receipts
- Search Receipt
- Delete Receipt

Supported receipt formats:

- JPG
- JPEG
- PNG
- PDF

Uploaded receipts are stored inside the `receipts` folder while their information is maintained in `receipts.json`.

---

## 🗂️ Project Structure

```text
Expense-Tracker/
│
├── main.py
│
├── auth.py
├── dashboard.py
│
├── income.py
├── expense.py
├── budget.py
├── reports.py
├── analytics.py
├── charts.py
├── csv_export.py
├── receipt.py
├── file_handler.py
│
├── income.json
├── expense.json
├── budget.json
├── receipts.json
│
├── receipts/
│
├── README.md
└── .gitignore


                         START
                           │
                           ▼
                    ┌─────────────┐
                    │ Main Menu   │
                    └─────────────┘
                       │    │    │
                 Register Login Exit
                       │
                       ▼
                  Login Success
                       │
                       ▼
                 ┌─────────────┐
                 │  Dashboard  │
                 └─────────────┘
                       │
       ┌───────────────┼────────────────┐
       │               │                │
       ▼               ▼                ▼
    Income          Expense           Budget
       │               │                │
       └───────────────┼────────────────┘
                       │
       ┌───────────────┼────────────────┐
       │               │                │
       ▼               ▼                ▼
    Reports         Analytics         Charts
       │               │                │
       └───────────────┼────────────────┘
                       │
                ┌──────┴──────┐
                ▼             ▼
           CSV Export     Receipts
                │             │
                └──────┬──────┘
                       ▼
                     Logout
                       │
                       ▼
                      END

🛠️ Technologies Used

The project is developed using:

Python
JSON
CSV
Matplotlib
Tkinter
OS Module
Shutil Module
Datetime Module

🧠 Python Concepts Used

This project demonstrates the following Python concepts:

Variables
Data Types
Conditional Statements
Loops
Functions
Lists
Dictionaries
Modules
Imports
File Handling
JSON Data Handling
CSV Data Handling
Exception Handling
Input Validation
Date and Time Handling
String Formatting
Data Analysis
Data Visualization
File Management

💾 Data Storage

The application uses JSON files to store financial records.

Example files:

income.json
expense.json
budget.json
receipts.json

Each record is associated with the logged-in username.

This allows different users to manage their own financial information separately.

Register
   ↓
Login
   ↓
Dashboard
   ↓
Add Income
   ↓
Add Expenses
   ↓
Set Budget
   ↓
Check Budget Status
   ↓
Generate Reports
   ↓
Analyze Spending
   ↓
View Charts
   ↓
Export CSV
   ↓
Upload Receipts
   ↓
Logout

Purpose of the Project

The main purpose of this project is to provide a simple financial management system while demonstrating practical Python programming concepts.

It combines:

User authentication
Financial record management
File handling
Data analysis
Data visualization
Report generation
CSV data export
Receipt management

into one complete application.

Future Improvements

The project can be further improved by adding:

SQLite or MySQL database
Password hashing
Graphical User Interface (GUI)
PDF financial reports
Recurring income and expenses
Expense reminders
Advanced financial forecasting
Cloud data synchronization
Mobile application
Improved dashboard with interactive chart

👩‍💻 Author

Kashmala Akram

Python Developer | Software Development | Financial Applications
