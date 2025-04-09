def slices(series, length):
    """
    Extract all contiguous substrings of specified length from the input series.
    
    Args:
        series (str): A string of characters (typically digits) to extract slices from
        length (int): The length of each slice to extract
    
    Returns:
        list: A list containing all possible contiguous substrings of the specified length
    
    Raises:
        ValueError: If the series is empty, if length is negative or zero,
                   or if the requested length exceeds the series length
    """
    # Validate inputs
    if not series:
        raise ValueError("series cannot be empty")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    
    # Generate all valid slices
    result = []
    for i in range(len(series) - length + 1):
        result.append(series[i:i + length])
    
    return result
