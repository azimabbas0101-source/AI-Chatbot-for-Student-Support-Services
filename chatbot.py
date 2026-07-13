from google import genai

def setup_gemini(api_key):
    client = genai.Client(api_key=api_key)
    return client


def get_response(client, question):

    # Student Support Topics
    allowed_topics = [
        "admission", "admissions",
        "fee", "fees",
        "exam", "examination", "result",
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

    # Check if question is related to student support
    is_allowed = False

    for topic in allowed_topics:
        if topic in question.lower():
            is_allowed = True
            break

    if not is_allowed:
        return (
            "🎓 I am an AI Student Support Chatbot.\n\n"
            "Please ask questions related to:\n"
            "• Admissions\n"
            "• Fees\n"
            "• Examination\n"
            "• Library\n"
            "• Hostel\n"
            "• Placements\n"
            "• Scholarships\n"
            "• Courses\n"
            "• Student Services"
        )

    # Generate AI Response
    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=question
    )

    return response.text
