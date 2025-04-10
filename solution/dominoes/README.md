# Dominoes

This exercise tackles the classic domino chain problem, where you need to determine if a set of dominoes can form a valid chain.

## Description

In Toyland, the trains run on tracks made of domino pieces. Each domino is marked with two numbers. For the train to move, the dominoes must form a perfect chain where the numbers match.

A valid domino chain requires:
1. Adjacent dominoes must have matching numbers where they connect
2. The first and last domino must also match (forming a loop)

For example, given the stones `[2|1]`, `[2|3]` and `[1|3]` you can form valid chains like `[1|2] [2|3] [3|1]` or `[3|2] [2|1] [1|3]`.

But for stones `[1|2]`, `[4|1]` and `[2|3]`, a valid chain is impossible because `4` and `3` don't match.

## Implementation

The solution uses a recursive backtracking approach:

1. Handle edge cases (empty list, single domino)
2. Try each domino as the starting point
3. For each starting domino, try both orientations
4. Use depth-first search to build a chain
5. Verify that the chain forms a loop (last value matches first value)

## Usage

```python
from dominoes import can_chain

# Example usage
dominoes = [[1, 2], [3, 1], [2, 3]]
result = can_chain(dominoes)
# Result will be a valid chain like [[1, 3], [3, 2], [2, 1]]

# If no valid chain exists
dominoes = [[1, 2], [4, 1], [2, 3]]
result = can_chain(dominoes)
# Result will be None
```

## Testing

Run the tests using the Python unittest framework:

```bash
python dominoes_test.py
```

## Edge Cases

- Empty input returns an empty list `[]`
- Single domino with matching values (like `[5, 5]`) returns the domino itself
- Single domino with non-matching values (like `[1, 2]`) returns `None`
- If no valid chain can be formed, the function returns `None`
