# Knapsack Problem Solution

## Problem Description

Lhakpa is a Sherpa mountain guide and porter. She is about to leave for an expedition and will be paid the value of the items she carries to the base camp. However, her knapsack has a limited weight capacity.

Given a list of items, each with a specific weight and value, the task is to determine which items to take to maximize the total value while staying within the knapsack's weight limit. Each item can be selected at most once (0/1 knapsack problem).

### Example

```
Items: [
  { "weight": 5, "value": 10 },
  { "weight": 4, "value": 40 },
  { "weight": 6, "value": 30 },
  { "weight": 4, "value": 50 }
]

Knapsack Maximum Weight: 10
```

In this example, Lhakpa should take the second and fourth items (with weights 4 and 4, values 40 and 50) to maximize her value at 90. She cannot get more than 90 as her knapsack has a weight limit of 10.

## Solution Approach

This solution implements a dynamic programming approach to solve the 0/1 knapsack problem:

1. Create a 1D array `dp` of size `maximum_weight + 1`, initialized with zeros.
2. For each item, iterate through the weight array from the maximum weight down to the item's weight.
3. For each possible weight, decide whether including the current item would give a better value than not including it.
4. The final result is in `dp[maximum_weight]`, representing the maximum value possible with the given weight constraint.

The time complexity is O(n * W), where n is the number of items and W is the maximum weight.

## How to Run

Execute the main solution:
```bash
python knapsack.py
```

Run the tests:
```bash
python -m unittest knapsack_test.py
```

## Implementation Details

The dynamic programming approach used here is an efficient solution to the 0/1 knapsack problem. By processing the weights from maximum to minimum for each item, we ensure that each item is considered exactly once.
