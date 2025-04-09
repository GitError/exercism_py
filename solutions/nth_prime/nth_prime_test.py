import unittest
import pytest

from nth_prime import prime


class NthPrimeTest(unittest.TestCase):
    def test_first_prime(self):
        self.assertEqual(prime(1), 2)

    def test_second_prime(self):
        self.assertEqual(prime(2), 3)

    def test_sixth_prime(self):
        self.assertEqual(prime(6), 13)

    def test_big_prime(self):
        self.assertEqual(prime(10001), 104743)

    def test_there_is_no_zeroth_prime(self):
        with self.assertRaisesRegex(ValueError, "there is no zeroth prime"):
            prime(0)

    def test_there_is_no_negative_prime(self):
        with self.assertRaisesRegex(ValueError, "there is no zeroth prime"):
            prime(-1)


if __name__ == "__main__":
    unittest.main()
