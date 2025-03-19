def square(number: int) -> int:
    """Calculate the number of grains on a specific square of the chessboard.

    :param number: int - The square number (1 to 64).
    :return: int - The number of grains on the given square.

    Raises:
        ValueError: If the square number is not between 1 and 64.
    """
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total() -> int:
    """Calculate the total number of grains on the chessboard.

    :return: int - The total number of grains on all 64 squares.
    """
    return sum(square(i) for i in range(1, 65))