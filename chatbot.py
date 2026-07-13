from google import genai
import time


def setup_gemini(api_key):
    return genai.Client(api_key=api_key)


def get_response(client, question):

    allowed_topics = [
        "admission", "admissions",
        "fee", "fees",
        "exam", "examination",
        "library",
        "hostel",
        "placement", "placements",
        "scholarship", "scholarships",
        "student", "students",
        "college", "university",
        "course", "courses",
        "education", "academic", "academics",
        "mba", "bba", "bca", "b.tech",
        "semester", "faculty", "campus",
        "syllabus", "attendance", "internship"
    ]

    question_lower = question.lower()

    if not any(topic in question_lower for topic in allowed_topics):
        return (
            "🎓 I am an AI Student Support Chatbot.\n\n"
            "Please ask questions related to admissions, fees, examinations, "
            "library, hostel, placements, scholarships, courses or other student services."
        )

    for _ in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=question
            )
            return response.text

        except Exception as e:
            if "503" in str(e):
                time.sleep(3)
                continue
            raise

    return "⚠️ Gemini is currently busy. Please try again after a few moments."
