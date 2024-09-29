import pytesseract
import cv2
from PIL import Image
import numpy as np

# Set the path to the tesseract executable (for Windows)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def preprocess_image(uploaded_file):
    # Open the uploaded image file
    image = Image.open(uploaded_file)

    # Convert image to grayscale
    image = np.array(image.convert('L'))  # Convert to grayscale (L mode)

    # Apply median filtering to remove noise
    image = cv2.medianBlur(image, 5)

    # Apply Otsu's thresholding to binarize the image
    _, image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Return preprocessed image
    return image

def perform_ocr(image):
    try:
        # Set custom configuration for better Hindi recognition
        custom_config = r'--oem 3 --psm 6 -l hin+eng'

        # Perform OCR on the preprocessed image
        extracted_text = pytesseract.image_to_string(image, config=custom_config)

        return extracted_text

    except Exception as e:
        return f"Error during OCR: {e}"
