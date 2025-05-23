import unittest
from prime_factors import factors


class PrimeFactorsTest(unittest.TestCase):
    def test_no_factors(self):
        self.assertEqual(factors(1), [])

    def test_prime_number(self):
        self.assertEqual(factors(2), [2])

    def test_square_of_a_prime(self):
        self.assertEqual(factors(9), [3, 3])

    def test_cube_of_a_prime(self):
        self.assertEqual(factors(8), [2, 2, 2])

    def test_product_of_primes_and_non_primes(self):
        self.assertEqual(factors(12), [2, 2, 3])

    def test_product_of_primes(self):
        self.assertEqual(factors(901255), [5, 17, 23, 461])

    def test_factors_include_a_large_prime(self):
        self.assertEqual(factors(93819012551), [11, 9539, 894119])

    def test_fibonacci_number(self):
        # 8th Fibonacci number is 21
        self.assertEqual(factors(21), [3, 7])

    def test_composite_number(self):
        self.assertEqual(factors(60), [2, 2, 3, 5])


if __name__ == "__main__":
    unittest.main()
