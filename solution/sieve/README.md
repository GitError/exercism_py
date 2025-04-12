# Sieve of Eratosthenes

## Description
This implementation provides a solution to find all prime numbers up to a given limit using the Sieve of Eratosthenes algorithm. The Sieve of Eratosthenes is an ancient and efficient algorithm for finding all prime numbers up to any given limit.

## Algorithm Description

The Sieve of Eratosthenes works by iteratively marking as composite (not prime) the multiples of each prime, starting from 2. The algorithm efficiently finds all the prime numbers up to a specified integer.

### Steps:
1. Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
2. Initially, let p = 2, the smallest prime number.
3. Mark all multiples of p that are greater than or equal to p² as composite.
4. Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p equal this new number (which is the next prime), and repeat from step 3.

## Implementation Details

- Time Complexity: O(n log log n)
- Space Complexity: O(n)
- The implementation handles edge cases like inputs less than 2.

## Usage

```python
from sieve import primes

# Find all primes up to 100
prime_list = primes(100)
print(prime_list)
```

## Running Tests

```bash
python -m unittest sieve_test.py
```

## Example Output

For `primes(10)`, the output is:
```
[2, 3, 5, 7]
```

For `primes(30)`, the output is:
```
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```
