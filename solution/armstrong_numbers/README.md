# Armstrong Numbers

This module provides a function to determine if a given number is an Armstrong number.

## 📘 What is an Armstrong Number?

An Armstrong number (also known as a narcissistic number, pluperfect digital invariant, or pluperfect number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

For example:
- 153 is an Armstrong number because: 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
- 370 is an Armstrong number because: 3³ + 7³ + 0³ = 27 + 343 + 0 = 370
- 9474 is an Armstrong number because: 9⁴ + 4⁴ + 7⁴ + 4⁴ = 6561 + 256 + 2401 + 256 = 9474

---

## 📝 Function

### `is_armstrong_number(number: int) -> bool`

Determines if a number is an Armstrong number. An Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

#### Parameters:
- `number` (int): The number to check.

#### Returns:
- `bool`: `True` if the number is an Armstrong number, `False` otherwise.

---

## 🚀 Usage

### Example 1: Armstrong Number
```python
from armstrong_numbers import is_armstrong_number

result = is_armstrong_number(153)
print(result)  # Output: True
```

### Example 2: Another Armstrong Number
```python
from armstrong_numbers import is_armstrong_number

result = is_armstrong_number(370)
print(result)  # Output: True
```

### Example 3: Non-Armstrong Number
```python
from armstrong_numbers import is_armstrong_number

result = is_armstrong_number(100)
print(result)  # Output: False
```

### Example 4: Single-Digit Number
```python
from armstrong_numbers import is_armstrong_number

# All single-digit numbers are Armstrong numbers
result = is_armstrong_number(5)
print(result)  # Output: True
```

---

## 💻 Implementation Details

The implementation uses the following approach:
1. Convert the number to a string to access individual digits
2. Calculate the number of digits (for determining the power)
3. Calculate the sum of each digit raised to the power of the number of digits
4. Compare the sum with the original number

---

## 📚 Additional Resources

- [Armstrong Numbers on Wikipedia](https://en.wikipedia.org/wiki/Narcissistic_number)
- [OEIS sequence A005188](https://oeis.org/A005188) - List of Armstrong numbers

---