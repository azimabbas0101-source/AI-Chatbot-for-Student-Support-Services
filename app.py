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

# Create chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.text_input("Ask your question:")

api_key = os.getenv("GEMINI_API_KEY")

if question:
    # Save user question
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    if api_key:
        try:
            client = setup_gemini(api_key)

with st.spinner("🤖 Thinking..."):
    answer = get_response(client, question)

st.session_state.messages.append(
    {"role": "assistant", "content": answer}
)

st.success(answer)
