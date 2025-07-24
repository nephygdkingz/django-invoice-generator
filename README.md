# Step 7: Switch to PostgreSQL with `dj-database-url`

This branch replaces Django's default `sqlite3` database with **PostgreSQL** using the `dj-database-url` library, making the app production-ready and compatible with cloud platforms like:

- ✅ [Render](https://render.com)
- ✅ [Supabase](https://supabase.com)
- ✅ [Neon](https://neon.tech)
- ✅ [Railway](https://railway.app)
- ✅ [Fly.io](https://fly.io)

> 🔒 **Why?**  
> Platforms like Render use **ephemeral storage** — any changes to `db.sqlite3` are lost on restart.  
> PostgreSQL provides **persistent, reliable storage** for users, invoices, and session data.

---

## ✅ What Was Done

- ✅ Added `dj-database-url` to parse `DATABASE_URL`
- ✅ Updated `settings.py` to support:
  - `sqlite3` for **local development**
  - `PostgreSQL` via `DATABASE_URL` in **production**
- ✅ Added `.env` support for local environment variables
- ✅ Ensured migrations run automatically in Docker
- ✅ Made the app **database-agnostic** — works with any PostgreSQL provider

---

## 🧪 How to Run Locally

### Option 1: Use SQLite (Default)

No setup needed — just run:

```bash
python manage.py runserver

```

Option 2: Use PostgreSQL Locally (Recommended for Consistency)

- Install PostgreSQL (e.g., via Postgres.app or brew install postgresql)
- Create a database:

```bash
createdb invoice_local
```

3. Create a .env file in the project root:

```bash
DATABASE_URL=postgres://localhost/invoice_local
DEBUG=True
SECRET_KEY=your-secret-key-here
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Run migrations:

```bash
python manage.py migrate
```

6. Start Server:

```bash
python manage.py runserver
```

🚀 How to Deploy to Render / Supabase / Neon

1. Set the DATABASE_URL environment variable in your platform:

```
postgres://user:password@host:5432/dbname
```

2. Deploy using Docker
3. Migrations run automatically via:

```
CMD ["sh", "-c", "python manage.py migrate --noinput && gunicorn ..."]
```

> "💡 Tip: Your app now works with any PostgreSQL provider — just change the connection string! "

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

```

```
