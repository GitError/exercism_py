# Triangle

This module provides functions to determine the properties of a triangle based on its side lengths.

---

## 📝 Functions

### `equilateral(sides) -> bool`
Determines if a triangle is equilateral (all sides equal).

#### Parameters:
- `sides` (list or tuple): A collection of three side lengths.

#### Returns:
- `bool`: `True` if all sides are equal and greater than 0.

### `isosceles(sides) -> bool`
Determines if a triangle is isosceles (at least two sides equal).

#### Parameters:
- `sides` (list or tuple): A collection of three side lengths.

#### Returns:
- `bool`: `True` if at least two sides are equal and the triangle is valid.

### `scalene(sides) -> bool`
Determines if a triangle is scalene (all sides different).

#### Parameters:
- `sides` (list or tuple): A collection of three side lengths.

#### Returns:
- `bool`: `True` if all sides are different and the triangle is valid.

---

## ⚠️ Triangle Validation

A valid triangle must satisfy these conditions:
- All sides must have positive length
- The sum of the lengths of any two sides must be greater than the length of the remaining side

---

## 🚀 Usage

### Example 1: Checking for an Equilateral Triangle
```python
from triangle import equilateral

result = equilateral([3, 3, 3])
print(result)  # Output: True
```

### Example 2: Checking for an Isosceles Triangle
```python
from triangle import isosceles

result = isosceles([5, 5, 3])
print(result)  # Output: True
```

### Example 3: Checking for a Scalene Triangle
```python
from triangle import scalene

result = scalene([3, 4, 5])
print(result)  # Output: True
```