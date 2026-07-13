import streamlit as st
import os
from chatbot import setup_gemini, get_response

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="AI Chatbot for Student Support Services",
    page_icon="🎓",
    layout="wide"
)

# ----------------------------
# Sidebar
# ----------------------------
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
This chatbot is designed to help students with common college-related queries.
""")

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# ----------------------------
# Chat History
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------
# Header
# ----------------------------
st.title("🎓 AI Chatbot for Student Support Services")

st.markdown("""
Welcome to the **AI Student Support Assistant**.

Ask questions related to:

- 📝 Admissions
- 💰 Fees
- 📖 Examination
- 📚 Library
- 🏠 Hostel
- 💼 Placements
- 🎓 Scholarships
""")

# ----------------------------
# Feature Cards
# ----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("📝 **Admissions**\n\nAdmission process and eligibility.")

with col2:
    st.info("💰 **Fees**\n\nFee structure and payment details.")

with col3:
    st.info("📚 **Library**\n\nLibrary timings and facilities.")

with col4:
    st.info("💼 **Placements**\n\nPlacements and internship support.")

st.divider()

# ----------------------------
# Display Previous Messages
# ----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------
# User Input
# ----------------------------
question = st.chat_input("Ask your question...")

api_key = os.getenv("GEMINI_API_KEY")

if question:

    with st.chat_message("user"):
        st.markdown(question)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    if api_key:
        try:
            client = setup_gemini(api_key)

            with st.spinner("🤖 Thinking..."):
                answer = get_response(client, question)

            with st.chat_message("assistant"):
                st.markdown(answer)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.error("Gemini API key not found.")

# ----------------------------
# Footer
# ----------------------------
st.divider()

st.caption(
    "Developed as an IBM PBEL Project | AI Chatbot for Student Support Services"
)
