# Use the official Python image from the Docker Hub
FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    python3-dev \
    portaudio19-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install required packages
RUN pip install -r requirements.txt

# Expose any ports if necessary (e.g., for a web server)
# EXPOSE 5000

# Set the command to run the application
CMD ["./start.sh"]