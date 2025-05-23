import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

# Define a function to ask the Gemini model
def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text

# Define a function to classify the subject of the question
def classify_subject(prompt):
    query = f"Classify the subject of this question into 'math' or 'physics': {prompt}"
    response = ask_gemini(query)
    if "math" in response.lower():
        return "math"
    elif "physics" in response.lower():
        return "physics"
    else:
        return "unknown"
