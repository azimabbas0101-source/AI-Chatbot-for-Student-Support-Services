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
This chatbot helps students with common college-related queries.
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
# Main Title
# ----------------------------
st.title("🎓 AI Chatbot for Student Support Services")

st.markdown("""
Welcome to the **AI Student Support Assistant**.

Ask questions related to:

- Admissions
- Fees
- Examinations
- Library
- Hostel
- Placements
- Scholarships
""")

# ----------------------------
# Feature Cards
# ----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("📝 **Admissions**\n\nAdmission process and eligibility.")

with col2:
    st.info("💰 **Fees**\n\nFee structure and payment information.")

with col3:
    st.info("📚 **Library**\n\nLibrary services and facilities.")

with col4:
    st.info("💼 **Placements**\n\nPlacement and internship support.")

st.divider()

# ----------------------------
# Display Chat History
# ----------------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ----------------------------
# Chat Input
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

            error_message = str(e)

            if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
                st.warning("""
⚠️ Daily AI Request Limit Reached

The chatbot has reached today's free Gemini API quota.

Please try again after the daily quota resets.
""")

            elif "503" in error_message:
                st.warning("""
⚠️ AI Service Temporarily Busy

Gemini is currently experiencing high traffic.

Please try again after a few minutes.
""")

            else:
                st.error(f"""
⚠️ Unexpected Error

{error_message}
""")

    else:
        st.error("⚠️ Gemini API key not found.")

# ----------------------------
# Footer
# ----------------------------
st.divider()

st.caption(
    "Developed as an IBM PBEL Project | AI Chatbot for Student Support Services"
)
