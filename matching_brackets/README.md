# Matching Brackets

This module provides a function to check if all brackets, braces, and parentheses in a given string are balanced and nested correctly.

---

## 📝 Function

### `is_paired(input_string: str) -> bool`

Checks if all brackets (`[]`), braces (`{}`), and parentheses (`()`) in the input string are balanced and nested correctly.

#### Parameters:
- `input_string` (str): The input string containing brackets, braces, and parentheses.

#### Returns:
- `bool`: `True` if all pairs are matched and nested correctly, `False` otherwise.

---

## 🚀 Usage

### Example 1: Balanced Brackets
```python
from matching_brackets import is_paired

result = is_paired("{[()]}")
print(result)  # Output: True