import google.generativeai as genai

def setup_gemini(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-2.0-flash")

def get_response(model, question):
    response = model.generate_content(question)
    return response.text
