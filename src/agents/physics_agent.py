from src.tools.constants_lookup import get_constant
from src.gemini import ask_gemini


# This function handles physics-related queries.
def handle_physics(query):
    for keyword in ["speed of light", "gravitational constant"]:
        if keyword in query:
            return f"The {keyword} is {get_constant(keyword)}"
    return ask_gemini(query)
