# Use official Python image from DockerHub
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements file to the working directory
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 9187 for Flask
EXPOSE 9187

# Run the Flask application
CMD ["gunicorn", "-b", "0.0.0.0:9187", "app:create_app()"]
