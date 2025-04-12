# Difference of Squares

This exercise calculates the difference between the square of the sum and the sum of the squares of the first N natural numbers.

## Problem Description

The square of the sum of the first ten natural numbers is:
(1 + 2 + ... + 10)² = 55² = 3025

The sum of the squares of the first ten natural numbers is:
1² + 2² + ... + 10² = 385

Hence the difference between the square of the sum and the sum of the squares of the first ten natural numbers is:
3025 - 385 = 2640

## Solution

The solution uses mathematical formulas for efficiency:

1. Sum of first n natural numbers: n(n+1)/2
2. Sum of squares of first n natural numbers: n(n+1)(2n+1)/6

These formulas allow us to calculate the result in constant time (O(1)) rather than using loops.

### Mathematical Derivation

The formula for the sum of the first n natural numbers can be derived as:
- Sum = 1 + 2 + 3 + ... + n
- Sum = n(n+1)/2

The formula for the sum of squares of the first n natural numbers is:
- Sum of Squares = 1² + 2² + 3² + ... + n²
- Sum of Squares = n(n+1)(2n+1)/6

## Functions

- `square_of_sum(number)`: Calculate the square of the sum of the first `number` natural numbers.
- `sum_of_squares(number)`: Calculate the sum of squares of the first `number` natural numbers.
- `difference_of_squares(number)`: Calculate the difference between the square of sum and sum of squares.

## Example Usage

```python
from difference_of_squares import square_of_sum, sum_of_squares, difference_of_squares

# Calculate for the first 10 natural numbers
square_of_sum_10 = square_of_sum(10)  # 3025
sum_of_squares_10 = sum_of_squares(10)  # 385
difference_10 = difference_of_squares(10)  # 2640

print(f"Square of sum: {square_of_sum_10}")
print(f"Sum of squares: {sum_of_squares_10}")
print(f"Difference: {difference_10}")
```

## Complexity Analysis

- **Time Complexity**: O(1) for all functions. The calculations use direct mathematical formulas instead of loops.
- **Space Complexity**: O(1), as only a fixed number of variables are used regardless of input size.

## Running the Tests

To run the tests, execute:

```bash
python difference_of_squares_test.py
```

For more detailed test results:

```bash
python -m unittest difference_of_squares_test.py
```

## Installation

No external dependencies are required. This solution uses only Python's standard library.

To set up the exercise:

1. Make sure you have Python 3.6+ installed
2. Clone this repository
3. Navigate to the `difference_of_squares` directory
4. Run the tests as described above

