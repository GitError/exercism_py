def commands(binary_str):
    """
    Convert a binary string to a sequence of actions for the secret handshake.
    
    Args:
        binary_str: A string representing a binary number (e.g. "00011")
        
    Returns:
        A list of strings representing the actions in the secret handshake
    """
    # Define the actions corresponding to each bit position
    actions = ["wink", "double blink", "close your eyes", "jump"]
    
    # Convert binary string to an integer and ensure we only use the last 5 bits
    binary_int = int(binary_str, 2) & 0b11111
    
    # Check if we need to reverse the order (5th bit)
    reverse = binary_int & 0b10000
    
    # Process the first 4 bits
    result = [actions[i] for i in range(4) if binary_int & (1 << i)]
    
    # Reverse if needed
    if reverse:
        result.reverse()
    
    return result
