
---

### **Lists**
```markdown
# Lists

This module provides functions to perform basic operations on lists.

---

## 📝 Functions

### `add_item(lst: list, item: any) -> list`
Adds an item to a list.

### `remove_item(lst: list, item: any) -> list`
Removes an item from a list.

---

## 🚀 Usage

### Example 1: Add Item
```python
from lists import add_item

result = add_item([1, 2, 3], 4)
print(result)  # Output: [1, 2, 3, 4]