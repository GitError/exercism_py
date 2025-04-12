# Grains

This module provides functions to calculate the number of grains of wheat on a chessboard given that the number doubles on each square.

## 📖 Background

The wheat and chessboard problem is a classic mathematical puzzle:
- Starting with a single grain on the first square
- Each subsequent square doubles the number of grains (2, 4, 8, 16, ...)
- A standard chessboard has 64 squares

This problem demonstrates exponential growth and can be used to visualize powers of 2.

---

## 📝 Functions

### `square(number: int) -> int`
Calculates the number of grains on a specific square.

**Parameters:**
- `number`: Integer between 1 and 64 (inclusive)

**Returns:**
- The number of grains on the given square (2^(number-1))

**Raises:**
- `ValueError`: If the square number is not between 1 and 64

### `total() -> int`
Calculates the total number of grains on the chessboard (all 64 squares).

**Returns:**
- The sum of grains on all squares (2^64 - 1)

---

## 🚀 Usage

### Example 1: Grains on a Specific Square
```python
from grains import square

# First square
result = square(1)
print(result)  # Output: 1

# Fourth square
result = square(4)
print(result)  # Output: 8

# Last square
result = square(64)
print(result)  # Output: 9223372036854775808
```

### Example 2: Total Grains on the Chessboard
```python
from grains import total

result = total()
print(result)  # Output: 18446744073709551615
```

---

## ⚙️ Installation

Clone this repository:
```bash
cd exercism_py/solution/grains
```

No additional dependencies are required beyond Python 3.6+.

---

## 💡 Performance Note

The implementation uses Python's built-in exponentiation (`**`) for efficient calculation rather than iterative doubling, making it suitable for large square numbers.

---

## ⚠️ Limitations

Due to the exponential growth, even a 64-square chessboard results in an extremely large number of grains. The 64th square alone contains over 9 quintillion grains!