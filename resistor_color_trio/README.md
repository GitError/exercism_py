# Resistor Color Trio

This module provides a function to calculate the resistance value of a resistor using three color bands.

---

## 📝 Function

### `value(colors: list[str]) -> str`
Calculates the resistance value of a resistor based on its first three color bands.

#### Parameters:
- `colors` (list[str]): A list of color names representing the resistor's bands.

#### Returns:
- `str`: The resistance value of the resistor, including the unit (e.g., "kiloohms").

---

## 🚀 Usage

### Example 1: Resistor Value
```python
from resistor_color_trio import value

result = value(["orange", "orange", "black"])
print(result)  # Output: "33 ohms"