# Collatz Conjecture

This module provides a function to calculate the number of steps required to reach 1 using the Collatz Conjecture.

---

## 📝 Function

### `steps(number: int) -> int`
Calculates the number of steps required to reach 1 using the Collatz Conjecture.

#### Parameters:
- `number` (int): The starting number. Must be a positive integer.

#### Returns:
- `int`: The number of steps required to reach 1.

#### Raises:
- `ValueError`: If the input number is not a positive integer.

---

## 🚀 Usage

### Example 1: Collatz Steps
```python
from collatz_conjecture import steps

result = steps(12)
print(result)  # Output: 9