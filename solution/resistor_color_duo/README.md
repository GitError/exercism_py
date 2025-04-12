# Resistor Color Duo

This module provides a function to calculate the resistance value of a resistor using two color bands.

## 📖 Background

Resistors have color-coded bands to indicate their resistance values. Each color represents a specific number:

| Color  | Value |
|--------|-------|
| Black  | 0     |
| Brown  | 1     |
| Red    | 2     |
| Orange | 3     |
| Yellow | 4     |
| Green  | 5     |
| Blue   | 6     |
| Violet | 7     |
| Grey   | 8     |
| White  | 9     |

For a resistor with multiple bands, the first two bands indicate the first two digits of the resistance value.

---

## 📝 Function

### `value(colors: list[str]) -> int`
Calculates the resistance value of a resistor based on its first two color bands.

#### Parameters:
- `colors` (list[str]): A list of color names representing the resistor's bands.

#### Returns:
- `int`: The resistance value of the resistor (as a two-digit number).

---

## 🚀 Usage

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd resistor-color-duo

# Import in your Python project
from resistor_color_duo import value
```

### Examples

#### Example 1: Brown-Black (10)
```python
from resistor_color_duo import value

result = value(["brown", "black"])
print(result)  # Output: 10
```

#### Example 2: Blue-Grey (68)
```python
from resistor_color_duo import value

result = value(["blue", "grey"])
print(result)  # Output: 68
```

#### Example 3: Yellow-Violet (47)
```python
from resistor_color_duo import value

result = value(["yellow", "violet"])
print(result)  # Output: 47
```

## 🧪 Testing

Run the included test suite to verify functionality:

```bash
pytest resistor_color_duo_test.py
```