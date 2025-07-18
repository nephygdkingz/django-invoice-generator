# Step 3: Upload and Process CSV/Excel Files

This branch adds CSV and Excel file upload functionality to the Django Invoice Generator.

## ✅ What Was Done

- Created upload form for CSV/Excel files
- Used `pandas` to parse file contents
- Added file validation
- Displayed parsed invoice data in a table
- Used Django sessions to pass data between views

## 🧪 How to Run

1. Activate virtual environment
2. Run migrations:
   ```bash
   python manage.py migrate
   ```
3. Run the server:

   ```bash
   python manage.py runserver
   ```

4. Visit:  
   [http://127.0.0.1:8000/upload/](http://127.0.0.1:8000/upload/)
   - Upload a CSV or Excel file
   - Preview the parsed invoice data

## 📁 Project Structure

```
invoice_generator/
├── .gitignore
├── .prettierignore
├── README.md
├── account/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── generate_tree.py
├── invoice_generator/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── invoices/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
├── static/
│   └── assets/
│       ├── bootstrap/
│       │   ├── bootstrap.min.css
│       │   └── bootstrap.min.js
│       ├── css/
│       │   └── style.css
│       ├── images/
│       └── js/
│           └── main.js
├── templates/
│   ├── account/
│   │   └── dashboard.html
│   ├── authentication/
│   │   ├── login.html
│   │   └── register.html
│   ├── includes/
│   │   ├── form_errors.html
│   │   └── messages.html
│   ├── invoices/
│   │   ├── preview.html
│   │   └── upload.html
│   └── main/
│       ├── base.html
│       └── navbar.html
├── tree_clean.txt
└── update_readme.py
```
