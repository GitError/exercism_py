# Perfect Numbers

This module provides a function to classify a number as perfect, abundant, or deficient.

## 📚 What are Perfect Numbers?

In number theory, a perfect number is a positive integer that equals the sum of its positive divisors, excluding the number itself. For example, 6 is a perfect number because its divisors are 1, 2, and 3, and 1 + 2 + 3 = 6.

- **Perfect Number**: Sum of proper divisors equals the number itself
- **Abundant Number**: Sum of proper divisors exceeds the number
- **Deficient Number**: Sum of proper divisors is less than the number

## 🧮 Mathematical Definition

For a number n:
- Let S(n) be the sum of proper divisors of n (divisors excluding n itself)
- n is **perfect** when S(n) = n
- n is **abundant** when S(n) > n
- n is **deficient** when S(n) < n

---

## 📝 Function

### `classify(number: int) -> str`
Classifies a number as perfect, abundant, or deficient based on the sum of its proper divisors.

#### Parameters:
- `number` (int): The number to classify. Must be a positive integer.

#### Returns:
- `str`: The classification of the number:
  - `"perfect"`: If the sum of its proper divisors equals the number.
  - `"abundant"`: If the sum of its proper divisors is greater than the number.
  - `"deficient"`: If the sum of its proper divisors is less than the number.

#### Raises:
- `ValueError`: If the input number is not a positive integer.

---

## 🚀 Usage

### Example 1: Perfect Number
```python
from perfect_numbers import classify

result = classify(28)
print(result)  # Output: "perfect"
```

### Example 2: Abundant Number
```python
from perfect_numbers import classify

result = classify(12)
print(result)  # Output: "abundant"
# Explanation: Proper divisors of 12 are 1, 2, 3, 4, 6
# Sum: 1 + 2 + 3 + 4 + 6 = 16, which is > 12
```

### Example 3: Deficient Number
```python
from perfect_numbers import classify

result = classify(8)
print(result)  # Output: "deficient"
# Explanation: Proper divisors of 8 are 1, 2, 4
# Sum: 1 + 2 + 4 = 7, which is < 8
```

## 🔍 Interesting Facts

- The first few perfect numbers are: 6, 28, 496, 8128
- Perfect numbers are rare - only 51 are known as of 2023
- All even perfect numbers have the form 2^(n-1) * (2^n - 1), where (2^n - 1) is a prime number
- It is unknown whether any odd perfect numbers exist