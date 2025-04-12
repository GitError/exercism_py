# Square Root

This module provides a function to calculate the square root of a given positive whole number without relying on external math libraries.

---

## 📝 Function

### `square_root(number: int) -> int`

Calculates the square root of a given positive whole number using a binary search approach.

#### Parameters:
- `number` (int): The number to find the square root of. Must be a positive whole number.

#### Returns:
- `int`: The square root of the number if it is a perfect square.

#### Raises:
- `ValueError`: If the input is not a positive whole number.
- `ValueError`: If the number does not have an integer square root.

#### Implementation Details:
- Uses an optimized binary search algorithm to find the square root
- Time complexity: O(log n)
- Space complexity: O(1)

---

## 🚀 Usage

### Example 1: Perfect Square
```python
from square_root import square_root

result = square_root(16)
print(result)  # Output: 4
```

### Example 2: Larger Perfect Square
```python
from square_root import square_root

result = square_root(10000)
print(result)  # Output: 100
```

### Example 3: Error Handling
```python
from square_root import square_root

try:
    result = square_root(-5)
except ValueError as e:
    print(e)  # Output: Input must be a positive whole number.
    
try:
    result = square_root(8)
except ValueError as e:
    print(e)  # Output: No integer square root found for the given number.
```

---

## ⚠️ Edge Cases

- **Negative numbers**: The function will raise a ValueError with the message "Input must be a positive whole number."
- **Zero**: The function will raise a ValueError with the message "Input must be a positive whole number."
- **Non-perfect squares**: The function will raise a ValueError with the message "No integer square root found for the given number."

---

## 🧪 Testing

Run the included tests to verify the function works as expected:

```bash
pytest square_root_test.py
```

The tests cover perfect squares, large numbers, and error handling for invalid inputs.