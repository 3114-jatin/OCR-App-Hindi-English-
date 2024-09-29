import streamlit as st
from ocr_processing import perform_ocr
from search_function import search_keywords

# Title and description
st.title('OCR Web Application (Hindi & English)')
st.write("Upload an image containing text in Hindi or English, extract the text using OCR, and search for keywords in the extracted text.")

# Image upload
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    # Perform OCR on the uploaded image
    extracted_text = perform_ocr(uploaded_file)
    
    # Check if OCR returned valid text
    if extracted_text:
        st.write("### Extracted Text")
        st.write(extracted_text)
        
        # Keyword search within extracted text
        keyword = st.text_input("Enter a keyword to search within the extracted text:")
        
        if keyword:
            results = search_keywords(extracted_text, keyword)
            st.write("### Search Results")
            
            if results:
                st.markdown(results, unsafe_allow_html=True)
            else:
                st.write(f"No matching keywords found for '{keyword}'.")
    else:
        st.write("No text could be extracted from the image. Please try again with a clearer image.")
