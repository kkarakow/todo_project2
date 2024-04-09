# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies required for mysqlclient
RUN apt-get update && apt-get install -y default-libmysqlclient-dev gcc

# Copy the requirements file into the container at /app/
COPY todo_project2/requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /app/
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000 to the outside world
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

