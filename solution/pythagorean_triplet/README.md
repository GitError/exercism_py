# Pythagorean Triplet

## Problem Description

A Pythagorean triplet is a set of three natural numbers, {a, b, c}, for which:
- a < b < c
- a² + b² = c²

For example, 3² + 4² = 9 + 16 = 25 = 5².

Given a number N, find all Pythagorean triplets for which a + b + c = N.

For example, with N = 1000, there is exactly one Pythagorean triplet for which a + b + c = 1000: {200, 375, 425}.

## Mathematical Approach

The solution uses a mathematical derivation to optimize the search for triplets:

1. We have two constraints:
   - a + b + c = N (where N is our target sum)
   - a² + b² = c² (the Pythagorean theorem)

2. From the first equation: c = N - a - b
   Substituting into the second equation:
   a² + b² = (N - a - b)²
   
3. Expanding:
   a² + b² = N² - 2N(a + b) + (a + b)²
   a² + b² = N² - 2Na - 2Nb + a² + 2ab + b²
   
4. Simplifying:
   0 = N² - 2Na - 2Nb + 2ab
   2Nb - 2ab = N² - 2Na
   2b(N - a) = N² - 2Na
   
5. Solving for b:
   b = (N² - 2Na) / (2(N - a))

6. The upper bound for 'a' is derived as a < N/(2 + √2), which significantly improves performance.

## Implementation

The function `triplets_with_sum(number)` takes a target sum and returns a list of Pythagorean triplets [a, b, c] that satisfy the given conditions.

## Usage

```python
from pythagorean_triplet import triplets_with_sum

# Find Pythagorean triplets where a + b + c = 1000
triplets = triplets_with_sum(1000)
print(triplets)  # Output: [[200, 375, 425]]
```

## Running Tests

To test the implementation, run the included test file:

```bash
python -m unittest pythagorean_triplet_test.py
```

## Time Complexity

The optimized solution has a time complexity of O(N), where N is the target sum. This is achieved by:
1. Using a tighter bound for the range of values 'a' can take
2. Directly calculating 'b' for each 'a' using the derived formula
3. Verifying potential triplets efficiently

The space complexity is O(T), where T is the number of triplets found.
