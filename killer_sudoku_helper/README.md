# Killer Sudoku Helper

This module provides a helper function to generate all valid combinations of digits for a Killer Sudoku cage, adhering to the rules of Killer Sudoku.

---

## 📝 Function

### `combinations(target: int, size: int, exclude: list[int]) -> list[list[int]]`
Generates all valid combinations of digits for a Killer Sudoku cage.

#### Parameters:
- `target` (int): The sum of the digits in the cage.
- `size` (int): The number of digits in the cage.
- `exclude` (list[int]): Digits to exclude due to Sudoku constraints.

#### Returns:
- `list[list[int]]`: A sorted list of valid combinations, where each combination is represented as a list of integers.

---

## 🚀 Usage

### Example 1: Single Digit Cage
```python
from killer_sudoku_helper import combinations

print(combinations(1, 1, []))
# Output: [[1]]
```

### Example 2: Multi-Digit Cage
```python
print(combinations(7, 3, []))
# Output: [[1, 2, 4]]
```

### Example 3: Two-Digit Cage
```python
print(combinations(10, 2, []))
# Output: [[1, 9], [2, 8], [3, 7], [4, 6]]

print(combinations(10, 2, [1, 4]))
# Output: [[2, 8], [3, 7]]