# Triangle

This module provides a function to determine the type of a triangle based on its side lengths.

---

## 📝 Function

### `type_of_triangle(a: int, b: int, c: int) -> str`
Determines the type of a triangle.

#### Parameters:
- `a` (int): The length of the first side.
- `b` (int): The length of the second side.
- `c` (int): The length of the third side.

#### Returns:
- `str`: The type of the triangle:
  - `"equilateral"`: All sides are equal.
  - `"isosceles"`: Two sides are equal.
  - `"scalene"`: All sides are different.

---

## 🚀 Usage

### Example 1: Triangle Type
```python
from triangle import type_of_triangle

result = type_of_triangle(3, 3, 3)
print(result)  # Output: "equilateral"