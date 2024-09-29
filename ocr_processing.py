import pytesseract

# Set the path to the tesseract executable (for Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR/tesseract.exe'

from PIL import Image
import io

def perform_ocr(uploaded_file):
    try:
        # Open the uploaded image file
        image = Image.open(uploaded_file)

        # Set custom configuration for better Hindi recognition
        #custom_config = r'--oem 3 --psm 6'  # Modify PSM and OEM for improved accuracy
        custom_config = r'--oem 3 --psm 3 -l hin+eng'


        # Perform OCR on the image for Hindi (hin) and English (eng)
        extracted_text = pytesseract.image_to_string(image, lang='hin+eng', config=custom_config)

        return extracted_text

    except Exception as e:
        return f"Error during OCR: {e}"
