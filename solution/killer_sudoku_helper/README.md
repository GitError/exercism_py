# Killer Sudoku Helper

A Python utility library that generates valid combinations of digits for Killer Sudoku cages, helping players solve these challenging puzzles more efficiently.

## What is Killer Sudoku?

Killer Sudoku is a variant of regular Sudoku with additional constraints:
- The puzzle is divided into "cages" (regions with dashed lines)
- Each cage has a target sum that the digits within must add up to
- No digit can be repeated within a cage (following standard Sudoku rules)
- Standard Sudoku rules still apply (each row, column, and 3×3 box must contain digits 1-9 without repetition)

## 📝 Function Reference

### `combinations(target: int, size: int, exclude: list[int]) -> list[list[int]]`

Generates all valid combinations of digits for a Killer Sudoku cage, adhering to both cage constraints and Sudoku rules.

#### Parameters:
- `target` (int): The sum that the digits in the cage must add up to
- `size` (int): The number of cells in the cage (how many digits to use)
- `exclude` (list[int]): Digits to exclude from consideration due to Sudoku constraints (e.g., digits already present in the same row, column, or box)

#### Returns:
- `list[list[int]]`: A sorted list of valid combinations, where each combination is represented as a sorted list of integers

#### Constraints:
- Only uses digits 1-9 (standard Sudoku digits)
- No digit repetition within combinations
- Each combination sums to the target value
- Each combination contains exactly the specified number of digits

---

## 🚀 Usage Examples

### Example 1: Single Digit Cage
```python
from killer_sudoku_helper import combinations

print(combinations(1, 1, []))
# Output: [[1]]
```
In this example, we're looking for a single digit with value 1, with no excluded digits.

### Example 2: Multi-Digit Cage
```python
print(combinations(7, 3, []))
# Output: [[1, 2, 4]]
```
Here, we need three digits that sum to 7. The only possible combination is [1, 2, 4].

### Example 3: Two-Digit Cage
```python
print(combinations(10, 2, []))
# Output: [[1, 9], [2, 8], [3, 7], [4, 6]]
```
For a two-digit cage summing to 10, there are four possible combinations.

### Example 4: With Excluded Digits
```python
print(combinations(10, 2, [1, 4]))
# Output: [[2, 8], [3, 7]]
```
When we exclude digits 1 and 4 (perhaps because they appear elsewhere in the same row, column, or box), only two combinations remain.

## 📋 Installation

No special installation required. Simply import the module in your Python project:

```python
from killer_sudoku_helper import combinations
```

## 📝 Note

- The function returns an empty list if no valid combinations exist
- All returned combinations are sorted in ascending order
- The function assumes valid inputs (target, size, and exclude values are reasonable for Killer Sudoku)