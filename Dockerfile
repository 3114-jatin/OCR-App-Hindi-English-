# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Install Tesseract OCR with Hindi language support and other dependencies
RUN apt-get update && \
    apt-get install -y tesseract-ocr tesseract-ocr-eng tesseract-ocr-hin && \
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    tesseract --version  # Check Tesseract installation

# Copy the current directory contents into the container at /app
COPY . .

# Upgrade pip and install any needed packages specified in requirements.txt
RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt


# Expose the port the app runs on
EXPOSE 8501

# Use JSON arguments for CMD to prevent OS signal issues
CMD ["streamlit", "run", "app.py"]
