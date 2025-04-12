# Resistor Color

This module provides functions to work with resistor color codes, helping you determine the numerical value of resistors based on their color bands.

## 📊 Background

Electronic resistors have colored bands that represent their resistance value. Each color corresponds to a specific number:

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

## 📝 Functions

### `color_code(color: str) -> int`
Returns the numerical value associated with a particular color band.

#### Parameters:
- `color` (str): The color name to look up.

#### Returns:
- `int`: The numerical value of the color.

### `colors() -> list[str]`
Returns a list of all possible resistor colors.

#### Returns:
- `list[str]`: A list of color names in order of their numerical values.

### `value(colors: list[str]) -> int`
Calculates the resistance value of a resistor based on its color bands.

#### Parameters:
- `colors` (list[str]): A list of color names representing the resistor's bands.

#### Returns:
- `int`: The resistance value of the resistor.

## 🚀 Usage Examples

### Example 1: Get a single color's value
```python
from resistor_color import color_code

result = color_code("blue")
print(result)  # Output: 6
```

### Example 2: Get all color codes
```python
from resistor_color import colors

color_list = colors()
print(color_list)  # Output: ["black", "brown", "red", ...]
```

### Example 3: Calculate resistor value
```python
from resistor_color import value

result = value(["brown", "black"])
print(result)  # Output: 10

result = value(["red", "violet"])
print(result)  # Output: 27
```

## 🔗 Related Topics
- Resistors and electronic components
- Color coding systems in electronics
- Ohm's law
