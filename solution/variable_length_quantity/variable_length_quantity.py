def encode(numbers):
    """
    Encode a list of integers using Variable Length Quantity (VLQ) encoding.
    
    In VLQ encoding, only the 7 least significant bits of each byte are used to store data.
    The most significant bit (bit 7) is used as a continuation flag - it's set to 1 for all
    bytes except the last one in a sequence.
    
    Args:
        numbers: A list of integers to encode
        
    Returns:
        A list of bytes representing the VLQ-encoded integers
        
    Examples:
        >>> encode([0x0])
        [0x0]
        >>> encode([0x80])
        [0x81, 0x0]
        >>> encode([0x2000])
        [0xC0, 0x0]
    """
    result = []
    
    for number in numbers:
        # Special case for 0
        if number == 0:
            result.append(0)
            continue
            
        # Convert to VLQ bytes
        bytes_list = []
        while number > 0:
            # Add the 7 least significant bits with continuation bit cleared
            bytes_list.insert(0, number & 0x7F)
            number >>= 7
        
        # Set continuation bit on all but the last byte
        for i in range(len(bytes_list) - 1):
            bytes_list[i] |= 0x80
            
        result.extend(bytes_list)
    
    return result


def decode(bytes_):
    """
    Decode a list of VLQ-encoded bytes into the original integers.
    
    In VLQ encoding, each byte uses 7 bits for the value and the 8th bit (MSB) 
    as a continuation flag. If the MSB is set (1), it indicates that more bytes follow.
    If the MSB is clear (0), it indicates the end of the encoded integer.
    
    Args:
        bytes_: A list of bytes in VLQ format
        
    Returns:
        A list of decoded integers
        
    Raises:
        ValueError: If the sequence is incomplete (if the last byte has continuation bit set)
        
    Examples:
        >>> decode([0x7F])
        [0x7F]
        >>> decode([0xC0, 0x0])
        [0x2000]
        >>> decode([0x81, 0x80, 0x0])
        [0x4000]
    """
    if not bytes_:
        raise ValueError("incomplete sequence")
        
    result = []
    current = 0
    
    for i, byte in enumerate(bytes_):
        # Check if this is a continuation byte (high bit set)
        is_continuation = byte & 0x80
        
        # Add the 7 lower bits to our accumulator
        current = (current << 7) | (byte & 0x7F)
        
        # If high bit is not set, this is the end of a number
        if not is_continuation:
            result.append(current)
            current = 0
        # If we're at the last byte and it's a continuation byte, the sequence is incomplete
        elif i == len(bytes_) - 1:
            raise ValueError("incomplete sequence")
    
    return result
