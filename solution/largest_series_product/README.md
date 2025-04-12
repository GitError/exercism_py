# Largest Series Product

This module provides a function to calculate the largest product for a contiguous substring of digits of a given size.

## 📋 Problem Description

Given a string of digits, find the largest product for a contiguous substring of digits of length `n`. 

For example, for the input `"1234"` and `n=2`, the largest product would be `12` (from the substring `"34"`).

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

## 🧠 Algorithm

The function uses a sliding window approach:
1. Validate input parameters
2. Iterate through each possible substring of the given size
3. Calculate the product of digits in each substring
4. Track the maximum product found

Time complexity: O(n * k) where n is the length of the series and k is the size of the substring.
Space complexity: O(1) as we only store intermediate results.

---

## ⚙️ Implementation Details

The function handles several edge cases:
- Empty strings
- Zero span (returns 1)
- Span equal to series length
- Series containing zeros

---

## 🚀 Usage Examples

### Example 1: Basic Usage

```python
from largest_series_product import largest_product

result = largest_product("63915", 3)
print(result)  # Output: 162
```

### Example 2: Series with Zeros

```python
result = largest_product("102030405", 2)
print(result)  # Output: 20
```

### Example 3: Edge Cases

```python
print(largest_product("", 0))  # Output: 1
print(largest_product("12345", 0))  # Output: 1
print(largest_product("12345", 5))  # Output: 120
```

### Example 4: Error Handling

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

```python
try:
    result = largest_product("12345", -1)
except ValueError as e:
    print(e)  # Output: "span must not be negative"
```

---

## 🧪 Testing

The module includes comprehensive tests covering:
- Various valid inputs with different spans
- Edge cases (empty strings, zero span)
- Error cases (invalid characters, negative span, span too large)
- Performance with large inputs

Run tests using pytest:

```bash
pytest largest_series_product_test.py -v
```