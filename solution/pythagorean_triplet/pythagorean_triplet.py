def triplets_with_sum(number):
    """
    Find all Pythagorean triplets where a + b + c = number and a < b < c.
    
    :param number: The target sum
    :return: List of triplet lists [a, b, c] satisfying the conditions
    """
    triplets = []
    
    # Tighter upper bound for a: a < number/(2 + sqrt(2))
    a_max = int(number / (2 + 2**0.5))
    
    for a in range(3, a_max + 1):
        # For a given a, we have a + b + c = number and a² + b² = c²
        # Solving these equations: b = (number² - 2*number*a) / (2*(number - a))
        b_numerator = number**2 - 2*number*a
        b_denominator = 2*(number - a)
        
        # Only proceed if b would be an integer
        if b_numerator % b_denominator == 0:
            b = b_numerator // b_denominator
            c = number - a - b
            
            # Verify a < b < c and the Pythagorean theorem
            if a < b < c and a*a + b*b == c*c:
                triplets.append([a, b, c])
                
    return triplets
