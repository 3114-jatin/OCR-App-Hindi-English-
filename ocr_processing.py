import cv2
import pytesseract
from PIL import Image
import numpy as np
from transformers import pipeline

# Set the path to the tesseract executable (for Windows)
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # Adjust this for your environment

# Initialize Hugging Face OCR pipeline
ocr_pipeline = pipeline("document-image-classification", model="microsoft/layoutlmv3-base")

def preprocess_image(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply binary thresholding to get a binary image
    _, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)

    return thresh

def perform_ocr(uploaded_file):
    try:
        # Open the uploaded image file with PIL
        image = Image.open(uploaded_file)

        # Convert PIL image to OpenCV format (numpy array)
        cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # Preprocess the image using OpenCV
        preprocessed_image = preprocess_image(cv_image)

        # Perform OCR using Tesseract
        tesseract_text = pytesseract.image_to_string(preprocessed_image, lang='hin+eng', config='--oem 3 --psm 6')

        # Convert preprocessed image back to PIL for Hugging Face model
        huggingface_image = Image.fromarray(preprocessed_image)

        # Perform OCR using Hugging Face model
        huggingface_result = ocr_pipeline(huggingface_image)

        # Combine results from both Tesseract and Hugging Face
        extracted_text = tesseract_text + "\n" + huggingface_result

        return extracted_text.strip()  # Remove any leading/trailing whitespace

    except Exception as e:
        return f"Error during OCR: {e}"
