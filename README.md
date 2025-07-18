# Step 2: Setup User Authentication

This branch adds user authentication to the Django Invoice Generator.

## ✅ What Was Done

- Created the `invoices` app
- Set up login, register, and logout views
- Protected the dashboard with `@login_required`
- Added Bootstrap-based templates

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
   http://127.0.0.1:8000/login/
   http://127.0.0.1:8000/register/
   http://127.0.0.1:8000/dashboard/
