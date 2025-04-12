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
```

### Example 2: Kiloohm Range
```python
from resistor_color_trio import value

result = value(["red", "black", "red"])
print(result)  # Output: "2 kiloohms"
```

### Example 3: Higher Multiplier
```python
from resistor_color_trio import value

result = value(["green", "brown", "orange"])
print(result)  # Output: "51 kiloohms"
```

---

## 🌈 Color Code Chart

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

---

## 📊 How Calculation Works

1. **First two bands**: Represent a two-digit number
   - First band = first digit
   - Second band = second digit

2. **Third band**: Acts as a multiplier (10^value)
   - Black (0) = 10^0 = 1
   - Brown (1) = 10^1 = 10
   - Red (2) = 10^2 = 100
   - etc.

3. **Final value** = (First two digits) × 10^(third band value)

---

## 📏 Units

Resistance values are expressed with the appropriate units:
- Less than 1,000 ohms: ohms
- 1,000 to 999,999 ohms: kiloohms
- 1,000,000 to 999,999,999 ohms: megaohms
- 1,000,000,000 or more: gigaohms

---

## 🔗 See Also

For more information on resistor color codes, check out:
- [Resistor Color Code Calculator](https://www.digikey.com/en/resources/conversion-calculators/conversion-calculator-resistor-color-code)
- [Wikipedia: Electronic Color Code](https://en.wikipedia.org/wiki/Electronic_color_code)