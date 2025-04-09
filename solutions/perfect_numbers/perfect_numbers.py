def classify(number: int) -> str:
    """Classify a number as perfect, abundant, or deficient.

    :param number: int - A positive integer to classify.
    :return: str - The classification of the input integer ("perfect", "abundant", or "deficient").

    Raises:
        ValueError: If the input number is not a positive integer.
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    # Calculate the aliquot sum (sum of factors excluding the number itself)
    aliquot_sum = sum(factor for factor in range(1, number) if number % factor == 0)

    # Classify the number based on its aliquot sum
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"