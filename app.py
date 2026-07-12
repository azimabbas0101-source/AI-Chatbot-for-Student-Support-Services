import streamlit as st
import os
from chatbot import setup_gemini, get_response

st.set_page_config(
    page_title="AI Chatbot for Student Support Services",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Chatbot for Student Support Services")

st.write(
    "Welcome! Ask any question related to admissions, fees, examinations, library, hostel, placements, scholarships, or any student-related topic."
)

question = st.text_input("Ask your question:")

api_key = os.getenv("GEMINI_API_KEY")

if question:
    if api_key:
        try:
            client = setup_gemini(api_key)
            answer = get_response(client, question)
            st.success(answer)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.error("Gemini API key not found.")
