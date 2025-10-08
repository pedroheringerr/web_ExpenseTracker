# Web Expense Tracker in Django
A simple yet powerful web application built with Django to help you track your personal expenses.
This application allows users to log, view, filter, and manage their financial transactions with ease.

## Features
- **Dashboard View:** See your current balance based on all logged transactions.
- **Add & Delete Expenses:** Easily add new expenses and remove incorrect entries.
- **Filtering:**
    - by **category**
    - by **description**
    - by **date**
- **Dynamic Balance:** The balance card updates automatically to reflect the sum of the filtered transactions.
- **Export:** Export your expense data to `.csv` and `.xlsx` (Excel) formats for offline analysis or record-keeping.

## Technology Stack
- **Backend:** Python, Django
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS
- **Libraries:**
    - `psycopg2-binary`: PostgreSQL adapter for Python.
    - `openpyxl`: For generating `.xlsx` Excel files.
    - `django-environ`: For managing environment variables.
