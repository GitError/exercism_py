def egg_count(display_value):
    """
    Count the number of 1 bits in the binary representation of a number.
    
    :param display_value: An integer representing the display value
    :return: The count of 1 bits in the binary representation
    """
    count = 0
    while display_value > 0:
        # Check if the least significant bit is 1
        if display_value & 1:
            count += 1
        # Shift right to check the next bit
        display_value >>= 1
    return count
