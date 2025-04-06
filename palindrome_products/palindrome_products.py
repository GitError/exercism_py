def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    largest_palindrome = None
    factors = []

    # Start from highest possible product and work down
    for i in range(max_factor, min_factor - 1, -1):
        for j in range(max_factor, min_factor - 1, -1):
            product = i * j
            
            # If we've found a palindrome and it's smaller than our current largest,
            # we can break out of this inner loop
            if largest_palindrome is not None and product < largest_palindrome:
                break
                
            if is_palindrome(product):
                if largest_palindrome is None or product > largest_palindrome:
                    largest_palindrome = product
                    factors = [[i, j]]
                elif product == largest_palindrome:
                    factors.append([i, j])
    
    return (largest_palindrome, factors)


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    smallest_palindrome = None
    factors = []

    # Start from lowest possible product and work up
    for i in range(min_factor, max_factor + 1):
        for j in range(min_factor, max_factor + 1):
            product = i * j
            
            # If we've found a palindrome and it's larger than our current smallest,
            # we can break out of this inner loop
            if smallest_palindrome is not None and product > smallest_palindrome:
                break
                
            if is_palindrome(product):
                if smallest_palindrome is None or product < smallest_palindrome:
                    smallest_palindrome = product
                    factors = [[i, j]]
                elif product == smallest_palindrome:
                    factors.append([i, j])
    
    return (smallest_palindrome, factors)


def is_palindrome(number):
    """Check if a number is a palindrome (reads the same forwards and backwards)."""
    return str(number) == str(number)[::-1]
