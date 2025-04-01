# Resistor Color

This module provides a function to determine the numerical value of a resistor based on its color.

---

## 📝 Function

### `value(colors: list[str]) -> int`
Calculates the resistance value of a resistor based on its color bands.

#### Parameters:
- `colors` (list[str]): A list of color names representing the resistor's bands.

#### Returns:
- `int`: The resistance value of the resistor.

---

## 🚀 Usage

### Example 1: Resistor Value
```python
from resistor_color import value

result = value(["brown", "black"])
print(result)  # Output: 10
