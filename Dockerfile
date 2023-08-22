# Use Python 3.10 slim as base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy Pipfile and Pipfile.lock to the working directory
COPY Pipfile Pipfile.lock .env ./

COPY "/etc/letsencrypt/live/billtheai.com/fullchain.pem" "./fullchain.pem"
COPY "/etc/letsencrypt/live/billtheai.com/privkey.pem" "./privkey.pem"

# Install pipenv, libpq-dev, and use pipenv to install Python dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && \
    pip install pipenv && \
    pipenv install --system --deploy && \
    apt-get purge -y --auto-remove gcc && \
    rm -rf /var/lib/apt/lists/*

# Copy main.py to the working directory
COPY main.py .

# Copy the mjb-tweet-frontend/dist directory to the same in the container
COPY bill-ai-frontend/dist bill-ai-frontend/dist

# Expose port 443
EXPOSE 443

# Command to run the application
CMD ["python3", "-m", "gunicorn", "-w", "4", "-b", "0.0.0.0:443",
"--certfile", "./fullchain.pem",
"--keyfile", "./privkey.pem", "app:app"]
