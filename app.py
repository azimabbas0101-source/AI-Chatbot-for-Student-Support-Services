import streamlit as st

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

if question:
    q = question.lower()

    if "admission" in q:
        st.success("Admission starts every academic session. Visit the admission office or college website for details.")

    elif "fee" in q or "fees" in q:
        st.success("You can pay fees online or at the accounts office. Contact the accounts department for exact details.")

    elif "exam" in q:
        st.success("The examination schedule is announced by the university before each semester.")

    elif "library" in q:
        st.success("The library provides books, journals and digital resources for students.")

    elif "hostel" in q:
        st.success("Hostel facilities are available. Contact the hostel office for room availability.")

    elif "placement" in q:
        st.success("The Training & Placement Cell organizes placement drives, internships and career guidance.")

    elif "scholarship" in q:
        st.success("Eligible students can apply for government and institutional scholarships.")

    else:
        st.info("Sorry, I don't have an answer for that question yet.")
