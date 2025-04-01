# All Your Base

This module provides a function to convert a sequence of digits from one base to another.

## 📝 Function

### `rebase(input_base: int, digits: list[int], output_base: int) -> list[int]`

Converts a sequence of digits in one base to another base.

#### Parameters:
- `input_base` (int): The base of the input digits. Must be greater than or equal to 2.
- `digits` (list[int]): A list of digits in the input base. Each digit must satisfy `0 <= digit < input_base`.
- `output_base` (int): The base to convert the digits to. Must be greater than or equal to 2.

#### Returns:
- `list[int]`: A list of digits in the output base.

#### Raises:
- `ValueError`: If `input_base` or `output_base` is less than 2, or if the digits are invalid.

---

## 🚀 Usage

### Example 1: Convert from base 10 to base 2
```python
from all_your_base import rebase

result = rebase(10, [1, 0], 2)
print(result)  # Output: [1, 0, 1, 0]