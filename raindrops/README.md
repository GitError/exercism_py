# Raindrops

This module provides a function to convert a number into a string based on its factors.

---

## 📝 Function

### `convert(number: int) -> str`
Converts a number into a raindrop-speak string based on its factors.

#### Parameters:
- `number` (int): The number to convert.

#### Returns:
- `str`: The raindrop-speak string:
  - `"Pling"`: If the number has 3 as a factor.
  - `"Plang"`: If the number has 5 as a factor.
  - `"Plong"`: If the number has 7 as a factor.
  - The number itself as a string if it has none of these factors.

---

## 🚀 Usage

### Example 1: Raindrop Conversion
```python
from raindrops import convert

result = convert(28)
print(result)  # Output: "Plong"