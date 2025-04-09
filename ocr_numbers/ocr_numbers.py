def convert(input_grid):
    """
    Convert OCR numbers from a grid format to their decimal representation.
    
    Each digit in the OCR format is represented by a 3x4 grid of pipes, underscores, and spaces.
    Multiple digits are parsed row by row, and multiple rows are joined with commas.
    
    Args:
        input_grid (list): A list of strings representing the OCR grid.
                          Each digit is 3 columns wide and 4 rows high.
    
    Returns:
        str: The decimal representation of the OCR numbers, with rows separated by commas.
    
    Raises:
        ValueError: If the number of rows is not a multiple of 4,
                   or if the rows have different lengths,
                   or if the number of columns is not a multiple of 3.
    """
    # Validate input
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    
    row_length = len(input_grid[0])
    for row in input_grid:
        if len(row) != row_length:
            raise ValueError("Input rows don't have the same length")
        if len(row) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")
    
    # Define the patterns for each digit
    patterns = {
        ' _ | ||_|   ': '0',
        '     |  |   ': '1',
        ' _  _||_    ': '2',
        ' _  _| _|   ': '3',
        '   |_|  |   ': '4',
        ' _ |_  _|   ': '5',
        ' _ |_ |_|   ': '6',
        ' _   |  |   ': '7',
        ' _ |_||_|   ': '8',
        ' _ |_| _|   ': '9'
    }
    
    # Process each group of 4 rows
    result = []
    num_rows = len(input_grid)
    num_digits_per_row = row_length // 3
    
    for i in range(0, num_rows, 4):
        row_result = ""
        
        # Process each digit in the current row group
        for j in range(0, row_length, 3):
            # Extract the 3x4 grid for this digit
            digit_grid = (
                input_grid[i][j:j+3] +
                input_grid[i+1][j:j+3] +
                input_grid[i+2][j:j+3] +
                input_grid[i+3][j:j+3]
            )
            
            # Convert the digit grid to a number
            row_result += patterns.get(digit_grid, '?')
        
        result.append(row_result)
    
    # Join the rows with commas
    return ','.join(result)

