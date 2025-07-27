# 🏨 OYO_INSPIRED_CLONE

A full-featured hotel booking web application inspired by OYO. Built with **Django**, integrated with **MySQL (WAMP)**, it supports hotel uploads, user authentication with **email OTP login**, media/image handling, and admin/vendor dashboards.

---

## 🚀 Features

- ✅ Vendor Registration & Login with Email OTP
- ✅ Upload Hotel Details with Images
- ✅ Hotel Dashboard for Vendors
- ✅ Search & Filter by **Price** and **Date**
- ✅ User Authentication System (OTP-based)
- ✅ Admin Panel (Django default)
- ✅ Image Upload & Preview
- ✅ Environment Config with `.env`

---

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Database**: MySQL (via WAMP server)
- **Frontend**: HTML, CSS, Bootstrap
- **Email**: SMTP (via Gmail or custom server)
- **Deployment Ready**: Switchable Redis/Cache support via `settings.py`
- **Consider settings.py for most of configuration**  # add more in future

---

## 📂 Project Structure

OYO_INSPIRED_CLONE/
├── accounts/ # User login, registration, OTP logic
├── hotel/ # Vendor hotel management logic
├── media/ # Uploaded hotel images
├── static/ # CSS, JS, Bootstrap
├── templates/ # base.html + all HTML pages
├── OYO_INSPIRED_CLONE/ # Django project settings
├── env/ # Local virtual environment (not tracked)
├── .env # Actual environment variables (not tracked)
├── .env.sample # Sample .env configuration
├── .gitignore
├── LICENSE
├── manage.py
├── requirements.txt




---

## ⚙️ Setup Instructions

0. **Conside the settings.py and .env.sample and requirements for all Config**

1. **Clone the repo**

   ```bash
   git clone https://github.com/aphex18/OYO_INSPIRED_CLONE.git
   cd OYO_INSPIRED_CLONE

2. **Create a virtual environment**
        python -m venv env
        source env/bin/activate      # On Windows: env\Scripts\activate

3. **Install dependencies**
        pip install -r requirements.txt

4. **Configure Environment Variables**

Copy .env.sample to .env

Fill in your credentials:

            DB_NAME=your_db_name
            DB_USER=your_db_user
            DB_PASSWORD=your_db_password
            DB_HOST=localhost
            DB_PORT=3306
            SECRET_KEY=your_django_secret_key
            EMAIL_HOST_USER = 'hostemail@gmail.com'
            EMAIL_HOST_PASSWORD ="abc"

Conside .env.sample for all environment variable and other config

5. **Set up the database**

Create a MySQL database (e.g., oyo_clone)

Update DATABASES section in settings.py  

6. **Run Migrations**
        python manage.py makemigrations
        python manage.py migrate
 

7. **Start the server**
        python manage.py runserver


**✉️ Email OTP Setup**
Uses Django's EmailBackend for sending OTP

Configure SMTP settings in .env and settings.py


# Use the Django admin panel to create superusers or simulate logins
python manage.py createsuperuser
# use the django admin to check whether the data is coming or not is the otp working,etc. It is highly recommended to use django admin


📌 Notes
For deployment, switch to production-ready tools like Redis for caching.

To customize hotel filters (e.g., city-based), update the models and templates accordingly.

All environment and configuration settings are controlled via .env and settings.py.

