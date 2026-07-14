from google import genai
import time

def setup_gemini(api_key):
    return genai.Client(api_key=api_key)

def get_response(client, question):

    prompt = f"""
You are an AI Chatbot for Student Support Services.

Your role:
- Answer only student support and college-related questions.
- Topics include admissions, fees, examinations, library, hostel, placements, scholarships, courses, internships, academics and campus services.
- If the user asks "Who are you?", reply that you are an AI Student Support Assistant.
- If the question is about a specific college or university and the information is not available, politely ask the user to provide the institution's name.
- If the question is outside student support (weather, sports, politics, movies, celebrities, jokes, coding, science, etc.), politely reply:

"I am an AI Student Support Assistant. I can only answer questions related to admissions, fees, examinations, library, hostel, placements, scholarships, and other student support services."

User Question:
{question}
"""

    for _ in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            return response.text

        except Exception as e:
            if "503" in str(e):
                time.sleep(3)
                continue
            raise

    return "⚠️ The service is temporarily unavailable. Please try again later."
