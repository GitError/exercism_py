# Minesweeper

This module provides a function to annotate a Minesweeper board with mine counts. The board is represented as a list of strings, where each string corresponds to a row of the board. Mines are represented by `'*'`, and empty spaces are represented by `' '`.

---

## 📝 Function

### `annotate(minefield: list[str]) -> list[str]`
Annotates a Minesweeper board with the number of adjacent mines for each empty square.

#### Parameters:
- `minefield` (list[str]): A list of strings representing the Minesweeper board. Each string corresponds to a row, and each character is either `'*'` (a mine) or `' '` (an empty space).

#### Returns:
- `list[str]`: A new list of strings representing the annotated board. Each empty square is replaced with the number of adjacent mines, or left empty if there are no adjacent mines.

#### Raises:
- `ValueError`: If the input board is invalid (e.g., rows of inconsistent lengths, invalid characters).

---

## 🚀 Usage

### Example 1: Empty Board
```python
from minesweeper import annotate

minefield = []
print(annotate(minefield))
# Output: []
```

### Example 2: Empty Board with Multiple Rows
```python
from minesweeper import annotate

minefield = [
    "     ",
    "     ",
    "     "
]
print(annotate(minefield))
# Output:
# [
#     "     ",
#     "     ",
#     "     "
# ]
```

### Example 3: Board with Mines
```python
from minesweeper import annotate

minefield = [
    " * * ",
    "  *  ",
    "  *  ",
    "     "
]
print(annotate(minefield))
# Output:
# [
#     "1*3*1",
#     "13*31",
#     " 2*2 ",
#     " 111 "
# ]
```

### Example 4: Invalid Board
```python
from minesweeper import annotate

try:
    annotate(["X  * "])
except ValueError as e:
    print(e)
# Output: The board is invalid with current input.
```