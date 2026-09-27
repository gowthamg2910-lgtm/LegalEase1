import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
class GeminiDocumentGenerator:
    def __init__(self):
        # Configures the API key from your .env file
        genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        # Selects the model specified in Milestone 1
        self.model = genai.GenerativeModel('gemini-3.8-flash')

    def generate_document(self, document_type, parties, terms, dates):
        prompt = (
            f"Generate a comprehensive legal document titled '{document_type}' \n"
            f"Involved parties: {parties} \n"
            f"Effective Date: {dates}\n"
            f"Terms and conditions: {terms} \n"
            " Ensure formal legal structure with multiple sections and legal clauses."
        )
        response = self.model.generate_content(prompt)
        return response.text