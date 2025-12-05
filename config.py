import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Gemini API key missing in .env")

genai.configure(api_key=API_KEY)

MODEL_NAME = "gemini-1.5-pro"


