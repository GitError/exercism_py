from itertools import combinations

def combinations(target, size, exclude):
    """Generate all valid combinations of digits for a Killer Sudoku cage.

    :param target: int - The sum of the digits in the cage.
    :param size: int - The number of digits in the cage.
    :param exclude: list[int] - Digits to exclude due to Sudoku constraints.
    :return: list[list[int]] - Sorted list of valid combinations.
    """
    # Digits available for the cage (1-9 excluding the excluded digits)
    available_digits = set(range(1, 10)) - set(exclude)

    # Generate and filter combinations in one step
    return sorted(
        [list(combo) for combo in combinations(available_digits, size) if sum(combo) == target]
    )
