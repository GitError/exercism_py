# Diamond

This module provides a function to generate a diamond shape for a given letter.

---

## 📝 Function

### `rows(letter: str) -> list[str]`
Generates the rows of a diamond for the given letter.

#### Parameters:
- `letter` (str): The letter at the widest point of the diamond. Must be a single uppercase letter.

#### Returns:
- `list[str]`: A list of strings representing the diamond rows.

#### Raises:
- `ValueError`: If the input is not a single uppercase letter.

---

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