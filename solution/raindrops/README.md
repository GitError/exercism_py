# Raindrops

This module provides a function to convert a number into a string based on its factors.

## 🌧️ About Raindrop-Speak

Raindrop-speak is a fun way to convert numbers to strings based on their factors:
- Numbers with 3 as a factor make the sound "Pling"
- Numbers with 5 as a factor make the sound "Plang"
- Numbers with 7 as a factor make the sound "Plong"
- Numbers with multiple of these factors combine the corresponding sounds
- Numbers without these factors simply return the number as a string

This is inspired by the children's game FizzBuzz.

## 📦 Installation

The module requires Python 3.6 or higher. No external dependencies are needed.

```bash
cd raindrops

# No installation needed, just import the module
```

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
  - Combinations of the above if multiple factors apply.
  - The number itself as a string if it has none of these factors.

## 🚀 Usage

### Example 1: Single Factor
```python
from raindrops import convert

result = convert(28)  # 28 is divisible by 7
print(result)  # Output: "Plong"
```

### Example 2: Multiple Factors
```python
from raindrops import convert

result = convert(15)  # 15 is divisible by both 3 and 5
print(result)  # Output: "PlingPlang"
```

### Example 3: All Factors
```python
from raindrops import convert

result = convert(105)  # 105 is divisible by 3, 5, and 7
print(result)  # Output: "PlingPlangPlong"
```

### Example 4: No Factors
```python
from raindrops import convert

result = convert(34)  # 34 is not divisible by 3, 5, or 7
print(result)  # Output: "34"
```

## ✅ Testing

Tests are included in the `raindrops_test.py` file. Run the tests using pytest:

```bash
pytest raindrops_test.py
```