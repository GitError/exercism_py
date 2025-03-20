def value(colors: list[str]) -> int:
    """Calculate the resistance value of a resistor based on the first two color bands.

    :param colors: list - A list of color names.
    :return: int - The resistance value as a two-digit number.
    """
    # List of resistor colors in order of their numerical values
    COLORS = [
        "black", "brown", "red", "orange", "yellow",
        "green", "blue", "violet", "grey", "white"
    ]

    # Get the numerical values of the first two colors and combine them
    return int(f"{COLORS.index(colors[0])}{COLORS.index(colors[1])}")