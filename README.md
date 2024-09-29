OCR Web Application (Hindi & English)
Overview
This web-based application extracts text from images containing Hindi and English text using Optical Character Recognition (OCR) and allows the user to search for specific keywords in the extracted text.
Features
•	OCR Support: Extracts text from images in both Hindi and English.
•	Image Preprocessing: Converts images to grayscale, removes noise, and applies thresholding for better OCR accuracy.
•	Keyword Search: Allows searching for keywords in the extracted text.
Technologies Used
•	Streamlit: For creating the web interface.
•	Tesseract OCR: For optical character recognition.
•	OpenCV: For image preprocessing.
•	Python: Core programming language.
•	Huggingface: OCR activity
How It Works
1.	Upload an Image: The user uploads an image in JPG, JPEG, or PNG format.
2.	Extract Text: The app preprocesses the image and uses Tesseract OCR to extract text.
3.	Search Keywords: Users can enter a keyword to search within the extracted text.
Installation
1. Prerequisites
Ensure you have the following installed on your system:
•	Python 3.8 or later.
•	Tesseract-OCR installed.
o	For Windows: Download and install Tesseract from this link.
o	For Linux: Use the following command to install Tesseract:
bash
Copy code
sudo apt-get install tesseract-ocr tesseract-ocr-hin tesseract-ocr-eng
o	For Mac: Use Homebrew:
bash
Copy code
brew install tesseract
2. Clone the Repository
Clone this repository to your local machine:
bash
Copy code
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
3. Set Up a Virtual Environment
It's recommended to use a virtual environment for this project. You can set it up as follows:
bash
Copy code
# Create virtual environment
python3 -m venv ocr_env

# Activate the virtual environment
# On macOS/Linux:
source ocr_env/bin/activate

# On Windows:
ocr_env\Scripts\activate
4. Install Dependencies
Install all the required packages using requirements.txt:
bash
Copy code
pip install -r requirements.txt
5. Run the App Locally
To run the application on your local machine:
bash
Copy code
streamlit run app.py
6. Docker (Optional)
You can also deploy the app using Docker. To build and run the Docker container:
bash
Copy code
docker build -t your-app-name .
docker run -p 8501:8501 your-app-name
File Structure
bash
Copy code
├── app.py                # Main Streamlit app script
├── ocr_processing.py      # OCR processing functions
├── search_function.py     # Function to search keywords in text
├── requirements.txt       # Python dependencies
├── packages.txt           # Linux dependencies (for Streamlit Cloud deployment)
└── README.md              # This file
Usage
1.	Upload an Image: Use the "Upload an Image" button to upload an image containing Hindi and/or English text.
2.	View Extracted Text: Once the image is uploaded, the app will display the extracted text.
3.	Search for Keywords: Enter a keyword to search within the extracted text.
Custom Configuration
The app uses the following Tesseract OCR configuration for better recognition of Hindi and English:
python
Copy code
custom_config = r'--oem 3 --psm 6 -l hin+eng'
•	--oem 3: Uses both the legacy and LSTM OCR engine.
•	--psm 6: Assumes a uniform block of text.
•	-l hin+eng: Recognizes text in both Hindi and English.
Common Issues
1.	Tesseract is not installed or not in PATH: If you encounter this error, ensure that Tesseract is installed and its path is correctly set in the code:
python
Copy code
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'  # For Linux
On Windows, update the path to where Tesseract is installed:
python
Copy code
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

Images of App deployed on streamlit

 

 




Images from app deployed on Local

![image](https://github.com/user-attachments/assets/71283168-73eb-4c91-b691-94b3e8fdb82a)

 


 
Contributing
Feel free to contribute to this project by submitting issues or pull requests.
________________________________________
This README provides essential information about the project and guides users on how to install, run, and use the application. 
Link of App deployed on Streamlit

Streamlit (fbkrrn2t8sjzq9fhmatezx.streamlit.app)
https://fbkrrn2t8sjzq9fhmatezx.streamlit.app/

Github repo link

3114-jatin/OCR-App-Hindi-English-: This is a web-based Optical Character Recognition (OCR) application built using Streamlit.It allows users to upload images with text in both Hindi and English, extract the text using Tesseract OCR, and perform keyword searches within the extracted text. The application is designed for easy deployment. (github.com)

