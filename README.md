# Step 4: Generate PDF Invoices

This branch adds PDF generation functionality to the Django Invoice Generator.

## ✅ What Was Done

- Created HTML invoice template
- Used `xhtml2pdf` to generate PDFs (Windows-friendly alternative to `weasyprint`)
- Added "Download PDF" button
- Styled invoice with CSS
- Passed invoice data from session to template

> 💡 Note: We're using `xhtml2pdf` for now because `weasyprint` requires native libraries that aren't available on Windows. We'll switch back to `weasyprint` in Step 5 when we dockerize the app.

## 🧪 How to Run

1. Activate virtual environment
2. Run migrations:
   ```bash
   python manage.py migrate
   ```

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
   - Click "Download PDF"

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
│   │   ├── invoice_template.html
│   │   ├── preview.html
│   │   └── upload.html
│   └── main/
│       ├── base.html
│       └── navbar.html
├── tree_clean.txt
└── update_readme.py
```
