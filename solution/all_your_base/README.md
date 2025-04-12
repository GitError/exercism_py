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

## 🧠 Algorithm

The conversion process follows these steps:
1. Convert the input digits from their base to decimal (base 10)
2. Convert the decimal value to the desired output base
3. Return the digits in the output base as a list

## 🔑 Key Concepts

- Number base conversions
- List manipulation
- Error handling
- Modular arithmetic
- Exponentiation

---

## 🚀 Usage Examples

### Example 1: Convert from base 10 to base 2
```python
from all_your_base import rebase

# Convert decimal 10 to binary
result = rebase(10, [1, 0], 2)
print(result)  # Output: [1, 0, 1, 0]
```

### Example 2: Convert from base 2 to base 10
```python
# Convert binary 1010 to decimal
result = rebase(2, [1, 0, 1, 0], 10)
print(result)  # Output: [1, 0]
```

### Example 3: Convert from base 16 to base 10
```python
# Convert hexadecimal 1F to decimal
result = rebase(16, [1, 15], 10)
print(result)  # Output: [3, 1]
```

### Example 4: Convert from base 10 to base 16
```python
# Convert decimal 123 to hexadecimal
result = rebase(10, [1, 2, 3], 16)
print(result)  # Output: [7, 11] (representing "7B" in hex)
```

### Example 5: Zero handling
```python
# Zero is still zero in any base
result = rebase(10, [0], 2)
print(result)  # Output: [0]
```