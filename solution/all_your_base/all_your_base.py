def rebase(input_base: int, digits: list[int], output_base: int) -> list[int]:
    """Convert a sequence of digits in one base to another base.

    :param input_base: int - The base of the input digits.
    :param digits: list - A list of digits in the input base.
    :param output_base: int - The base to convert the digits to.
    :return: list - A list of digits in the output base.

    Raises:
        ValueError: If input_base or output_base is less than 2, or if digits are invalid.
    """
    # Validate input base
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    # Validate output base
    if output_base < 2:
        raise ValueError("output base must be >= 2")

    # Validate digits
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    # Convert input digits to base 10
    decimal_value = sum(d * (input_base ** i) for i, d in enumerate(reversed(digits)))

    # Handle the special case where the decimal value is 0
    if decimal_value == 0:
        return [0]

    # Convert base 10 to the output base
    output_digits = []
    while decimal_value > 0:
        output_digits.append(decimal_value % output_base)
        decimal_value //= output_base

    # Reverse the output digits to get the correct order
    return output_digits[::-1]