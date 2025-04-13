# Spiral Matrix

## Description

This exercise requires you to create a square matrix of a given size, filled with natural numbers in a clockwise spiral pattern.

The matrix starts with 1 in the top-left corner and proceeds in a clockwise inward spiral pattern, incrementing the number for each position.

## Examples

### Spiral matrix of size 3
```
1 2 3
8 9 4
7 6 5
```

### Spiral matrix of size 4
```
 1  2  3  4
12 13 14  5
11 16 15  6
10  9  8  7
```

## Implementation

The solution uses directional vectors to navigate through the matrix following a clockwise pattern:
- Right: (0, 1)
- Down: (1, 0)
- Left: (0, -1)
- Up: (-1, 0)

The algorithm changes direction whenever it encounters a boundary or an already filled cell.

## Usage

```python
from spiral_matrix import spiral_matrix

# Create a 3x3 spiral matrix
matrix = spiral_matrix(3)
print(matrix)  # [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
```

## Testing

Run the provided tests with:

```bash
python -m unittest spiral_matrix_test.py
```
