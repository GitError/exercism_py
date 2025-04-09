def steps(number: int) -> int:
    """Calculate the number of steps to reach 1 using the Collatz Conjecture.

    :param number: int - The starting positive integer.
    :return: int - The number of steps to reach 1.

    Raises:
        ValueError: If the input number is not a positive integer.
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    step_count = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        step_count += 1

    return step_count