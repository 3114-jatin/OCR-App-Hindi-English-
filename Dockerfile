# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Install Tesseract OCR and other dependencies
RUN apt-get update && \
    apt-get install -y tesseract-ocr tesseract-ocr-hin && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . .

# Upgrade pip and install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "your_app.py"]  # Replace your_app.py with your actual main file
