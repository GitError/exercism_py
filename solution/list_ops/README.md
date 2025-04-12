# List Operations

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This module provides implementations of basic list operations such as appending, concatenating, filtering, mapping, folding, and reversing lists. These operations are implemented without relying on external libraries or imports.

## 📋 Table of Contents
- [Installation](#installation)
- [Functions](#functions)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## 🔧 Installation

No installation required. Simply copy the `list_ops.py` file into your project.

```python
from list_ops import append, concat, filter, length, map, foldl, foldr, reverse
```

---

## 📝 Functions

### `append(list1: list, list2: list) -> list`
Appends all items from `list2` to the end of `list1` without modifying the original lists.

#### Example:

```python
append([1, 2], [3, 4])  # Output: [1, 2, 3, 4]
append([], [1, 2, 3])   # Output: [1, 2, 3]
append([1, 2, 3], [])   # Output: [1, 2, 3]
```

### `concat(lists: list[list]) -> list`

Concatenates a series of lists into one flattened list. Does not flatten nested lists.

#### Example:

```python
concat([[1, 2], [3], [], [4, 5, 6]])  # Output: [1, 2, 3, 4, 5, 6]
concat([])  # Output: []
```

### `filter(function: callable, lst: list) -> list`

Filters items in the list based on the predicate function, returning only items for which the function returns True.

#### Example:

```python
filter(lambda x: x % 2 == 1, [1, 2, 3, 5])  # Output: [1, 3, 5]
filter(lambda x: x > 10, [5, 8, 15, 12])    # Output: [15, 12]
```

### `length(lst: list) -> int`
Returns the total number of items in the list without using Python's built-in `len()` function.

#### Example:

```python
length([1, 2, 3, 4])  # Output: 4
length([])            # Output: 0
```

### `map(function: callable, lst: list) -> list`
Applies a function to each item in the list and returns the results as a new list.

#### Example:

```python
map(lambda x: x + 1, [1, 3, 5, 7])    # Output: [2, 4, 6, 8]
map(lambda x: x * 2, [0, 2, 4])       # Output: [0, 4, 8]
```

### `foldl(function: callable, lst: list, initial: any) -> any`
Reduces the list from the left using the given function and initial value. The accumulator is the first parameter to the function.

#### Example:

```python
foldl(lambda acc, el: el + acc, [1, 2, 3, 4], 5)  # Output: 15
foldl(lambda acc, el: el / acc, [1, 2, 3, 4], 24) # Output: 64
```

### `foldr(function: callable, lst: list, initial: any) -> any`
Reduces the list from the right using the given function and initial value. The accumulator is the first parameter to the function.

#### Example:

```python
foldr(lambda acc, el: el + acc, [1, 2, 3, 4], 5)  # Output: 15
foldr(lambda acc, el: el / acc, [1, 2, 3, 4], 24) # Output: 9
```

### `reverse(lst: list) -> list`
Returns a new list with all items in reversed order without modifying the original list.

#### Example:

```python
reverse([1, 3, 5, 7])                  # Output: [7, 5, 3, 1]
reverse([[1, 2], [3], [], [4, 5, 6]])  # Output: [[4, 5, 6], [], [3], [1, 2]]
```

## 🧪 Usage

Here's a more complete example demonstrating the use of multiple functions:

```python
from list_ops import append, concat, filter, length, map, foldl, foldr, reverse

# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6]

# Get only odd numbers
odds = filter(lambda x: x % 2 == 1, numbers)  # [1, 3, 5]

# Double each odd number
doubled_odds = map(lambda x: x * 2, odds)  # [2, 6, 10]

# Sum the doubled odds using fold
sum_doubled_odds = foldl(lambda acc, x: acc + x, doubled_odds, 0)  # 18

print(f"Original: {numbers}")
print(f"Odds: {odds}")
print(f"Doubled odds: {doubled_odds}")
print(f"Sum: {sum_doubled_odds}")
```

## 🧪 Testing

To run the tests:

```bash
python list_ops_test.py
```

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
