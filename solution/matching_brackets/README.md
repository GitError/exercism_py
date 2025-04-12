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

# More examples of balanced brackets
print(is_paired("{}"))  # Output: True
print(is_paired("function() { return [1, 2, 3]; }"))  # Output: True
print(is_paired("a + b - (c * d) / e"))  # Output: True
```

### Example 2: Unbalanced Brackets
```python
from matching_brackets import is_paired

# Missing closing bracket
print(is_paired("("))  # Output: False

# Mismatched brackets
print(is_paired("{[}]"))  # Output: False

# Incorrectly nested brackets
print(is_paired("{[(])}"))  # Output: False
```

### Example 3: Empty String
```python
from matching_brackets import is_paired

# Empty string is considered balanced
print(is_paired(""))  # Output: True
```

---

## 🧮 Algorithm

The function uses a stack-based approach to check for balanced brackets:

1. Iterate through each character in the input string
2. If an opening bracket (`{`, `[`, `(`) is found, push it onto the stack
3. If a closing bracket (`}`, `]`, `)`) is found:
   - Check if the stack is empty (no matching opening bracket) → return `False`
   - Pop the top element from the stack and check if it matches the closing bracket
   - If no match → return `False`
4. After processing all characters, check if the stack is empty
   - Empty stack → all brackets were matched → return `True`
   - Non-empty stack → some opening brackets weren't closed → return `False`

---

## 🔍 Edge Cases

- Empty string: Considered balanced (returns `True`)
- String with no brackets: Considered balanced (returns `True`)
- Unmatched opening brackets: Considered unbalanced (returns `False`)
- Unmatched closing brackets: Considered unbalanced (returns `False`)
- Incorrectly nested brackets: Considered unbalanced (returns `False`)