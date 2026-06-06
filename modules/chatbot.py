import os
from dotenv import load_dotenv
import google.generativeai as genai
import re

# Load .env
load_dotenv()

# Gemini API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Create Model
model = genai.GenerativeModel("gemini-2.5-flash")


# FUNCTION FOR APP.PY
def ask_ai(question):

    response = model.generate_content(
        f"""
        You are an expert agriculture assistant helping farmers.

        Provide practical advice about:
        - crop diseases
        - fertilizers
        - irrigation
        - organic farming
        - prevention methods

        Farmer Question:
        {question}
        """
    )

    return response.text



def format_ai_response(text):

    text = text.replace("\n", "<br>")

    text = re.sub(
        r"\*\*(.*?)\*\*",
        r"<span style='color:#15803d;font-weight:bold;'>🌱 \1</span>",
        text
    )

    return text