
---

### **Resistor Color Duo**
```markdown
# Resistor Color Duo

This module provides a function to calculate the resistance value of a resistor using two color bands.

---

## 📝 Function

### `value(colors: list[str]) -> int`
Calculates the resistance value of a resistor based on its first two color bands.

#### Parameters:
- `colors` (list[str]): A list of color names representing the resistor's bands.

#### Returns:
- `int`: The resistance value of the resistor.

---

## 🚀 Usage

### Example 1: Resistor Value
```python
from resistor_color_duo import value

result = value(["blue", "grey"])
print(result)  # Output: 68