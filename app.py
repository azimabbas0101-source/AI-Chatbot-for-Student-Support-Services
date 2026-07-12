import streamlit as st
import os
from chatbot import setup_gemini, get_response

st.set_page_config(
    page_title="AI Chatbot for Student Support Services",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Chatbot for Student Support Services")

st.write("""
Welcome! This chatbot helps students with common college-related queries.
""")

st.markdown("""
### Select a Topic

- 🎓 Admission
- 💰 Fees
- 📝 Examination
- 📚 Library
- 🏠 Hostel
- 💼 Placements
- 🎁 Scholarships
""")

question = st.text_input("Ask your question:")
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    model = setup_gemini(api_key)

if question:
    if api_key:
        response = get_response(model, question)
        st.success(response)
    else:
        st.error("Gemini API key not found.")
