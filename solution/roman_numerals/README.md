# Roman Numerals Converter

A Python module that converts Arabic numerals to Roman numerals following traditional rules.

## Overview

This module provides a function to convert numbers from Arabic numerals (0-9) to Roman numerals, which use the letters M, D, C, L, X, V, and I to represent values.

## Roman Numeral Rules

Roman numerals follow these basic rules:
- Letters are represented by values:
  - I = 1
  - V = 5
  - X = 10
  - L = 50
  - C = 100
  - D = 500
  - M = 1000
  
- A letter can't be used more than three times in succession. 
- Instead of 4 consecutive identical symbols, we use subtraction with the next higher value:
  - 4 is not IIII, but IV (5-1)
  - 9 is not VIIII, but IX (10-1)
  - 40 is XL (50-10)
  - 90 is XC (100-10)
  - 400 is CD (500-100)
  - 900 is CM (1000-100)

- Symbols must be arranged in descending order of value from left to right, with the exceptions of the special subtraction cases.

## Usage

```python
from roman_numerals import roman

# Convert numbers to Roman numerals
print(roman(1))    # Output: I
print(roman(4))    # Output: IV
print(roman(9))    # Output: IX
print(roman(42))   # Output: XLII
print(roman(1984)) # Output: MCMLXXXIV
print(roman(3999)) # Output: MMMCMXCIX
```

## Constraints
- This implementation works for numbers from 1 to 3,999 (MMMCMXCIX).
- Numbers outside this range will raise a ValueError.

## Running Tests

To run the tests:

```bash
python roman_numerals_test.py
```
