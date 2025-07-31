# Django Invoice Generator 🧾

A full-stack Django app that converts CSV/Excel files into branded PDF invoices — with user authentication, invoice history, and DevOps integration.

Perfect for freelancers, small businesses, and developers who want to learn or sell a production-ready Django + DevOps project.

## 🚀 About the Project

This is a step-by-step side project that:

- Uploads CSV/Excel files
- Generates branded PDF invoices
- Saves invoice history
- Uses Docker, CI/CD, and cloud deployment
- Has built-in monetization potential

Built with:

- Django (Backend)
- HTML/CSS + Bootstrap (Frontend)
- WeasyPrint (PDF generation)
- Docker & GitHub Actions (DevOps)
- PostgreSQL (via Render or Supabase)

## 🧩 Tutorial Series

Each step of the project is tracked in a Git branch. You can follow along step-by-step by checking out each branch.

## 📚 Tutorial Branches

| Step   | Branch Name            | Description                                          |
|--------|------------------------|------------------------------------------------------|
| Step 1 | `step-1-project-setup` | Setup Django project and virtual environment         |
| Step 2 | `step-2-user-auth`     | Add login, register, and dashboard views             |
| Step 3 | `step-3-upload-csv`    | Upload and parse CSV/Excel files                     |
| Step 4 | `step-4-generate-pdf`  | Generate PDF invoices with totals and tax            |
| Step 5 | `step-5-dockerize`     | Dockerize the app using Vagrant (Windows-compatible) |
| Step 6 | `step-6-ci-cd`         | Add GitHub Actions CI/CD pipeline                    |
| Step 7 | `step-7-postgres`      | Switch to PostgreSQL using `dj-database-url`         |
| Step 8 | `step-8-deploy`        | Add InvoiceHistory model and prepare for deployment  |
| Step 9 | `step-9-monetize`      | Final polish and monetization setup                  |

## 📦 Tech Stack

| Layer        | Tools                                              |
|--------------|----------------------------------------------------|
| **Backend**  | Django                                             |
| **Frontend** | HTML/CSS, Bootstrap                                |
| **PDF**      | WeasyPrint (in Docker), xhtml2pdf (local fallback) |
| **Database** | SQLite (dev), PostgreSQL (prod)                    |
| **DevOps**   | Docker, Docker Compose, GitHub Actions, Render     |
| **Auth**     | Django built-in                                    |
| **Files**    | Pandas (CSV/Excel), Pillow (logo upload)           |

## 🐳 How to Run Locally with Docker & Docker Compose

You can run the app in containers for a production-like environment.

### 1. Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/) (v2.22.0+ recommended)

### 2. Build and Run

```bash
docker-compose up --build
```

### 3. Access the App

Open your browser:

```
http://127.0.0.1:8000
```

### 4. Run Django Commands:

```bash
# Migrate
docker-compose run --rm web python manage.py migrate

# Create superuser
docker-compose run --rm web python manage.py createsuperuser

# Test
docker-compose run --rm web python manage.py test
```

### 5. Shut Down

```bash
docker-compose down
```

## 🌐 How to Deploy to Render

1. Go to [https://render.com](https://render.com) → Click **"New Web Service"**
2. Connect your GitHub repository
3. Configure the following settings:

   - **Runtime:** `Docker`
   - **Start Command:**
     ```bash
     gunicorn invoice_generator.wsgi:application --bind 0.0.0.0:8000
     ```

4. Add the following **Environment Variables**:

| Variable        | Description                                            |
|-----------------|--------------------------------------------------------|
| `DATABASE_URL`  | Your PostgreSQL connection string (Render or Supabase) |
| `SECRET_KEY`    | A long, random Django secret key                       |
| `DEBUG`         | `False`                                                |
| `ALLOWED_HOSTS` | `your-app.onrender.com` (replace with your URL)        |

5. Click **Deploy!**

✅ Your app will be live at:  
[https://your-app.onrender.com](https://your-app.onrender.com)

---

## 💰 Monetization: Sell This Template on Gumroad

This project is not just a learning tool — it's a ready-to-sell Django SaaS starter.

You can sell it as a downloadable template on Gumroad for **$29–$49** one-time.

## 🛒 What Buyers Get

- ✅ Full source code with tutorial branches
- ✅ Docker + CI/CD + PostgreSQL setup
- ✅ User auth, invoice history, PDF generation
- ✅ DevOps integration (GitHub Actions, Render)
- ✅ Monetization hooks (`is_paid`, feature flags)
- ✅ Documentation and tutorial guide

## 🎯 Gumroad Product Example

**Title:**  
Django Invoice Generator – Ready-to-Deploy SaaS Template

**Description:**  
Automate invoicing for freelancers and small businesses with this full-stack Django app.

- ✅ Upload CSV/Excel → Generate Branded PDF Invoices
- ✅ User Auth, Invoice History & PDF Export
- ✅ Docker, CI/CD, PostgreSQL Ready
- ✅ DevOps-Integrated (GitHub Actions, Render)
- ✅ Monetization Hooks Built-In (Free/Paid, Gumroad, Stripe)

**Perfect for:**

- Django developers
- DevOps learners
- Freelancers building tools
- Anyone who wants to ship a SaaS starter

**Price:** $29 one-time  
**Includes:** Full source code, documentation, tutorial branches, support.

---

## 📎 Watch Demo Video

## 📥 Download on Gumroad

---

## 🎥 How to Record a Demo Video

Use Loom or OBS to record a 60–90 second video showing:

- Login
- Upload `test_invoice.csv`
- Fill company/client info
- Preview and download PDF
- View invoice history
- Show GitHub repo and deployment

Upload to YouTube (unlisted) or Loom, then link it in README and Gumroad.

---

## 📣 Marketing Plan

Share your project on:

- Reddit
  - r/django
  - r/Python
  - r/SideProject: _"I built a Django invoice generator with DevOps — now selling the template"_
- LinkedIn
  - Post series: _"How I built a monetizable Django project"_
- Hacker News
  - _Show HN: A Django Invoice Generator with DevOps_
- Indie Hackers
  - _How I built a SaaS starter and sold it_
- Twitter/X
  - Short clip + _"Download & deploy your own invoice SaaS"_

---

## 🧩 Future Expansion Ideas

- Multiple invoice templates (Premium)
- Stripe integration
- SaaS subscription plans
- Email invoice sending
- Usage-based billing
- Client management features
- Bulk invoice generation

---

## 🏁 Congratulations!

You’ve built a professional, monetizable Django project that showcases:

- Django
- DevOps (Docker, CI/CD)
- Database design
- PDF generation
- User authentication
- Monetization strategy

Now go sell it, ship it, and build the next one!

💬 **Tip:** Pin this repo to your GitHub profile — it’s a portfolio powerhouse.

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Made with 💡 by [Your Name]  
Let’s connect: [LinkedIn](https://linkedin.com/in/yourprofile) | [YouTube](https://youtube.com/yourchannel)
