# Diamond

This module provides a function to generate a diamond shape for a given letter, following specific pattern rules.

## 🔍 Challenge

The diamond challenge requires you to create a diamond pattern where:
- The first and last row contain an 'A', centered in the row
- All rows have exactly the same width (determined by the input letter)
- All rows after the first have two identical letters, one at the beginning and one at the end
- The diamond is horizontally and vertically symmetric
- The diamond width equals its height
- The letters form a diamond shape starting with 'A' at the top, increasing until the input letter, then decreasing back to 'A'

## 📝 Function

### `rows(letter: str) -> list[str]`
Generates the rows of a diamond for the given letter.

#### Parameters:
- `letter` (str): The letter at the widest point of the diamond. Must be a single uppercase letter.

#### Returns:
- `list[str]`: A list of strings representing the diamond rows.

#### Raises:
- `ValueError`: If the input is not a single uppercase letter.

## 🚀 Usage

### Example 1: Diamond for 'A'
```python
from diamond import rows

result = rows('A')
print("\n".join(result))
# Output:
# A
```

### Example 2: Diamond for 'C'
```python
from diamond import rows

result = rows('C')
print("\n".join(result))
# Output:
#   A  
#  B B 
# C   C
#  B B 
#   A
```

### Example 3: Diamond for 'E'
```python
from diamond import rows

result = rows('E')
print("\n".join(result))
# Output:
#     A    
#    B B   
#   C   C  
#  D     D 
# E       E
#  D     D 
#   C   C  
#    B B   
#     A
```

## 📊 Diamond Structure

The diamond for letter 'C' visualized with spaces and letter positions marked:

```
  A    <- 2 spaces before A, 2 spaces after A
 B B   <- 1 space before first B, 1 space between Bs, 1 space after last B
C   C  <- 0 spaces before first C, 3 spaces between Cs, 0 spaces after last C
 B B   <- 1 space before first B, 1 space between Bs, 1 space after last B
  A    <- 2 spaces before A, 2 spaces after A
```

## 📋 Edge Cases

- Input 'A' produces a single-row diamond with just 'A'
- Invalid inputs (non-letters, lowercase letters, multiple characters) raise ValueError

## 🛠️ Installation

No special installation required beyond Python 3.6+.

## 🧪 Testing

Run the tests with pytest:

```bash
pytest diamond_test.py
```

## 📚 Pattern Rules

For any letter 'X' at position n in the alphabet (A=0, B=1, etc.):
- The width of the diamond is 2n+1
- The outside spaces on each side of a letter decrease as you go from A to X
- The inside spaces between identical letters increase by 2 for each step from A to X