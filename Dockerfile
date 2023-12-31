# Stage 1: Build environment
FROM python:3.11 AS builder

WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a virtual environment
RUN python -m venv /usr/src/app/venv

# Set environment variables for virtual environment
ENV PATH="/usr/src/app/venv/bin:$PATH"

# Copy only the requirements file to avoid unnecessary installs
COPY requirements.txt .

# Install required Python packages
RUN pip install --upgrade pip && \
    pip install --upgrade -r requirements.txt

# Stage 2: Production environment
FROM python:3.11

WORKDIR /usr/src/app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy installed dependencies from the builder stage
COPY --from=builder /usr/src/app/venv /usr/src/app/venv

ENV PATH="/usr/src/app/venv/bin:$PATH"

# Copy the local directory contents into the container
COPY . .

# Create a non-root user
RUN useradd -ms /bin/bash django

# Change ownership of the application directory to the non-root user
RUN chown -R django:django /usr/src/app

# Switch to the non-root user
USER django

# Create directories
RUN mkdir /usr/src/app/static /usr/src/app/media

# Expose port 8000 for the Django application
EXPOSE 8000

# Run Django migrations and start the development server
CMD python3 manage.py collectstatic --noinput && \
    python3 manage.py makemigrations && \
    python3 manage.py migrate && \
    python3 manage.py test portfolio && \
    gunicorn resume_website.wsgi:application -b 0.0.0.0:8000 --workers 4
