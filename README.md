# Step 5: Dockerize the App Using Vagrant

This branch adds Docker support to the Django Invoice Generator by running the containerized app inside a **Vagrant-managed Linux VM**.

## ✅ What Was Done

- Created `Dockerfile` and `docker-compose.yml`
- Added `.dockerignore` to exclude unnecessary files
- Switched back to `weasyprint` for PDF generation
- Used `Vagrant` to run Docker on a Linux VM
- Tested PDF generation in container
- Updated views and templates for compatibility

> 💡 Note: Docker Desktop is not available on this machine, so we use Vagrant with Ubuntu to run Docker and `weasyprint` (which requires Linux system libraries).

## 🧪 How to Run with Vagrant + Docker

1. Start the Vagrant VM:

   ```bash
   vagrant up

   ```

2. SSH into the VM:

   ```bash
   vagrant ssh

   ```

3. Build and run the Docker app:

   ```bash
   cd /vagrant
   sudo docker-compose up --build

   ```

4. Visit:  
   [http://127.0.0.1:8000/upload/](http://127.0.0.1:8000/upload/)
   - Upload a CSV or Excel file
   - Preview the parsed invoice data
   - Click "Download PDF" to download the pdf invoice

> You can take the csv sample file in root folder, the file is named test_invoice.csv to test it

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
│   │   ├── invoice_template_pdf.html
│   │   ├── new_invoice_template.html
│   │   ├── preview.html
│   │   └── upload.html
│   └── main/
│       ├── base.html
│       └── navbar.html
├── test_invoice.csv
├── tree_clean.txt
└── update_readme.py
```
