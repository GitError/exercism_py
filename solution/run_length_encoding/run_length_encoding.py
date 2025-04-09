def decode(string):
    """
    Decode a run-length encoded string back to its original form.
    
    Args:
        string (str): A run-length encoded string where consecutive characters 
                     are represented as a count followed by the character.
    
    Returns:
        str: The decoded string with each character repeated according to its count.
    
    Example:
        >>> decode("2AB3CD4E")
        "AABCCCDEEEE"
    """
    result = ""
    count_str = ""
    
    for char in string:
        if char.isdigit():
            count_str += char
        else:
            # If no count is specified, use 1
            count = int(count_str) if count_str else 1
            result += char * count
            count_str = ""
            
    return result


def encode(string):
    """
    Encode a string using run-length encoding.
    
    Args:
        string (str): The string to encode, containing letters A-Z (upper or lower case)
                     and whitespace.
    
    Returns:
        str: A run-length encoded string where consecutive identical characters
             are replaced by a count followed by the character. If a character
             appears only once, no count is prepended.
    
    Example:
        >>> encode("AABCCCDEEEE")
        "2AB3CD4E"
    """
    if not string:
        return ""
        
    result = ""
    count = 1
    prev_char = string[0]
    
    for char in string[1:]:
        if char == prev_char:
            count += 1
        else:
            # Only include count if greater than 1
            if count > 1:
                result += str(count)
            result += prev_char
            prev_char = char
            count = 1
    
    # Handle the last character
    if count > 1:
        result += str(count)
    result += prev_char
    
    return result
