# Binary Search

This module provides a function to find the index of a value in a sorted list using the binary search algorithm.

## 📜 Background

Binary search is an efficient algorithm for finding a target value in a sorted array. Instead of checking each element sequentially, it repeatedly divides the search space in half, significantly reducing the number of operations required.

### How It Works

1. Compare the target value to the middle element of the array
2. If they are equal, return the middle index
3. If the target is smaller, search the left half
4. If the target is larger, search the right half
5. Repeat until the value is found or the search space is empty

### Time Complexity

- **Best case**: O(1) - value is found at the middle on the first attempt
- **Average case**: O(log n) - where n is the number of elements in the list
- **Worst case**: O(log n) - much more efficient than linear search's O(n)

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

### Example 3: Visual Representation
For the search list `[4, 8, 12, 16, 23, 28, 32]` and value `16`:

```
Step 1: Check middle element (16)
[4, 8, 12, 16, 23, 28, 32]
             ^
Value matches! Return index 3.
```

For the search list `[1, 3, 5, 8, 13, 21, 34, 55, 89]` and value `21`:

```
Step 1: Check middle element (8)
[1, 3, 5, 8, 13, 21, 34, 55, 89]
         ^
8 < 21, so search right half.

Step 2: Check middle element (34)
[13, 21, 34, 55, 89]
          ^
34 > 21, so search left half.

Step 3: Check middle element (21)
[13, 21]
     ^
Value matches! Return index 5 (in original array).
```

## 🧪 Testing

Run the included tests with pytest:

```bash
pytest binary_search_test.py
```

## 💡 Implementation Notes

The implementation uses an iterative approach with two pointers (left and right) that track the current search range. The algorithm continues until either:

1. The value is found (success)
2. The left pointer exceeds the right pointer (failure)

This approach avoids the overhead of recursive function calls while maintaining the O(log n) time complexity.

## 🔍 When to Use Binary Search

Binary search is ideal when:
- The data is sorted
- Random access is efficient (like in arrays/lists)
- The collection is relatively static (not frequently modified)
- The search operation is performed many times

For small datasets or unsorted data, other search algorithms might be more appropriate.