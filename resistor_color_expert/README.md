# Resistor Color Expert

This module provides functions to calculate the resistance value of a resistor using advanced color band logic.

---

## 📝 Function

### `value(colors: list[str]) -> str`
Calculates the resistance value of a resistor based on its color bands, including tolerance.

#### Parameters:
- `colors` (list[str]): A list of color names representing the resistor's bands.

#### Returns:
- `str`: The resistance value of the resistor, including the unit and tolerance.

---

## 🚀 Usage

### Example 1: Resistor Value
```python
from resistor_color_expert import value

result = value(["red", "violet", "yellow", "gold"])
print(result)  # Output: "27.4k ohms ±5%"