import pytesseract
from PIL import Image

# Set the Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust if needed

# Try running Tesseract on a sample image
try:
    img = Image.open('your_image.png')  # Change this to a valid image path
    text = pytesseract.image_to_string(img, lang='eng+hin')
    print("Extracted Text:", text)
except Exception as e:
    print("Error:", e)
