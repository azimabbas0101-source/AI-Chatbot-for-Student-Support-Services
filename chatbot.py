from google import genai

def setup_gemini(api_key):
    client = genai.Client(api_key=api_key)
    return client


def get_response(client, question):

    prompt = f"""
You are an AI Chatbot for Student Support Services.

Your job is to answer ONLY questions related to:

- Admissions
- Fees
- Examination
- Library
- Hostel
- Placements
- Scholarships
- Academics
- Courses
- College facilities
- Student services
- Career guidance
- MBA, BBA, BCA, B.Tech and other educational queries

Rules:
1. Give clear, simple and helpful answers.
2. Use easy English.
3. If the question is NOT related to education or student support, politely reply:

"I'm an AI Student Support Chatbot. Please ask questions related to admissions, fees, examinations, library, hostel, placements, scholarships, academics or other student services."

Student Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text
