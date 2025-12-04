import google.generativeai as genai
from config import MODEL_NAME

def summarize(text: str):
    model = genai.GenerativeModel(MODEL_NAME)

    response = model.generate_content(
        f"Summarize this into 3–4 bullet points:\n {text}"
    )

    return response.text

