# Palindrome Products

This module provides functions to find the largest and smallest palindrome products within a given range of factors.

---

## 📝 Overview

A palindrome is a number that reads the same backward as forward. For example, 121 is a palindrome, but 123 is not.

This module provides functions to find:
- The **largest** palindrome that is a product of two numbers within a given range.
- The **smallest** palindrome that is a product of two numbers within a given range.

For each palindrome, the module returns both the palindrome itself and a list of factor pairs that produce it.

---

## 🚀 Usage

### Finding the Largest Palindrome Product

```python
from palindrome_products import largest

# Find the largest palindrome product with factors in range [1, 9]
palindrome, factors = largest(min_factor=1, max_factor=9)
print(palindrome)  # Output: 9
print(factors)     # Output: [[1, 9], [3, 3]]

# Find the largest palindrome product with factors in range [10, 99]
palindrome, factors = largest(min_factor=10, max_factor=99)
print(palindrome)  # Output: 9009
print(factors)     # Output: [[91, 99]]
```

### Finding the Smallest Palindrome Product

```python
from palindrome_products import smallest

# Find the smallest palindrome product with factors in range [1, 9]
palindrome, factors = smallest(min_factor=1, max_factor=9)
print(palindrome)  # Output: 1
print(factors)     # Output: [[1, 1]]

# Find the smallest palindrome product with factors in range [10, 99]
palindrome, factors = smallest(min_factor=10, max_factor=99)
print(palindrome)  # Output: 121
print(factors)     # Output: [[11, 11]] 

# No palindrome in range
palindrome, factors = smallest(min_factor=1002, max_factor=1003)
print(palindrome)  # Output: None
print(factors)     # Output: []

# Invalid range
try:
    palindrome, factors = largest(min_factor=10, max_factor=5)
except ValueError as e:
    print(e)  # Output: "min must be <= max"
```

---

## ⚙️ Implementation Details

### Algorithm

The module uses a straightforward approach:
- For `largest()`, we start from the highest possible product and work downward
- For `smallest()`, we start from the lowest possible product and work upward
- Each function stops searching once a better palindrome cannot be found

### Edge Cases Handled

- **Zero as Factor**: When `min_factor=0`, the smallest palindrome is 0 (0×0)
- **No Palindromes**: Returns `(None, [])` if no palindromes exist in the range
- **Invalid Range**: Raises `ValueError` if `min_factor > max_factor`
- **Multiple Factor Pairs**: Returns all factor pairs that produce the same palindrome

### Performance Considerations

- The implementation has a time complexity of O((max_factor - min_factor)²) in the worst case
- Early breaking from loops when better solutions cannot be found improves average performance
- Factor pairs are returned with the smaller factor listed first

---

## 🧪 Testing

The module includes comprehensive tests for all functionality and edge cases described above. Run the tests using:

```bash
python -m unittest palindrome_products_test.py
```