import streamlit as st
import os
from chatbot import setup_gemini, get_response

# Page Configuration
st.set_page_config(
    page_title="AI Chatbot for Student Support Services",
    page_icon="🎓",
    layout="centered"
)

# Sidebar
st.sidebar.title("🎓 Student Support")

st.sidebar.markdown("""
### 📌 Available Services

- 📝 Admissions
- 💰 Fees
- 📖 Examination
- 📚 Library
- 🏠 Hostel
- 💼 Placements
- 🎓 Scholarships

---

### ℹ️ About

This AI chatbot helps students by answering questions related to student support services.
""")

# Title
st.title("🎓 AI Chatbot for Student Support Services")

st.write(
    "Welcome! Ask any question related to admissions, fees, examinations, library, hostel, placements, scholarships, or any student-related topic."
)

# Create chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input (Bottom)
question = st.chat_input("Ask your question...")

# Read API Key
api_key = os.getenv("GEMINI_API_KEY")

if question:
    # Show user message
    with st.chat_message("user"):
        st.markdown(question)

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    if api_key:
        try:
            client = setup_gemini(api_key)

            # Loading animation
            with st.spinner("🤖 Thinking..."):
                answer = get_response(client, question)

            # Show AI response
            with st.chat_message("assistant"):
                st.markdown(answer)

            # Save AI response
            st.session_state.messages.append(
                {"role": "assistant", "content": answer}
            )

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.error("Gemini API key not found.")
