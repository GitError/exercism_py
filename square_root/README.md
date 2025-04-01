# Square Root

This module provides a function to calculate the square root of a given positive whole number without relying on external math libraries.

---

## 📝 Function

### `square_root(number: int) -> int`

Calculates the square root of a given positive whole number using a binary search approach.

#### Parameters:
- `number` (int): The number to find the square root of. Must be a positive whole number.

#### Returns:
- `int`: The square root of the number if it is a perfect square.

#### Raises:
- `ValueError`: If the input is not a positive whole number.
- `ValueError`: If the number does not have an integer square root.

---

## 🚀 Usage

### Example 1: Perfect Square
```python
from square_root import square_root

result = square_root(16)
print(result)  # Output: 4