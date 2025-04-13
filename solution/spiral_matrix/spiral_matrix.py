def spiral_matrix(size):
    """
    Generate a square matrix of a given size, filled with natural numbers in a clockwise spiral pattern.
    
    Args:
        size (int): The size of the square matrix (both width and height)
        
    Returns:
        list: A square matrix of the given size filled with natural numbers in a spiral pattern
              starting from 1 in the top-left corner and proceeding clockwise inward
              
    Examples:
        >>> spiral_matrix(3)
        [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        
        >>> spiral_matrix(4)
        [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
    """
    # Handle edge case
    if size <= 0:
        return []
        
    # Initialize the matrix with zeros
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    
    # Set boundary variables (more intuitive than checking matrix values)
    row_start, row_end = 0, size - 1
    col_start, col_end = 0, size - 1
    num = 1
    
    while row_start <= row_end and col_start <= col_end:
        # Fill top row from left to right
        for col in range(col_start, col_end + 1):
            matrix[row_start][col] = num
            num += 1
        row_start += 1
        
        # Fill right column from top to bottom
        for row in range(row_start, row_end + 1):
            matrix[row][col_end] = num
            num += 1
        col_end -= 1
        
        # Check if still within boundaries
        if row_start <= row_end:
            # Fill bottom row from right to left
            for col in range(col_end, col_start - 1, -1):
                matrix[row_end][col] = num
                num += 1
            row_end -= 1
        
        if col_start <= col_end:
            # Fill left column from bottom to top
            for row in range(row_end, row_start - 1, -1):
                matrix[row][col_start] = num
                num += 1
            col_start += 1
    
    return matrix
