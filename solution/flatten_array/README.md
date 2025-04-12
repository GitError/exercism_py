# Flatten Array

This module provides a function to flatten nested arrays of any depth into a single-level array.

## 📝 Overview

When working with nested data structures, it's often necessary to convert a multi-level structure into a flat list. The `flatten` function in this module does exactly that - it takes a nested iterable of any depth and returns a single-level list, excluding any `None` values.

## ⚙️ Installation

Clone this repository and import the module in your Python project:

```python
from flatten_array import flatten
```

## 🚀 Usage

```python
from flatten_array import flatten

# Basic usage
nested_list = [1, [2, 6, None], [[None, [4]], 5]]
flat_list = flatten(nested_list)
print(flat_list)  # Output: [1, 2, 6, 4, 5]

# Works with different types of nesting
deeply_nested = [0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]
print(flatten(deeply_nested))  # Output: [0, 2, 2, 3, 8, 100, 4, 50, -2]

# Removes all None values
only_nones = [None, [[[None]]], None, None, [[None, None], None], None]
print(flatten(only_nones))  # Output: []

# Works with tuples too
mixed_types = [1, (2, [3, 4]), 5]
print(flatten(mixed_types))  # Output: [1, 2, 3, 4, 5]

# Additional examples
print(flatten([1, [2, 3], 4]))  # Output: [1, 2, 3, 4]
print(flatten([1, [2, None, 3], 4]))  # Output: [1, 2, 3, 4]
```

## 💡 Implementation Details

The `flatten` function uses an iterative stack-based approach rather than recursion, which has several advantages:

1. **Efficiency**: Avoids the overhead of function calls in deeply nested structures
2. **Memory safety**: Prevents stack overflow for extremely deep nested structures
3. **Performance**: Pre-allocates result list to reduce memory reallocations

### Algorithm Complexity

- **Time Complexity**: O(n), where n is the total number of elements across all nesting levels
- **Space Complexity**: O(n) for the output list, plus O(d) for the stack where d is the maximum nesting depth

### Iterative vs. Recursive Approach

While a recursive approach might be more intuitive:

```python
def flatten_recursive(iterable):
    result = []
    for item in iterable:
        if item is None:
            continue
        elif isinstance(item, (list, tuple)):
            result.extend(flatten_recursive(item))
        else:
            result.append(item)
    return result
```

The iterative approach used in this implementation offers better performance for deeply nested structures and avoids potential stack overflow errors.

## 🧪 Testing

The module includes comprehensive unit tests covering various scenarios including:
- Empty lists
- Lists with various nesting depths
- Lists containing None values
- Mixed data types
- Tuple inputs

Run the tests using:

```bash
python -m unittest flatten_array_test
```