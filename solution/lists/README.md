# Lists

This module provides functions to perform basic operations on lists.

---

## 📝 Functions

### `add_item(lst: list, item: any) -> list`
Adds an item to a list.

### `remove_item(lst: list, item: any) -> list`
Removes an item from a list.

### `get_item(lst: list, index: int) -> any`
Gets an item from a list at the specified index.

### `list_length(lst: list) -> int`
Returns the length of the list.

---

## 🚀 Usage

### Example 1: Add Item
```python
from lists import add_item

result = add_item([1, 2, 3], 4)
print(result)  # Output: [1, 2, 3, 4]
```

### Example 2: Remove Item
```python
from lists import remove_item

result = remove_item([1, 2, 3], 2)
print(result)  # Output: [1, 3]
```

### Example 3: Get Item
```python
from lists import get_item

result = get_item([1, 2, 3], 1)
print(result)  # Output: 2
```

### Example 4: List Length
```python
from lists import list_length

result = list_length([1, 2, 3])
print(result)  # Output: 3
```

---

## 💻 Installation

```bash
# Navigate to the project directory
cd lists

# Install dependencies (if any)
pip install -r requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request