# Binary Search

This module provides a function to find the index of a value in a sorted list using the binary search algorithm.

---

## 📝 Function

### `find(search_list: list, value: int) -> int`
Finds the index of a value in a sorted list using binary search.

#### Parameters:
- `search_list` (list): A sorted list of elements to search.
- `value` (int): The value to find in the list.

#### Returns:
- `int`: The index of the value in the list.

#### Raises:
- `ValueError`: If the value is not in the list.

---

## 🚀 Usage

### Example 1: Value Found
```python
from binary_search import find

search_list = [4, 8, 12, 16, 23, 28, 32]
result = find(search_list, 23)
print(result)  # Output: 4
```

### Example 2: Value Not Found
```python
try:
    result = find([1, 2, 3, 4, 5], 6)
except ValueError as e:
    print(e)  # Output: "value not in array"
```