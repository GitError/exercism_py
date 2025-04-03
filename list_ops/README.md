# List Operations

This module provides implementations of basic list operations such as appending, concatenating, filtering, mapping, folding, and reversing lists. These operations are implemented without relying on external libraries or imports.

---

## 📝 Functions

### `append(list1: list, list2: list) -> list`
Appends all items from `list2` to the end of `list1`.

#### Example:

```python
append([1, 2], [3, 4])  # Output: [1, 2, 3, 4]
```

### `concat(lists: list[list]) -> list`

Concatenates a series of lists into one flattened list.

#### Example:

```python
concat([[1, 2], [3], [], [4, 5, 6]])  # Output: [1, 2, 3, 4, 5, 6]
```

### `filter(function: callable, lst: list) -> list`

Filters items in the list based on the predicate function.

#### Example:

```python
filter(lambda x: x % 2 == 1, [1, 2, 3, 5])  # Output: [1, 3, 5]
```

### `length(lst: list) -> int`
Returns the total number of items in the list.

#### Example:

```python
length([1, 2, 3, 4])  # Output: 4
```

### `map(function: callable, lst: list) -> list`
Applies a function to each item in the list and returns the results.

#### Example:

```python
map(lambda x: x + 1, [1, 3, 5, 7])  # Output: [2, 4, 6, 8]
```

### `foldl(function: callable, lst: list, initial: any) -> any`
Reduces the list from the left using the given function and initial value.

#### Example:

```python
foldl(lambda acc, el: el + acc, [1, 2, 3, 4], 5)  # Output: 15
```

### `foldr(function: callable, lst: list, initial: any) -> any`
Reduces the list from the right using the given function and initial value.

#### Example:

```python
foldr(lambda acc, el: el / acc, [1, 2, 3, 4], 24)  # Output: 9
```

### `reverse(lst: list) -> list`
Returns a list with all items in reversed order.

#### Example:

```python
reverse([1, 3, 5, 7])  # Output: [7, 5, 3, 1]
```
