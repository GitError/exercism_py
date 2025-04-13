def transpose(text):
    """
    Transpose the input text (convert rows to columns and columns to rows).
    
    Rules for transposition:
    - Pad shorter rows to the left with spaces
    - Don't pad to the right
    - Preserve all input characters in the output
    
    Args:
        text (str): Input text to be transposed, with rows separated by newlines
        
    Returns:
        str: Transposed text with original columns as rows
        
    Examples:
        >>> transpose("ABC\nDEF")
        'AD\nBE\nCF'
        
        >>> transpose("ABC\nDE")
        'AD\nBE\nC'
    """
    if not text:
        return ""
    
    lines = text.split('\n')
    # Pre-calculate line lengths for better efficiency
    line_lengths = [len(line) for line in lines]
    max_length = max(line_lengths, default=0)
    
    # Initialize the result list with proper size
    result = []
    
    # Process column by column
    for j in range(max_length):
        column = []
        for i, line in enumerate(lines):
            if j < line_lengths[i]:
                # Add the character at this position
                column.append(line[j])
            elif any(j < length for length in line_lengths[i+1:]):
                # This is a "hole" in the matrix that needs a space
                column.append(' ')
            # No need to append anything if we're past the end of all remaining rows
        
        result.append(''.join(column))
    
    return '\n'.join(result)
