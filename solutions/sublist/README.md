# Sublist

This module provides a function to compare two lists and determine their relationship.

---

## 📝 Function

### `sublist(list_one: list, list_two: list) -> str`
Determines the relationship between two lists.

#### Parameters:
- `list_one` (list): The first list.
- `list_two` (list): The second list.

#### Returns:
- `str`: The relationship between the lists:
  - `"equal"`: If the lists are identical.
  - `"sublist"`: If the first list is a sublist of the second.
  - `"superlist"`: If the first list is a superlist of the second.
  - `"unequal"`: If the lists are unrelated.

---

## 🚀 Usage

### Example 1: Sublist Check
```python
from sublist import sublist

result = sublist([1, 2], [1, 2, 3])
print(result)  # Output: "sublist"