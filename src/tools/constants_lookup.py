# These are some common physical constants and their values.
CONSTANTS = {
    "speed of light": "299,792,458 m/s",
    "gravitational constant": "6.674×10⁻¹¹ N·m²/kg²",
}


# This function retrieves the value of a constant based on its name.
def get_constant(name):
    return CONSTANTS.get(name.lower(), "Constant not found.")
