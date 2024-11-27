# Use a lightweight Python image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt to the container
COPY src/requirements.txt .

# Install required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire src folder to the container
COPY src/ /app/src/

# Expose the port that FastAPI will run on
EXPOSE 8000

# Run the FastAPI application with Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
