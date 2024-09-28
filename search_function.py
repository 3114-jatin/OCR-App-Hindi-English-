def search_keywords(text, keyword):
    # Check if either text or keyword is None
    if text is None or keyword is None:
        return "Error: Text or keyword is None"
    
    # Proceed with the keyword search
    if keyword.lower() in text.lower():
        return f"Keyword '{keyword}' found in the text!"
    else:
        return f"Keyword '{keyword}' not found."
