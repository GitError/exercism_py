def flatten(iterable):
    """
    Flatten a nested iterable of any depth.
    
    Args:
        iterable: A potentially nested iterable (list, tuple, etc.)
        
    Returns:
        A flattened list containing all non-None elements from the input
    """
    # Pre-allocate the result list to reduce reallocations
    result = []
    
    # Use a stack-based approach instead of recursion to avoid call stack overhead
    stack = [iterable]
    
    while stack:
        current = stack.pop()
        
        if current is None:
            continue
            
        if isinstance(current, (list, tuple)):
            # Add items in reverse order so they're processed in original order
            stack.extend(reversed(current))
        else:
            result.append(current)
    
    return result
