# Nth Prime

## Instructions

Given a number n, determine what the nth prime is.

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

If your language provides methods in the standard library to deal with prime numbers, pretend they don't exist and implement them yourself.

## Definition of a Prime Number

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. By this definition, the first few prime numbers are:

```
2, 3, 5, 7, 11, 13, 17, 19, 23, ...
```

## Example

```python
from nth_prime import prime

# 1st prime
prime(1)  # Returns: 2

# 6th prime 
prime(6)  # Returns: 13

# 10,001st prime
prime(10001)  # Returns: 104743
```

## Exception Handling

The function should handle error cases properly:

- If n < 1, raise a ValueError with the message "there is no zeroth prime"

## Solution Approach

The implementation uses two key functions:

1. `is_prime(n)`: Determines whether a number is prime by:
   - Handling base cases (1 is not prime, 2 is prime)
   - Checking divisibility only by odd numbers up to the square root of n
   - Optimizing by skipping even numbers

2. `prime(number)`: Finds the nth prime by:
   - Validating input (n ≥ 1)
   - Iteratively checking consecutive numbers until the nth prime is found

## Running the tests

To run the tests, navigate to the directory and run:

```bash
pytest nth_prime_test.py
```

## Source

A variation on Problem 7 at Project Euler [http://projecteuler.net/problem=7](http://projecteuler.net/problem=7)
