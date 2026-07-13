from google import genai

def setup_gemini(api_key):
    client = genai.Client(api_key=api_key)
    return client


def get_response(client, question):

    allowed_topics = [
        "admission", "admissions", "fee", "fees",
        "exam", "examination", "library", "hostel",
        "placement", "placements", "scholarship",
        "scholarships", "college", "student",
        "course", "courses", "education",
        "mba", "bba", "bca", "b.tech", "university",
        "semester", "syllabus", "faculty", "campus"
    ]

    if not any(word in question.lower() for word in allowed_topics):
        return (
            "🎓 I'm an AI Student Support Chatbot.\n\n"
            "Please ask questions related to:\n"
            "• Admissions\n"
            "• Fees\n"
            "• Examinations\n"
            "• Library\n"
            "• Hostel\n"
            "• Placements\n"
            "• Scholarships\n"
            "• Courses\n"
            "• Student Services"
        )

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=question
    )

    return response.text
