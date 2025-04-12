# Resistor Color Expert

This module provides functions to calculate the resistance value of a resistor using advanced color band logic. It handles resistors with 1, 4, or 5 color bands and provides the resistance value with appropriate units and tolerance.

## 🔍 Background

Resistors are electronic components that restrict the flow of electrical current. They are marked with colored bands to indicate their resistance value and tolerance. The color coding system is standardized and allows electronics professionals to quickly identify resistor values.

---

## 📝 Functions

### `resistor_label(colors: list[str]) -> str`
Calculates the resistance value of a resistor based on its color bands, including tolerance.

#### Parameters:
- `colors` (list[str]): A list of color names representing the resistor's bands.
  - For 1-band resistors: `[color]`
  - For 4-band resistors: `[first, second, multiplier, tolerance]`
  - For 5-band resistors: `[first, second, third, multiplier, tolerance]`

#### Returns:
- `str`: The resistance value of the resistor with appropriate unit and tolerance.

#### Units:
- Values < 1,000 are returned in ohms
- Values 1,000 to 999,999 are returned in kiloohms
- Values 1,000,000 to 999,999,999 are returned in megaohms
- Values ≥ 1,000,000,000 are returned in gigaohms

---

## 🎨 Color Code Reference

| Color  | Value | Multiplier | Tolerance |
|--------|-------|------------|-----------|
| Black  | 0     | ×10⁰       | -         |
| Brown  | 1     | ×10¹       | ±1%       |
| Red    | 2     | ×10²       | ±2%       |
| Orange | 3     | ×10³       | -         |
| Yellow | 4     | ×10⁴       | -         |
| Green  | 5     | ×10⁵       | ±0.5%     |
| Blue   | 6     | ×10⁶       | ±0.25%    |
| Violet | 7     | ×10⁷       | ±0.1%     |
| Grey   | 8     | ×10⁸       | ±0.05%    |
| White  | 9     | ×10⁹       | -         |
| Gold   | -     | ×10⁻¹      | ±5%       |
| Silver | -     | ×10⁻²      | ±10%      |
| None   | -     | -          | ±20%      |

---

## 🚀 Usage Examples

### Example 1: 4-Band Resistor
```python
from resistor_color_expert import resistor_label

result = resistor_label(["red", "violet", "yellow", "gold"])
print(result)  # Output: "27 kiloohms ±5%"
```

### Example 2: 5-Band Resistor
```python
result = resistor_label(["brown", "green", "black", "red", "brown"])
print(result)  # Output: "150 kiloohms ±1%"
```

### Example 3: Single-Band Resistor
```python
result = resistor_label(["black"])
print(result)  # Output: "0 ohms"
```

### Example 4: High-Precision Resistor
```python
result = resistor_label(["blue", "grey", "violet", "orange", "violet"])
print(result)  # Output: "6.87 megaohms ±0.1%"
```

## 🧪 Testing

Run the tests using pytest:

```bash
pytest resistor_color_expert_test.py
```