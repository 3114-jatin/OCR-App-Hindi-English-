from PIL import ImageFilter

def perform_ocr(uploaded_file):
    try:
        # Open the uploaded image file
        image = Image.open(uploaded_file)

        # Preprocess the image: convert to grayscale and apply a filter
        image = image.convert("L")  # Convert to grayscale
        image = image.filter(ImageFilter.SHARPEN)  # Apply sharpening filter

        # Set custom configuration for better Hindi recognition
        custom_config = r'--oem 3 --psm 6'  # Modify PSM and OEM for improved accuracy

        # Perform OCR on the image for Hindi (hin) and English (eng)
        extracted_text = pytesseract.image_to_string(image, lang='hin+eng', config=custom_config)

        return extracted_text

    except Exception as e:
        return f"Error during OCR: {e}"
