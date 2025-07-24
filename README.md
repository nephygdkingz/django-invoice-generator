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
├── .github/
│ └── workflows/
│ └── ci.yml
├── .gitignore
├── .prettierignore
├── Dockerfile
├── README.md
├── Vagrantfile
├── account/
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── migrations/
│ │ └── **init**.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── db.sqlite3
├── docker-compose.yml
├── generate_tree.py
├── invoice_generator/
│ ├── **init**.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── invoices/
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── migrations/
│ │ └── **init**.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── manage.py
├── requirements.txt
├── static/
│ ├── admin/
│ │ ├── css/
│ │ │ ├── autocomplete.css
│ │ │ ├── base.css
│ │ │ ├── changelists.css
│ │ │ ├── dark_mode.css
│ │ │ ├── dashboard.css
│ │ │ ├── forms.css
│ │ │ ├── login.css
│ │ │ ├── nav_sidebar.css
│ │ │ ├── responsive.css
│ │ │ ├── responsive_rtl.css
│ │ │ ├── rtl.css
│ │ │ ├── unusable_password_field.css
│ │ │ ├── vendor/
│ │ │ │ └── select2/
│ │ │ │ ├── LICENSE-SELECT2.md
│ │ │ │ ├── select2.css
│ │ │ │ └── select2.min.css
│ │ │ └── widgets.css
│ │ ├── img/
│ │ │ ├── LICENSE
│ │ │ ├── README.txt
│ │ │ ├── calendar-icons.svg
│ │ │ ├── gis/
│ │ │ │ ├── move_vertex_off.svg
│ │ │ │ └── move_vertex_on.svg
│ │ │ ├── icon-addlink.svg
│ │ │ ├── icon-alert.svg
│ │ │ ├── icon-calendar.svg
│ │ │ ├── icon-changelink.svg
│ │ │ ├── icon-clock.svg
│ │ │ ├── icon-deletelink.svg
│ │ │ ├── icon-hidelink.svg
│ │ │ ├── icon-no.svg
│ │ │ ├── icon-unknown-alt.svg
│ │ │ ├── icon-unknown.svg
│ │ │ ├── icon-viewlink.svg
│ │ │ ├── icon-yes.svg
│ │ │ ├── inline-delete.svg
│ │ │ ├── search.svg
│ │ │ ├── selector-icons.svg
│ │ │ ├── sorting-icons.svg
│ │ │ ├── tooltag-add.svg
│ │ │ └── tooltag-arrowright.svg
│ │ └── js/
│ │ ├── SelectBox.js
│ │ ├── SelectFilter2.js
│ │ ├── actions.js
│ │ ├── admin/
│ │ │ ├── DateTimeShortcuts.js
│ │ │ └── RelatedObjectLookups.js
│ │ ├── autocomplete.js
│ │ ├── calendar.js
│ │ ├── cancel.js
│ │ ├── change_form.js
│ │ ├── core.js
│ │ ├── filters.js
│ │ ├── inlines.js
│ │ ├── jquery.init.js
│ │ ├── nav_sidebar.js
│ │ ├── popup_response.js
│ │ ├── prepopulate.js
│ │ ├── prepopulate_init.js
│ │ ├── theme.js
│ │ ├── unusable_password_field.js
│ │ ├── urlify.js
│ │ └── vendor/
│ │ ├── jquery/
│ │ │ ├── LICENSE.txt
│ │ │ ├── jquery.js
│ │ │ └── jquery.min.js
│ │ ├── select2/
│ │ │ ├── LICENSE.md
│ │ │ ├── i18n/
│ │ │ │ ├── af.js
│ │ │ │ ├── ar.js
│ │ │ │ ├── az.js
│ │ │ │ ├── bg.js
│ │ │ │ ├── bn.js
│ │ │ │ ├── bs.js
│ │ │ │ ├── ca.js
│ │ │ │ ├── cs.js
│ │ │ │ ├── da.js
│ │ │ │ ├── de.js
│ │ │ │ ├── dsb.js
│ │ │ │ ├── el.js
│ │ │ │ ├── en.js
│ │ │ │ ├── es.js
│ │ │ │ ├── et.js
│ │ │ │ ├── eu.js
│ │ │ │ ├── fa.js
│ │ │ │ ├── fi.js
│ │ │ │ ├── fr.js
│ │ │ │ ├── gl.js
│ │ │ │ ├── he.js
│ │ │ │ ├── hi.js
│ │ │ │ ├── hr.js
│ │ │ │ ├── hsb.js
│ │ │ │ ├── hu.js
│ │ │ │ ├── hy.js
│ │ │ │ ├── id.js
│ │ │ │ ├── is.js
│ │ │ │ ├── it.js
│ │ │ │ ├── ja.js
│ │ │ │ ├── ka.js
│ │ │ │ ├── km.js
│ │ │ │ ├── ko.js
│ │ │ │ ├── lt.js
│ │ │ │ ├── lv.js
│ │ │ │ ├── mk.js
│ │ │ │ ├── ms.js
│ │ │ │ ├── nb.js
│ │ │ │ ├── ne.js
│ │ │ │ ├── nl.js
│ │ │ │ ├── pl.js
│ │ │ │ ├── ps.js
│ │ │ │ ├── pt-BR.js
│ │ │ │ ├── pt.js
│ │ │ │ ├── ro.js
│ │ │ │ ├── ru.js
│ │ │ │ ├── sk.js
│ │ │ │ ├── sl.js
│ │ │ │ ├── sq.js
│ │ │ │ ├── sr-Cyrl.js
│ │ │ │ ├── sr.js
│ │ │ │ ├── sv.js
│ │ │ │ ├── th.js
│ │ │ │ ├── tk.js
│ │ │ │ ├── tr.js
│ │ │ │ ├── uk.js
│ │ │ │ ├── vi.js
│ │ │ │ ├── zh-CN.js
│ │ │ │ └── zh-TW.js
│ │ │ ├── select2.full.js
│ │ │ └── select2.full.min.js
│ │ └── xregexp/
│ │ ├── LICENSE.txt
│ │ ├── xregexp.js
│ │ └── xregexp.min.js
│ └── assets/
│ ├── bootstrap/
│ │ ├── bootstrap.min.css
│ │ └── bootstrap.min.js
│ ├── css/
│ │ └── style.css
│ ├── images/
│ └── js/
│ └── main.js
├── templates/
│ ├── account/
│ │ └── dashboard.html
│ ├── authentication/
│ │ ├── login.html
│ │ └── register.html
│ ├── includes/
│ │ ├── form_errors.html
│ │ └── messages.html
│ ├── invoices/
│ │ ├── invoice_template.html
│ │ ├── invoice_template_pdf.html
│ │ ├── new_invoice_template.html
│ │ ├── preview.html
│ │ └── upload.html
│ └── main/
│ ├── base.html
│ └── navbar.html
├── test_invoice.csv
├── tree_clean.txt
└── update_readme.py

```

```

```
