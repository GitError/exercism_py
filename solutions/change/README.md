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

## Usage Examples

```python
from change import find_fewest_coins

# Find minimum coins to make 15 cents
result = find_fewest_coins([1, 5, 10, 25], 15)
print(result)  # Output: [5, 10]

# Find minimum coins to make 40 cents
result = find_fewest_coins([1, 5, 10, 25, 100], 40)
print(result)  # Output: [5, 10, 25]

# Error case: Can't make 3 cents with [5, 10]
try:
    find_fewest_coins([5, 10], 3)
except ValueError as e:
    print(str(e))  # Output: "can't make target with given coins"
```

## Running Tests

To run the tests:

```bash
python -m unittest change_test.py
```

## Time and Space Complexity

- Time Complexity: O(n × t) where n is the number of coin denominations and t is the target amount
- Space Complexity: O(t) for the dynamic programming table and tracking which coins were used

## Edge Cases Handled

- Negative target amounts
- Zero target amount
- Target amounts smaller than any available coin
- Cases where change cannot be made with the available coins
