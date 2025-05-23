from sympy import symbols, Eq, solve, sympify
from tools.calculator import evaluate_expression
from gemini import ask_gemini
import re

# This function handles math-related queries.
def handle_math(query):
    try:
        if "=" in query:
            x = symbols("x")
            left_side, right_side = query.split("=")

            # Insert * between number and variable (e.g., 2x → 2*x)
            left_side = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", left_side)
            right_side = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", right_side)

            # Remove any stray characters (like '?')
            left_side = re.sub(r"[^\dx+\-*/(). ]", "", left_side)
            right_side = re.sub(r"[^\dx+\-*/(). ]", "", right_side)

            # Use sympify instead of eval for safety
            equation = Eq(sympify(left_side), sympify(right_side))
            solution = solve(equation, x)
            return f"x = {solution[0]}"
    except Exception as e:
        print(f"Failed to solve algebraic equation: {e}")

    # Try evaluating as arithmetic expression
    match = re.findall(r"[\d+\-*/(). ]+", query)
    if match:
        try:
            return str(evaluate_expression(match[0]))
        except Exception:
            pass

    return ask_gemini(query)
