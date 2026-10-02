import streamlit as st
import requests
BACKEND_URL = st.secrets.get("BACKEND_URL", "http://localhost:8000")

# Page Config and Layout
st.set_page_config(page_title="LegalEase", layout="centered")

# Header
st.markdown("<h2 style='text-align: center;'>AI Legal Document Generator</h2>", unsafe_allow_html=True)

# User Input Fields
document_type = st.text_input("Document Type (e.g., Agreement, Contract, NDA)")
parties = st.text_area("Parties Involved")
terms = st.text_area("Terms & Conditions (Use semicolons for bullet points)")
dates = st.text_input("Effective Date")

# Generate Button and API Call
if st.button("Generate Document"):
    if document_type and parties and terms and dates:
        # Send data to FastAPI backend
        response = requests.post(f"{BACKEND_URL}/generate", json={
            "document_type": document_type,
            "parties": parties,
            "terms": terms,
            "dates": dates
        })
        
        if response.status_code == 200:
            st.success("Document Generated Successfully!")
            generated_text = response.json()["document"]
            
            # Editable Document Preview
            edited_text = st.text_area("Edit Document Below:", generated_text, height=300)
            
            # Download Option
            st.download_button(
                label="Download as .TXT", 
                data=edited_text, 
                file_name=f"{document_type.replace(' ', '_').lower()}.txt"
            )
        else:
            st.error("Failed to generate document. Please check the backend server.")
    else:
        st.warning("Please fill in all the fields before generating.")