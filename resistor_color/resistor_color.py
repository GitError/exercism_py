# List of resistor colors in order of their numerical values
COLORS = [
    "black", "brown", "red", "orange", "yellow",
    "green", "blue", "violet", "grey", "white"
]

def color_code(color: str) -> int:
    """Return the numerical value associated with a particular color band.

    :param color: str - The color to look up.
    :return: int - The numerical value of the color.
    """
    return COLORS.index(color)


def colors() -> list[str]:
    """Return a list of all possible resistor colors.

    :return: list - A list of color names in order of their numerical values.
    """
    return COLORS
