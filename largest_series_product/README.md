# Largest Series Product

This module provides a function to calculate the largest product for a contiguous substring of digits of a given size.

---

## 📝 Function

### `largest_product(series: str, size: int) -> int`
Calculates the largest product for a contiguous substring of digits of a given size.

#### Parameters:
- `series` (str): The input string of digits.
- `size` (int): The size of the substring to consider.

#### Returns:
- `int`: The largest product of the substrings.

#### Raises:
- `ValueError`: If the input is invalid:
  - `"span must not be negative"`: If the span is negative.
  - `"span must be smaller than string length"`: If the span is larger than the series length.
  - `"digits input must only contain digits"`: If the series contains non-digit characters.

---

## 🚀 Usage

### Example 1: Valid Input
```python
from largest_series_product import largest_product

result = largest_product("63915", 3)
print(result)  # Output: 162
```

### Example 2: Invalid Input
```python
try:
    result = largest_product("123", 5)
except ValueError as e:
    print(e)  # Output: "span must be smaller than string length"
```

```python
try:
    result = largest_product("12a34", 2)
except ValueError as e:
    print(e)  # Output: "digits input must only contain digits"
```