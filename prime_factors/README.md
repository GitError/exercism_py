# Prime Factors

## Instructions

Compute the prime factors of a given natural number.

A **prime number** is only evenly divisible by itself and 1.

Note that 1 is not a prime number.

## Example

What are the prime factors of 60?

- Our first divisor is 2. 2 goes into 60, leaving 30.
- 2 goes into 30, leaving 15.
- 2 doesn't go cleanly into 15. So let's move on to our next divisor, 3.
- 3 goes cleanly into 15, leaving 5.
- 3 does not go cleanly into 5. The next possible factor is 4.
- 4 does not go cleanly into 5. The next possible factor is 5.
- 5 does go cleanly into 5.
- We're left only with 1, so now, we're done.

Our successful divisors in that computation represent the list of prime factors of 60: 2, 2, 3, and 5.

You can check this yourself:

```
2 * 2 * 3 * 5
= 4 * 15
= 60
```

## Algorithm

The most straightforward approach to finding prime factors:

1. Start with the smallest prime number (2).
2. Divide the number by this prime as many times as possible.
3. Move to the next prime number and repeat.
4. Continue until the number becomes 1 or until the square of the current divisor exceeds the number.

## Optimizations

The implementation includes an optimization: if the square of the current divisor is greater than the remaining value (and the value is > 1), then the value itself is prime. This allows us to directly add it to our result without testing further divisors.

## Running the tests

To run the tests, execute:

```bash
pytest prime_factors_test.py
```

## Source

The Prime Factors Kata by Uncle Bob [http://butunclebob.com/ArticleS.UncleBob.ThePrimeFactorsKata](http://butunclebob.com/ArticleS.UncleBob.ThePrimeFactorsKata)
