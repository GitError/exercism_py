import unittest
from say import say


class SayTest(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(say(0), "zero")

    def test_one(self):
        self.assertEqual(say(1), "one")

    def test_fourteen(self):
        self.assertEqual(say(14), "fourteen")

    def test_twenty(self):
        self.assertEqual(say(20), "twenty")

    def test_twenty_two(self):
        self.assertEqual(say(22), "twenty-two")

    def test_fifty(self):
        self.assertEqual(say(50), "fifty")

    def test_ninety_eight(self):
        self.assertEqual(say(98), "ninety-eight")

    def test_one_hundred(self):
        self.assertEqual(say(100), "one hundred")

    def test_one_hundred_twenty_three(self):
        self.assertEqual(say(123), "one hundred twenty-three")

    def test_one_thousand(self):
        self.assertEqual(say(1000), "one thousand")

    def test_one_thousand_two(self):
        self.assertEqual(say(1002), "one thousand two")

    def test_one_thousand_two_hundred_thirty_four(self):
        self.assertEqual(say(1234), "one thousand two hundred thirty-four")

    def test_one_million(self):
        self.assertEqual(say(1000000), "one million")

    def test_one_million_two_thousand_three_hundred_forty_five(self):
        self.assertEqual(
            say(1002345), "one million two thousand three hundred forty-five"
        )

    def test_one_billion(self):
        self.assertEqual(say(1000000000), "one billion")

    def test_a_large_number(self):
        self.assertEqual(
            say(987654321123),
            "nine hundred eighty-seven billion six hundred fifty-four million three hundred twenty-one thousand one hundred twenty-three",
        )

    def test_raises_error_for_negative_numbers(self):
        with self.assertRaisesRegex(ValueError, "input out of range"):
            say(-1)

    def test_raises_error_for_numbers_above_limit(self):
        with self.assertRaisesRegex(ValueError, "input out of range"):
            say(1000000000000)


if __name__ == "__main__":
    unittest.main()
