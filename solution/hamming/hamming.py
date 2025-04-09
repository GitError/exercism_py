def distance(strand_a, strand_b):
    """
    Calculate the Hamming distance between two DNA strands.
    
    The Hamming distance is the number of differences between two DNA strands
    of equal length. It measures the minimum number of substitutions required
    to change one string into the other.
    
    Args:
        strand_a (str): The first DNA strand
        strand_b (str): The second DNA strand
    
    Returns:
        int: The Hamming distance between the two strands
        
    Raises:
        ValueError: If the two strands have different lengths
    
    Example:
        >>> distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")
        7
    """
    # Check if strands are of equal length
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    
    # Count differences between strands
    differences = 0
    for a, b in zip(strand_a, strand_b):
        if a != b:
            differences += 1
            
    return differences
