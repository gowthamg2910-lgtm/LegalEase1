# LegalEase: AI Legal Document Generator

Generate legal document drafts (rental agreements, NDAs, contracts) in seconds using AI.

**Live demo:** https://legalease1-guvdugwwy6p9wuapwqimyc.streamlit.app

## Features
- Enter the document type, parties, terms and effective date
- Gemini AI writes a full draft
- Edit the generated document in the app

## Tech Stack
- **Frontend:** Streamlit
- **Backend:** FastAPI + Uvicorn
- **AI:** Google Gemini API
- **Hosting:** Streamlit Community Cloud (frontend), Render (backend)

## Run Locally
1. Clone the repo and install packages:
   ```
   git clone https://github.com/gowthamg2910-lgtm/LegalEase1.git
   cd LegalEase1
   pip install -r requirements.txt
   ```
2. Create a `.env` file with your Gemini API key.
3. Start the backend:
   ```
   uvicorn legalEaseAPI.main:app --reload
   ```
4. In a second terminal, start the frontend:
   ```
   streamlit run frontend/app.py
   ```

## Project Structure
```
ai_core/        Gemini document generation logic
legalEaseAPI/   FastAPI backend (main.py, routes.py)
frontend/       Streamlit app (app.py)
```

## Disclaimer
Documents are AI-generated drafts and are not legal advice. Have a qualified lawyer review them before use.
