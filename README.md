# Step 8: Add Invoice History & Prepare for Deployment

This branch adds persistent storage for generated invoices and prepares the app for deployment to **Render** or **Supabase**.

## ✅ What Was Done

- Created `InvoiceHistory` model to store invoice metadata
- Added UUID primary key for security
- Linked to Django `User` model
- Updated `Dockerfile` to collect static files
- Ensured compatibility with PostgreSQL (Render, Supabase)
- Used `dj-database-url` for database flexibility

## 🐳 How to Run Locally with Docker & Docker Compose

You can run the entire app in containers for a production like environment.

### 1. Make sure you have:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/) (v2.22.0+ recommended)

### 2. Build and run the app

```bash
docker-compose up --build
```

3. Access the app
   Open your browser:

```bash
http://127.0.0.1:8000
```

The app will be served via Gunicorn in a Docker container , just like in production.

4. Run Django commands (optional)
   To run migrate, createsuperuser, or test inside the container:

```bash
# Run migrations
docker-compose run --rm web python manage.py migrate

# Create a superuser
docker-compose run --rm web python manage.py createsuperuser

# Run tests
docker-compose run --rm web python manage.py test
```

> Tip: Use --rm to clean up the container after the command finishes.

5. Upload a csv to generate an invoice — download the pdf invoice

> "The test CSV file is located in the root folder (test_invoice.csv). Please use it as a reference when creating your own CSV file."

6. Shut down
   Press Ctrl+C in the terminal, then:

```bash
docker-compose down
```

## 🧪 How to Run Locally

1. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

2. Run server:

```bash
python manage.py runserver
```

3. Upload a csv to generate an invoice — download the pdf invoice

> "The test CSV file is located in the root folder (test_invoice.csv). Please use it as a reference when creating your own CSV file."

🚀 How to Deploy to Render

1. Go to https://render.com → "New Web Service"

2. Connect your GitHub repo

3. Set:

- Runtime : Docker
- Start Command : gunicorn invoice_generator.wsgi:application --bind 0.0.0.0:8000

4. Add environment variables:

- DATABASE_URL: Your PostgreSQL connection string
- SECRET_KEY: A long, random key
- DEBUG: False
- ALLOWED_HOSTS: your-app.onrender.com, your domain name if you have any

5. Deploy!

🌐 How to Use Supabase PostgreSQL

1. Sign up at https://supabase.com

2. Create a project

3. Copy the connection string from Settings → Database

4. Paste into Render’s Environment - DATABASE_URL

- ✅ No code changes needed — dj-database-url handles the rest.

📁 Files Updated

1. invoices/models.py – Added InvoiceHistory

2. Dockerfile – Added collectstatic

3. settings.py – Improved security and config

4. requirements.txt – Added whitenoise (optional)

```
invoice_generator/
├── .dockerignore
├── .env
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── .prettierignore
├── Dockerfile
├── README.md
├── Vagrantfile
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
├── database-info.txt
├── db.sqlite3
├── docker-compose.yml
├── env.txt
├── frontend/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
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
│   ├── frontend/
│   │   └── home.html
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
