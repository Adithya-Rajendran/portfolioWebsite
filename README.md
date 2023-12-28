# portfolioWebsite
This repository contains the source code for my Website access it from [adithya-rajendran.com](https://adithya-rajendran.com)
The rest of the page is included in case you, the reader, wants to clone or fork this repo and use it.

## Features

 - **Home Page**: Introduce yourself and provide a brief overview of your skills and passion.
 - **Contact Page**: Allow visitors to get in touch with you through a contact form.
 - **Projects Page**: Display a list of your projects with details and images.
 - **Resume Page**: Showcase your education, skills, and professional experiences.
 - **Static Files**: Manage CSS stylesheets, images, and other static files to enhance the website's appearance.

## Setup Instructions

 1. Clone the Repository:

```bash
git clone https://github.com/your-username/django-portfolio.git
cd django-portfolio
```

 2. Install Dependencies:

```bash
pip install -r requirements.txt
```

 3. Apply Migrations:

```bash
python manage.py migrate
```

 4. Create Superuser:

```bash
python manage.py createsuperuser
```

 5. Run the Development Server:

```bash
python manage.py runserver
```

 6. Access the Website:

Open your browser and go to (127.0.0.1:8000/)[http://127.0.0.1:8000/]

 7. Admin Panel:

Access the Django admin panel at (127.0.0.1:8000/admin/)[http://127.0.0.1:8000/admin/] using the superuser credentials.

## Project Structure

**portfolio/**: Django app containing models, views, and templates.  
**portfolio/static/**: Directory for CSS stylesheets and images.  
**portfolio/templates/**: HTML templates for various pages.  
**manage.py**: Django management script.  
**requirements.txt**: List of Python dependencies.  


## Environment Vars

Add these variables to a .env file or a setting.ini file or directly to the environment variables:

```txt
EMAIL_HOST=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_PORT=

MY_EMAILS=

SECRET_KEY=

POSTGRES_DATABASE=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_HOST=
```

### Multiple emails

Use comma seperated values for multiple emails
Example:

```txt
MY_EMAILS=email@email.com,email2@domain.com
```

### Secret Key

To generate a secret key:

 1. Start a python shell

 ```bash
 python manage.py shell
 ```

 2. Run the following commands to get a key

 ```python
from django.core.management.utils import get_random_secret_key

new_secret_key = get_random_secret_key()
print(new_secret_key)
 ```

## Deployment

The project is designed to be easily deployable. You can use platforms like Heroku, Vercel, or your preferred hosting service.

***Important***: Set the `DEBUG` variable to **False** in the settings.py file before deploying in a production environment.
