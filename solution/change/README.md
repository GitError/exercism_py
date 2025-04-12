# Change Making Problem

## Description

This project implements a solution to the classic change-making problem: determining the minimum number of coins needed to make change for a given amount.

Given a set of coin denominations and a target amount, the goal is to find the fewest number of coins that sum up to the target amount. If it's impossible to make the exact change with the available denominations, the solution will raise an appropriate error.

## Problem Statement

The problem can be formalized as follows:
- Given a set of coin denominations `[c₁, c₂, ..., cₙ]` and a target amount `t`
- Find the minimum number of coins needed to make `t` exactly
- Return the specific coins used to make the change

## Solution Approach

This implementation uses a dynamic programming approach:

1. Handle edge cases:
   - If target is negative, raise a ValueError
   - If target is 0, return an empty list
   - If target is positive but smaller than the smallest coin, raise a ValueError

2. Create a dynamic programming table where:
   - `dp[i]` = minimum number of coins needed to make change for amount `i`
   - `coin_used[i]` = the last coin used in the optimal solution for amount `i`

3. Fill the table bottom-up:
   - For each amount from 1 to target
   - For each available coin
   - Update if using this coin gives a better solution

4. Reconstruct the solution by tracking which coins were used

## Algorithm Visualization

For a concrete example, let's visualize how the algorithm works with coins `[1, 5, 10]` and target `12`:

```
Step 1: Initialize dp array [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
        (dp[0] = 0 as the base case)

Step 2: Fill dp array:
  For amount 1: 
    - Use coin 1: dp[1] = dp[0] + 1 = 1, coin_used[1] = 1
  For amount 2:
    - Use coin 1: dp[2] = dp[1] + 1 = 2, coin_used[2] = 1
  ...
  For amount 5:
    - Use coin 1: dp[5] = dp[4] + 1 = 5
    - Use coin 5: dp[5] = dp[0] + 1 = 1, coin_used[5] = 5 (better!)
  ...
  For amount 12:
    - Use coin 1: dp[12] = dp[11] + 1 = 4
    - Use coin 5: dp[12] = dp[7] + 1 = 3, coin_used[12] = 5
    - Use coin 10: dp[12] = dp[2] + 1 = 3, coin_used[12] = 10

Step 3: Reconstruct solution:
  amount = 12, coin_used[12] = 10, result = [10]
  amount = 2, coin_used[2] = 1, result = [10, 1]
  amount = 1, coin_used[1] = 1, result = [10, 1, 1]
  amount = 0, done!

Final result (sorted): [1, 1, 10]
```

## Usage Examples

```python
from change import find_fewest_coins

# Find minimum coins to make 15 cents
result = find_fewest_coins([1, 5, 10, 25], 15)
print(result)  # Output: [5, 10]

# Find minimum coins to make 40 cents
result = find_fewest_coins([1, 5, 10, 25, 100], 40)
print(result)  # Output: [5, 10, 25]

# Find minimum coins for unusual denominations
result = find_fewest_coins([1, 4, 15, 20, 50], 23)
print(result)  # Output: [4, 4, 15]

# Find minimum coins for large amount
result = find_fewest_coins([1, 5, 10, 25], 99)
print(result)  # Output: [4, 25, 25, 25, 20]

# Error case: Can't make 3 cents with [5, 10]
try:
    find_fewest_coins([5, 10], 3)
except ValueError as e:
    print(str(e))  # Output: "can't make target with given coins"
```

## Performance Considerations

### Time and Space Complexity

- **Time Complexity**: O(n × t) where n is the number of coin denominations and t is the target amount
- **Space Complexity**: O(t) for the dynamic programming table and tracking which coins were used

### Optimizations Used

1. **Sorting the coins**: While not necessary for correctness, sorting can improve performance in some cases by allowing us to consider larger coins first
2. **Early termination** for edge cases like negative targets, zero targets, etc.
3. **Direct reconstruction** of the solution rather than recalculating 

### Performance Limitations

For very large target amounts or a large number of coin denominations, the algorithm might become slow. In those cases, alternative approaches like greedy algorithms (for canonical coin systems) might be worth considering.

## Running Tests

To run the tests:

```bash
python -m unittest change_test.py
```

Or to run a specific test:

```bash
python -m unittest change_test.ChangeTest.test_large_target_values
```

## Edge Cases Handled

- **Negative target amounts**: Raises ValueError with message "target can't be negative"
- **Zero target amount**: Returns an empty list
- **Target amounts smaller than any available coin**: Raises ValueError
- **Cases where change cannot be made with the available coins**: Raises ValueError
- **Non-standard coin denominations**: Works correctly with any set of positive integer denominations

## Related Problems

- Coin Change 2 (number of ways to make change)
- Knapsack Problem
- Minimum Number of Coins to Make Change (without returning the actual coins)

## References

- Introduction to Algorithms (CLRS)
- Dynamic Programming: A Computational Tool by Art Lew and Holger Mauch
