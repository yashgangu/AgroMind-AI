# modules/translator.py
import streamlit as st
from deep_translator import GoogleTranslator

lang_map = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Punjabi": "pa",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml"
}

def translate_text(text):
    # Fetch the language saved in session_state, defaulting to English
    language = st.session_state.get("selected_language", "English")
    
    if language == "English" or not text:
        return text

    try:
        return GoogleTranslator(
            source='auto',
            target=lang_map[language]
        ).translate(text)
    except:
        return text