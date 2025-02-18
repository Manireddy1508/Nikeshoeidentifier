# Use an official lightweight Python runtime
FROM python:3.9

# Set the working directory
WORKDIR /app

# Ensure Python recognizes the app directory as a module
ENV PYTHONPATH=/app

# Copy the project files
COPY ./app /app
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 8080

# Run the Flask app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

