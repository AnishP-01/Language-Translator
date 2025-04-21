import streamlit as st
from deep_translator import GoogleTranslator
from unidecode import unidecode
from googletrans import LANGUAGES

# -------------------------
# 🧠 Utility Functions
# -------------------------

def get_language_code(lang_name):
    """Find the language code by its name from googletrans LANGUAGES."""
    lang_name = lang_name.lower()
    for code, name in LANGUAGES.items():
        if name.lower() == lang_name:
            return code
    return None

def display_available_languages():
    """Return a sorted list of available languages."""
    sorted_langs = sorted(LANGUAGES.items(), key=lambda x: x[1])
    return [name.title() for code, name in sorted_langs]

# -------------------------
# 🚀 Streamlit App Starts Here
# -------------------------

# Page setup
st.set_page_config(page_title="🌍 Language Translator", layout="centered")

# Title and description
st.title("🔤 Language Translator with Pronunciation")
st.markdown("Translate text between languages and get a **phonetic** version (approximate pronunciation).")

# Get list of languages
lang_names = display_available_languages()

# Language selection
col1, col2 = st.columns(2)
with col1:
    from_lang_name = st.selectbox("Select source language:", lang_names, index=lang_names.index("English"))
with col2:
    to_lang_name = st.selectbox("Select target language:", lang_names, index=lang_names.index("Hindi"))

# Text input
input_text = st.text_area("📝 Enter text to translate:", height=150)

# Translate button
if st.button("🌐 Translate"):
    from_lang_code = get_language_code(from_lang_name)
    to_lang_code = get_language_code(to_lang_name)

    if not input_text.strip():
        st.warning("Please enter some text to translate.")
    else:
        try:
            # Perform translation
            translated = GoogleTranslator(source=from_lang_code, target=to_lang_code).translate(input_text)

            # Get pronunciation (approx)
            pronunciation = unidecode(translated)

            # Display results
            st.success(f"✅ Translated Text ({to_lang_name}):")
            st.text_area("📘 Translation:", translated, height=150)

            st.success("🔊 Pronunciation (approx):")
            st.text_area("🗣️ Pronunciation:", pronunciation if pronunciation.strip() else "Not Available", height=100)

        except Exception as e:
            st.error(f"⚠️ Error occurred: {str(e)}")
