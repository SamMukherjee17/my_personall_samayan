
# Use a minimal base image with Python 3.9 installed
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR/app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the port on which the Flask application will run
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=app:super_kart_api

# Define the command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
