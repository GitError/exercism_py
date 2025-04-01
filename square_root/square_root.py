def square_root(number):
    """Calculate the square root of a given positive whole number.

    :param number: int - The number to find the square root of.
    :return: int - The square root of the number.
    """
    if number < 1:
        raise ValueError("Input must be a positive whole number.")

    low, high = 1, number
    while low <= high:
        mid = (low + high) // 2
        square = mid * mid

        if square == number:
            return mid
        elif square < number:
            low = mid + 1
        else:
            high = mid - 1

    raise ValueError("No integer square root found for the given number.")
