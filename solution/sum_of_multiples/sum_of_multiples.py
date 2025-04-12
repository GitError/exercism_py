def sum_of_multiples(limit, multiples):
    """
    Calculate the sum of all unique multiples of the given factors below a limit.
    
    This function implements an efficient solution to find all unique multiples
    of the provided factors that are less than the given limit, and returns their sum.
    
    Args:
        limit (int): The upper bound (exclusive) for finding multiples.
        multiples (list): A list of factors to find multiples for.
        
    Returns:
        int: The sum of all unique multiples of the factors below the limit.
        
    Examples:
        >>> sum_of_multiples(20, [3, 5])
        78
        >>> sum_of_multiples(10, [3, 5])
        23
    """
    # Remove zeros to avoid issues
    multiples = [m for m in multiples if m != 0]
    
    # If there are no valid multiples, return 0
    if not multiples:
        return 0
    
    # Use a set comprehension for better performance
    unique_multiples = {
        i 
        for multiple in multiples 
        for i in range(multiple, limit, multiple)
    }
    
    return sum(unique_multiples)
