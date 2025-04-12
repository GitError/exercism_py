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
```

### Example 2: Equal Lists
```python
result = sublist([1, 2, 3], [1, 2, 3])
print(result)  # Output: "equal"
```

### Example 3: Superlist Check
```python
result = sublist([1, 2, 3], [2])
print(result)  # Output: "superlist"
```

### Example 4: Unequal Lists
```python
result = sublist([1, 2, 3], [4, 5, 6])
print(result)  # Output: "unequal"
```

---

## 🔍 Edge Cases

- **Empty Lists**: An empty list is considered a sublist of any list.
  ```python
  result = sublist([], [1, 2, 3])
  print(result)  # Output: "sublist"
  ```

- **Identical Empty Lists**: Two empty lists are considered equal.
  ```python
  result = sublist([], [])
  print(result)  # Output: "equal"
  ```

- **Non-Consecutive Matches**: The elements must appear consecutively to be considered a sublist.
  ```python
  result = sublist([1, 3], [1, 2, 3])
  print(result)  # Output: "unequal"
  ```

---

## 📦 Installation

No special installation required. Just import the function:

```python
from sublist import sublist
```

---

## 📚 References

- [Enumerated Types in Python](https://en.wikipedia.org/wiki/Enumerated_type)
- [Python List Operations](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)