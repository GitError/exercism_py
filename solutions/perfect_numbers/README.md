# Perfect Numbers

This module provides a function to classify a number as perfect, abundant, or deficient.

---

## 📝 Function

### `classify(number: int) -> str`
Classifies a number as perfect, abundant, or deficient based on the sum of its proper divisors.

#### Parameters:
- `number` (int): The number to classify. Must be a positive integer.

#### Returns:
- `str`: The classification of the number:
  - `"perfect"`: If the sum of its proper divisors equals the number.
  - `"abundant"`: If the sum of its proper divisors is greater than the number.
  - `"deficient"`: If the sum of its proper divisors is less than the number.

#### Raises:
- `ValueError`: If the input number is not a positive integer.

---

## 🚀 Usage

### Example 1: Perfect Number
```python
from perfect_numbers import classify

result = classify(28)
print(result)  # Output: "perfect"