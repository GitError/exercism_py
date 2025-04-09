def factors(value):
    """
    Compute the prime factors of a given natural number.
    
    Args:
        value: A natural number
        
    Returns:
        A list of prime factors in ascending order
    """
    factor_list = []
    divisor = 2
    
    while value > 1:
        while value % divisor == 0:
            factor_list.append(divisor)
            value //= divisor
        divisor += 1
        
        # Optimization: if divisor^2 > value and value > 1, 
        # then value itself is a prime number
        if divisor * divisor > value and value > 1:
            factor_list.append(value)
            break
            
    return factor_list
