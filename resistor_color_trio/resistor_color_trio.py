def label(colors: list[str]) -> str:
    """Calculate the resistance value of a resistor based on three color bands.

    :param colors: list - A list of three color names.
    :return: str - The resistance value with the appropriate unit ("ohms", "kiloohms", "megaohms", or "gigaohms").
    """
    # List of resistor colors in order of their numerical values
    COLORS = [
        "black", "brown", "red", "orange", "yellow",
        "green", "blue", "violet", "grey", "white"
    ]

    # Decode the first two colors to get the main value
    main_value = int(f"{COLORS.index(colors[0])}{COLORS.index(colors[1])}")

    # Decode the third color to determine the number of zeros
    multiplier = 10 ** COLORS.index(colors[2])

    # Calculate the resistance value
    resistance = main_value * multiplier

    # Determine the appropriate unit
    if resistance >= 1_000_000_000:
        return f"{resistance // 1_000_000_000} gigaohms"
    elif resistance >= 1_000_000:
        return f"{resistance // 1_000_000} megaohms"
    elif resistance >= 1_000:
        return f"{resistance // 1_000} kiloohms"
    return f"{resistance} ohms"