def prime(number):
    """
    Return the nth prime number.
    
    Args:
        number: A positive integer n to find the nth prime.
        
    Returns:
        The nth prime number.
        
    Raises:
        ValueError: If number is less than 1.
    """
    if number < 1:
        raise ValueError("there is no zeroth prime")
    
    count = 0
    candidate = 1
    
    while count < number:
        candidate += 1
        if is_prime(candidate):
            count += 1
            
    return candidate


def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n: An integer to check.
        
    Returns:
        True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
            
    return True
