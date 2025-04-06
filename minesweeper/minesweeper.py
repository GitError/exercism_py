def annotate(minefield):
    """Annotate a Minesweeper board with mine counts."""
    # Handle the case of an empty board
    if not minefield:
        return []

    # Validate the input
    row_length = len(minefield[0])
    if any(len(row) != row_length for row in minefield):
        raise ValueError("The board is invalid with current input.")
    if any(char not in {'*', ' '} for row in minefield for char in row):
        raise ValueError("The board is invalid with current input.")

    # Dimensions of the board
    rows, cols = len(minefield), row_length

    # Precompute directions for adjacent cells
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # Top-left, Top, Top-right
        (0, -1),         (0, 1),     # Left, Right
        (1, -1), (1, 0), (1, 1)      # Bottom-left, Bottom, Bottom-right
    ]

    # Helper function to count adjacent mines
    def count_mines(r, c):
        return sum(
            1
            for dr, dc in directions
            if 0 <= r + dr < rows and 0 <= c + dc < cols and minefield[r + dr][c + dc] == '*'
        )

    # Annotate the board
    annotated_board = [
        ''.join(
            '*' if cell == '*' else str(count_mines(r, c)) if count_mines(r, c) > 0 else ' '
            for c, cell in enumerate(row)
        )
        for r, row in enumerate(minefield)
    ]

    return annotated_board
