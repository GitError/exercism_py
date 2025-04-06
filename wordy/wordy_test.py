import unittest
from wordy import answer


class WordyTest(unittest.TestCase):
    def test_single_number(self):
        self.assertEqual(answer("What is 5?"), 5)

    def test_addition(self):
        self.assertEqual(answer("What is 1 plus 1?"), 2)

    def test_subtraction(self):
        self.assertEqual(answer("What is 4 minus -12?"), 16)

    def test_multiplication(self):
        self.assertEqual(answer("What is -3 multiplied by 25?"), -75)

    def test_division(self):
        self.assertEqual(answer("What is 33 divided by -3?"), -11)

    def test_multiple_operations(self):
        self.assertEqual(answer("What is 1 plus 1 plus 1?"), 3)
        self.assertEqual(answer("What is 1 plus 5 minus -2?"), 8)
        self.assertEqual(answer("What is 20 minus 4 minus 13?"), 3)
        self.assertEqual(answer("What is 17 minus 6 plus 3?"), 14)
        self.assertEqual(answer("What is 2 multiplied by -2 multiplied by 3?"), -12)
        self.assertEqual(answer("What is -3 plus 7 multiplied by -2?"), -8)
        self.assertEqual(answer("What is -12 divided by 2 divided by -3?"), 2)

    def test_unknown_operation(self):
        with self.assertRaises(ValueError) as err:
            answer("What is 52 cubed?")
        self.assertEqual(str(err.exception), "unknown operation")

    def test_invalid_syntax(self):
        with self.assertRaises(ValueError) as err:
            answer("What is 1 plus?")
        self.assertEqual(str(err.exception), "syntax error")

        with self.assertRaises(ValueError) as err:
            answer("What is?")
        self.assertEqual(str(err.exception), "syntax error")

        with self.assertRaises(ValueError) as err:
            answer("What is 1 plus plus 2?")
        self.assertEqual(str(err.exception), "syntax error")

        with self.assertRaises(ValueError) as err:
            answer("What is 1 plus 2 1?")
        self.assertEqual(str(err.exception), "syntax error")

        with self.assertRaises(ValueError) as err:
            answer("What is 1 2 plus?")
        self.assertEqual(str(err.exception), "syntax error")

        with self.assertRaises(ValueError) as err:
            answer("What is plus 1 2?")
        self.assertEqual(str(err.exception), "syntax error")

        with self.assertRaises(ValueError) as err:
            answer("What is 7 plus multiplied by -2?")
        self.assertEqual(str(err.exception), "syntax error")

    def test_large_numbers(self):
        self.assertEqual(answer("What is 123 plus 45678?"), 45801)

    def test_addition_with_negative_numbers(self):
        self.assertEqual(answer("What is -1 plus -10?"), -11)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as err:
            answer("What is 10 divided by 0?")
        self.assertEqual(str(err.exception), "syntax error")


if __name__ == "__main__":
    unittest.main()