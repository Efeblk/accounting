# Use a Python slim image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Copy entrypoint.sh and make it executable
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint to run the script
ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]

# CMD to start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
