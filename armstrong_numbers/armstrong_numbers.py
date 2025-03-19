def is_armstrong_number(number: int) -> bool:
    """Determine if a number is an Armstrong number.

    :param number: int - The number to check.
    :return: bool - True if the number is an Armstrong number, False otherwise.

    An Armstrong number is a number that is the sum of its own digits each raised
    to the power of the number of digits.
    """
    digits = [int(digit) for digit in str(number)]
    power = len(digits)
    return number == sum(digit ** power for digit in digits)