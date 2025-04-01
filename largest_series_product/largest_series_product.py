def largest_product(series, size):
    """Calculate the largest product for a contiguous substring of digits of a given size.

    :param series: str - The input string of digits.
    :param size: int - The size of the substring to consider.
    :return: int - The largest product of the substrings.
    :raises ValueError: If the input is invalid.
    """
    if size < 0:
        raise ValueError("span must not be negative")
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    if not series.isdigit() and series != "":
        raise ValueError("digits input must only contain digits")

    max_product = 0
    for i in range(len(series) - size + 1):
        product = 1
        for digit in series[i:i + size]:
            product *= int(digit)
        max_product = max(max_product, product)

    return max_product
