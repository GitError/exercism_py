# Sum of Multiples

This project implements a solution for calculating the sum of unique multiples of given factors below a specified limit.

## Problem Description

In this fantasy-survival game, players earn energy points when they complete a level. The points are calculated based on the magical items found during the level:

1. For each magical item, find all multiples of its base value that are less than the level number
2. Combine all these multiples into a single set, removing duplicates
3. Calculate the sum of all the remaining numbers

## Example

For a player who completed level 20 and found magical items with base values 3 and 5:

- Multiples of 3 less than 20: {3, 6, 9, 12, 15, 18}
- Multiples of 5 less than 20: {5, 10, 15}
- Combined set (without duplicates): {3, 5, 6, 9, 10, 12, 15, 18}
- Sum: 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 = 78

## Implementation

The implementation is in `sum_of_multiples.py` and provides an efficient solution using set comprehensions.

### Function Signature

```python
def sum_of_multiples(limit, multiples):
    """
    Calculate the sum of all unique multiples of the given factors below a limit.
    
    Args:
        limit (int): The upper bound (exclusive) for finding multiples.
        multiples (list): A list of factors to find multiples for.
        
    Returns:
        int: The sum of all unique multiples of the factors below the limit.
    """
```

### Features

- Efficiently calculates the sum of unique multiples
- Handles edge cases like zeros in the multiples list
- Optimized for performance with set comprehensions

## Testing

Run the tests using:

```
python -m unittest sum_of_multiples_test.py
```

The test suite covers various scenarios including:
- Standard cases with common factors like 3 and 5
- Edge cases with empty lists or zeros
- Cases with multiple factors
- Various limit values from small to large

## Assumptions

- All input numbers are non-negative integers
- The list of factors may contain zeros (which are handled properly)
- The factors are unique and sorted in ascending order (though the implementation works even if they aren't)
