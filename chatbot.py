from google import genai

def setup_gemini(api_key):
    client = genai.Client(api_key=api_key)
    return client

def get_response(client, question):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=question,
    )
    return response.text
