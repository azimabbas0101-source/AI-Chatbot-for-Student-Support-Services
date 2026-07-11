import streamlit as st

st.set_page_config(
    page_title="AI Student Support Chatbot",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Student Support Chatbot")

st.write("Welcome to the AI Student Support Chatbot.")

st.write("This chatbot will help students with:")

st.markdown("""
- 📚 Admission
- 💰 Fees
- 📝 Examination
- 🏠 Hostel
- 📖 Library
- 💼 Placements
- 🎓 Scholarships
""")

question = st.text_input("Ask your question:")

if st.button("Submit"):
    if question == "":
        st.warning("Please enter a question.")
    else:
        st.success("Your question has been received.")
        st.write("AI response will be added in the next step.")
