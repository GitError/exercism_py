def saddle_points(matrix):
    """
    Find saddle points in a matrix.
    
    A saddle point is a position in a matrix where the value is:
    - The maximum value in its row
    - The minimum value in its column
    
    Args:
        matrix (list): A list of lists representing a 2D matrix of integers.
                      All rows must be of equal length.
    
    Returns:
        list: A list of dictionaries containing the positions of saddle points.
              Each dictionary has 'row' and 'column' keys with 1-indexed values.
    
    Raises:
        ValueError: If the matrix is irregular (rows have different lengths).
    
    Examples:
        >>> matrix = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
        >>> saddle_points(matrix)
        [{'row': 2, 'column': 1}]
    """
    # Check for empty matrix
    if not matrix:
        return []
    
    # Check for irregular matrix
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("irregular matrix")
    
    # Pre-calculate row maxima and column minima
    row_maxima = [max(row) for row in matrix]
    col_minima = [min(matrix[r][c] for r in range(len(matrix))) for c in range(len(matrix[0]))]
    
    result = []
    
    # Find saddle points using the pre-calculated values
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == row_maxima[i] and value == col_minima[j]:
                result.append({"row": i + 1, "column": j + 1})
    
    return result
