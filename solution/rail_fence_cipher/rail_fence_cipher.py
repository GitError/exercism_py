def encode(message, rails):
    """
    Encode a message using the rail fence cipher.
    
    The rail fence cipher works by writing the message in a zig-zag pattern across
    a specified number of "rails", then reading off the cipher by rows.
    
    Args:
        message (str): The message to encode
        rails (int): The number of rails (rows) to use in the cipher
        
    Returns:
        str: The encoded message
    """
    # Remove spaces if any
    message = message.replace(" ", "")
    
    # Create the rail fence pattern
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1  # 1 for down, -1 for up
    
    # Distribute characters in zig-zag pattern
    for char in message:
        fence[rail].append(char)
        rail += direction
        
        # Change direction if we hit the top or bottom rail
        if rail == 0 or rail == rails - 1:
            direction *= -1
    
    # Read off the encoded message
    return ''.join([''.join(rail) for rail in fence])


def decode(encoded_message, rails):
    """
    Decode a message that was encoded using the rail fence cipher.
    
    This reverses the rail fence cipher by:
    1. Calculating how many characters belong in each rail
    2. Reconstructing the rails from the encoded message
    3. Reading the original message by traversing the zig-zag pattern
    
    Args:
        encoded_message (str): The encoded message to decode
        rails (int): The number of rails (rows) used in the cipher
        
    Returns:
        str: The decoded (original) message
    """
    if not encoded_message:
        return ""
        
    # Calculate the length of each rail
    fence_pattern = [0] * rails
    rail = 0
    direction = 1
    
    # Count how many characters go in each rail
    for _ in range(len(encoded_message)):
        fence_pattern[rail] += 1
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    
    # Fill the rails with the encoded message
    fence = []
    index = 0
    for rail_size in fence_pattern:
        fence.append(encoded_message[index:index + rail_size])
        index += rail_size
    
    # Reconstruct the original message by following the zig-zag
    result = []
    rail = 0
    direction = 1
    rail_indices = [0] * rails
    
    for _ in range(len(encoded_message)):
        result.append(fence[rail][rail_indices[rail]])
        rail_indices[rail] += 1
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1
    
    return ''.join(result)
