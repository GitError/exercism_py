# Flatten Array

This module provides a function to flatten nested arrays of any depth into a single-level array.

## 📝 Overview

When working with nested data structures, it's often necessary to convert a multi-level structure into a flat list. The `flatten` function in this module does exactly that - it takes a nested iterable of any depth and returns a single-level list, excluding any `None` values.

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