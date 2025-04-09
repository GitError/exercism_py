import unittest
from palindrome_products import largest, smallest


class PalindromeProductsTest(unittest.TestCase):
    def test_find_the_smallest_palindrome_from_single_digit_factors(self):
        value, factors = smallest(min_factor=1, max_factor=9)
        self.assertEqual(value, 1)
        self.assertFactorsEqual(factors, [[1, 1]])

    def test_find_the_largest_palindrome_from_single_digit_factors(self):
        value, factors = largest(min_factor=1, max_factor=9)
        self.assertEqual(value, 9)
        self.assertFactorsEqual(factors, [[1, 9], [3, 3]])

    def test_find_the_smallest_palindrome_from_double_digit_factors(self):
        value, factors = smallest(min_factor=10, max_factor=99)
        self.assertEqual(value, 121)
        self.assertFactorsEqual(factors, [[11, 11]])

    def test_find_the_largest_palindrome_from_double_digit_factors(self):
        value, factors = largest(min_factor=10, max_factor=99)
        self.assertEqual(value, 9009)
        self.assertFactorsEqual(factors, [[91, 99]])

    def test_find_the_smallest_palindrome_from_triple_digit_factors(self):
        value, factors = smallest(min_factor=100, max_factor=999)
        self.assertEqual(value, 10201)
        self.assertFactorsEqual(factors, [[101, 101]])

    def test_find_the_largest_palindrome_from_triple_digit_factors(self):
        value, factors = largest(min_factor=100, max_factor=999)
        self.assertEqual(value, 906609)
        self.assertFactorsEqual(factors, [[913, 993]])

    def test_empty_result_for_smallest_if_no_palindrome_in_the_range(self):
        value, factors = smallest(min_factor=1002, max_factor=1003)
        self.assertIsNone(value)
        self.assertFactorsEqual(factors, [])

    def test_empty_result_for_largest_if_no_palindrome_in_the_range(self):
        value, factors = largest(min_factor=15, max_factor=15)
        self.assertIsNone(value)
        self.assertFactorsEqual(factors, [])

    def test_error_result_for_smallest_if_min_is_more_than_max(self):
        with self.assertRaises(ValueError) as err:
            value, factors = smallest(min_factor=10000, max_factor=1)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "min must be <= max")

    def test_error_result_for_largest_if_min_is_more_than_max(self):
        with self.assertRaises(ValueError) as err:
            value, factors = largest(min_factor=2, max_factor=1)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "min must be <= max")

    def test_multiple_factors_for_largest_palindrome(self):
        value, factors = largest(min_factor=10, max_factor=20)
        self.assertEqual(value, 323)
        self.assertFactorsEqual(factors, [[17, 19]])

    def test_multiple_factors_for_smallest_palindrome(self):
        value, factors = smallest(min_factor=10, max_factor=50)
        self.assertEqual(value, 121)
        self.assertFactorsEqual(factors, [[11, 11]])

    def test_returns_sorted_factor_lists(self):
        value, factors = largest(min_factor=1, max_factor=9)
        for factor_list in factors:
            self.assertTrue(factor_list[0] <= factor_list[1])

    def test_handles_min_factor_zero(self):
        value, factors = smallest(min_factor=0, max_factor=9)
        self.assertEqual(value, 0)
        self.assertFactorsEqual(factors, [[0, 0]])

    def assertFactorsEqual(self, actual, expected):
        """Helper method to compare factors, ignoring order within each pair."""
        self.assertEqual(len(actual), len(expected))
        
        # Convert both lists to a set of frozensets for order-independent comparison
        actual_sets = set(frozenset(pair) for pair in actual)
        expected_sets = set(frozenset(pair) for pair in expected)
        self.assertEqual(actual_sets, expected_sets)


if __name__ == "__main__":
    unittest.main()