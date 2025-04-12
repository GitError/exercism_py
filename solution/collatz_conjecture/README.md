# Collatz Conjecture

This module provides a function to calculate the number of steps required to reach 1 using the Collatz Conjecture.

## 📖 What is the Collatz Conjecture?

The Collatz Conjecture is a famous unsolved problem in mathematics. It states that for any positive integer:
- If the number is even, divide it by 2
- If the number is odd, multiply it by 3 and add 1
- Repeat this process until you reach 1

The conjecture proposes that no matter which positive integer you start with, you will always eventually reach 1.

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

### Algorithm
```
1. If number is 1, return 0 (already at the target)
2. If number is even, divide by 2
3. If number is odd, multiply by 3 and add 1
4. Increment the step counter
5. Repeat steps 2-4 until number is 1
```

---

## 🚀 Usage

### Example 1: Collatz Steps for 12
```python
from collatz_conjecture import steps

result = steps(12)
print(result)  # Output: 9
```

### Example 2: Step-by-Step Breakdown
For number = 12:
```
Step 1: 12 is even, 12 ÷ 2 = 6
Step 2: 6 is even, 6 ÷ 2 = 3
Step 3: 3 is odd, 3 × 3 + 1 = 10
Step 4: 10 is even, 10 ÷ 2 = 5
Step 5: 5 is odd, 5 × 3 + 1 = 16
Step 6: 16 is even, 16 ÷ 2 = 8
Step 7: 8 is even, 8 ÷ 2 = 4
Step 8: 4 is even, 4 ÷ 2 = 2
Step 9: 2 is even, 2 ÷ 2 = 1
```
Total steps: 9

### Example 3: Handling Errors
```python
try:
    steps(0)  # Will raise ValueError
except ValueError as e:
    print(f"Error: {e}")  # Output: Error: Only positive integers are allowed
```

---

## 🧪 Testing

The module includes a comprehensive test suite using pytest:

```bash
pytest collatz_conjecture_test.py
```

Tests cover:
- Various positive integers (including 1, which requires 0 steps)
- Large numbers (e.g., 1,000,000)
- Error handling for invalid inputs (zero and negative values)

---

## ⚠️ Performance Considerations

For very large numbers, the algorithm may take a significant number of steps to complete. The implementation uses basic integer operations which are efficient, but be aware of potential long computation times for extremely large inputs.