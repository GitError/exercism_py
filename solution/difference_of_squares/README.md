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

## Functions

- `square_of_sum(number)`: Calculate the square of the sum of the first `number` natural numbers.
- `sum_of_squares(number)`: Calculate the sum of squares of the first `number` natural numbers.
- `difference_of_squares(number)`: Calculate the difference between the square of sum and sum of squares.

## Running the Tests

To run the tests, execute:

