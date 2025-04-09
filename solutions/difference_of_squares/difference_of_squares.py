def square_of_sum(number):
    """Calculate the square of the sum of the first 'number' natural numbers."""
    sum_n = number * (number + 1) // 2
    return sum_n ** 2


def sum_of_squares(number):
    """Calculate the sum of squares of the first 'number' natural numbers."""
    return number * (number + 1) * (2 * number + 1) // 6


def difference_of_squares(number):
    """Calculate the difference between square of sum and sum of squares."""
    return square_of_sum(number) - sum_of_squares(number)
