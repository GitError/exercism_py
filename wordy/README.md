# Wordy

This module provides a function to parse and evaluate simple math word problems, returning the result as an integer or float.

---

## 📝 Function

### `answer(question: str) -> int | float`
Parses and evaluates a math word problem.

#### Parameters:
- `question` (str): A string containing the math word problem.

#### Returns:
- `int | float`: The result of the evaluated math word problem.

#### Raises:
- `ValueError`: If the question contains invalid syntax or unsupported operations.

---

## 🚀 Usage

### Example 1: Single Number
```python
from wordy import answer

print(answer("What is 5?"))
# Output: 5

print(answer("What is 1 plus 1?"))
# Output: 2

print(answer("What is 4 minus -12?"))
# Output: 16

print(answer("What is -3 multiplied by 25?"))
# Output: -75

print(answer("What is 33 divided by -3?"))
# Output: -11

print(answer("What is 1 plus 1 plus 1?"))
# Output: 3

print(answer("What is 1 plus 5 minus -2?"))
# Output: 8

print(answer("What is 2 multiplied by -2 multiplied by 3?"))
# Output: -12

try:
    answer("What is 1 plus?")
except ValueError as e:
    print(e)
# Output: syntax error

try:
    answer("What is 52 cubed?")
except ValueError as e:
    print(e)
# Output: unknown operation