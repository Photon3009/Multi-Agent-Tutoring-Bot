from agents.math_agent import handle_math
from agents.physics_agent import handle_physics
from gemini import classify_subject

# This function handles the user's query by classifying it and delegating to the appropriate agent.
def handle_query(user_query):
    subject = classify_subject(user_query)  # e.g., via Gemini API
    if subject == "math":
        return handle_math(user_query)
    elif subject == "physics":
        return handle_physics(user_query)
    else:
        return "Sorry, I can only help with Math or Physics right now."
