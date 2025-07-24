# Step 6: Set Up CI/CD with GitHub Actions

This branch adds a full CI/CD pipeline using GitHub Actions.

## ✅ What Was Done

- Created `.github/workflows/ci.yml`
- Automated Docker image build and push to GitHub Container Registry (GHCR)
- Added Django test runner in CI
- Tagged images with `latest` and commit SHA
- Prepared for deployment to Render or Heroku

## 🧪 How to Trigger CI

1. Push to `main` or open a PR
2. Go to GitHub → "Actions" tab
3. Watch the pipeline run:
   - Build Docker image
   - Push to GHCR
   - Run Django tests

## 🚀 How to Deploy

### Option 1: Render (Docker)

- Connect your repo
- Use Dockerfile or GHCR image
- Set start command: `gunicorn invoice_generator.wsgi:application --bind 0.0.0.0:8000`

### Option 2: Heroku (Docker)

```bash
heroku container:push web -a your-app-name
heroku container:release web -a your-app-name

## 📁 Project Structure

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
