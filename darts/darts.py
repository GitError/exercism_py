def score(x: float, y: float) -> int:
    """Calculate the points scored in a single toss of a Darts game.

    :param x: float - The x-coordinate of the dart's landing point.
    :param y: float - The y-coordinate of the dart's landing point.
    :return: int - The score based on where the dart lands.
    """
    # Calculate the distance from the center (0, 0)
    distance = (x**2 + y**2)**0.5

    # Determine the score based on the distance
    if distance <= 1:
        return 10  # Inner circle
    elif distance <= 5:
        return 5  # Middle circle
    elif distance <= 10:
        return 1  # Outer circle
    else:
        return 0  # Outside the target