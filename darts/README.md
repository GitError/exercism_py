
---

### **Darts**
```markdown
# Darts

This module provides a function to calculate the score of a dart throw based on its position on the dartboard.

---

## 📝 Function

### `score(x: float, y: float) -> int`
Calculates the score of a dart throw based on its position.

#### Parameters:
- `x` (float): The x-coordinate of the dart.
- `y` (float): The y-coordinate of the dart.

#### Returns:
- `int`: The score based on the distance from the center:
  - 10 points for a distance ≤ 1.
  - 5 points for a distance ≤ 5.
  - 1 point for a distance ≤ 10.
  - 0 points otherwise.

---

## 🚀 Usage

### Example 1: Dart Score
```python
from darts import score

result = score(0, 0)
print(result)  # Output: 10