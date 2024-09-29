# Use the official Python image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install Tesseract and language packages
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-hin \
    tesseract-ocr-eng \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Run the application
CMD ["streamlit", "run", "app.py"]
