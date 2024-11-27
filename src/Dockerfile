# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /src

# Copy requirements.txt to the container
COPY src/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire src directory into the container
COPY src/ /src/

# Expose the port that FastAPI will run on
EXPOSE 8000

# Start the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
