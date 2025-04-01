# Armstrong Numbers

This module provides a function to determine if a given number is an Armstrong number.

---

## 📝 Function

### `is_armstrong_number(number: int) -> bool`

Determines if a number is an Armstrong number. An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

#### Parameters:
- `number` (int): The number to check.

#### Returns:
- `bool`: `True` if the number is an Armstrong number, `False` otherwise.

---

## 🚀 Usage

### Example 1: Armstrong Number
```python
from armstrong_numbers import is_armstrong_number

result = is_armstrong_number(153)
print(result)  # Output: True