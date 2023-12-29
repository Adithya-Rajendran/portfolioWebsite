FROM python:3.9

WORKDIR /usr/src/app

## Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the local directory contents into the container at /usr/src/app
COPY . .

# Install required Python packages
RUN pip install --upgrade pip
RUN pip install --upgrade -r requirements.txt

RUN python3 manage.py collectstatic --noinput

# Expose port 8000 for the Django application
EXPOSE 8000

# Run Django migrations and start the development server
CMD python3 manage.py makemigrations && \
    python3 manage.py migrate && \
    python manage.py test portfolio && \
    gunicorn resume_website.wsgi:application -b 0.0.0.0:8000 --workers 4
