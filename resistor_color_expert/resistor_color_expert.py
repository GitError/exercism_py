def resistor_label(colors: list[str]) -> str:
    """Calculate the resistance value and tolerance of a resistor based on its color bands.

    :param colors: list - A list of 1, 4, or 5 color names.
    :return: str - The resistance value with the appropriate unit and tolerance.
    """
    # List of resistor colors in order of their numerical values
    COLORS = [
        "black", "brown", "red", "orange", "yellow",
        "green", "blue", "violet", "grey", "white"
    ]

    # Tolerance values for the last band
    TOLERANCE = {
        "grey": "±0.05%",
        "violet": "±0.1%",
        "blue": "±0.25%",
        "green": "±0.5%",
        "brown": "±1%",
        "red": "±2%",
        "gold": "±5%",
        "silver": "±10%"
    }

    # Handle single-band resistors (special case)
    if len(colors) == 1:
        if colors[0] == "black":
            return "0 ohms"
        raise ValueError("Invalid single-band resistor color")

    # Decode the first two or three colors to get the main value
    if len(colors) == 4:
        main_value = int("".join(str(COLORS.index(color)) for color in colors[:2]))
    elif len(colors) == 5:
        main_value = int("".join(str(COLORS.index(color)) for color in colors[:3]))
    else:
        raise ValueError("Invalid number of bands")

    # Decode the multiplier
    multiplier = 10 ** COLORS.index(colors[-2])

    # Calculate the resistance value
    resistance = main_value * multiplier

    # Determine the tolerance
    tolerance = TOLERANCE.get(colors[-1], "")

    # Determine the appropriate unit
    if resistance >= 1_000_000_000:
        resistance_value = resistance / 1_000_000_000
        unit = "gigaohms"
    elif resistance >= 1_000_000:
        resistance_value = resistance / 1_000_000
        unit = "megaohms"
    elif resistance >= 1_000:
        resistance_value = resistance / 1_000
        unit = "kiloohms"
    else:
        resistance_value = resistance
        unit = "ohms"

    # Format the resistance value to remove unnecessary decimals
    if isinstance(resistance_value, float) and resistance_value.is_integer():
        resistance_value = int(resistance_value)
    return f"{resistance_value} {unit} {tolerance}"