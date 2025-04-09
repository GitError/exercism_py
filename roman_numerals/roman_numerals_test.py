import unittest
from roman_numerals import roman

class RomanNumeralsTest(unittest.TestCase):
    def test_single_values(self):
        self.assertEqual(roman(1), "I")
        self.assertEqual(roman(5), "V")
        self.assertEqual(roman(10), "X")
        self.assertEqual(roman(50), "L")
        self.assertEqual(roman(100), "C")
        self.assertEqual(roman(500), "D")
        self.assertEqual(roman(1000), "M")

    def test_special_cases(self):
        self.assertEqual(roman(4), "IV")
        self.assertEqual(roman(9), "IX")
        self.assertEqual(roman(40), "XL")
        self.assertEqual(roman(90), "XC")
        self.assertEqual(roman(400), "CD")
        self.assertEqual(roman(900), "CM")

    def test_general_numbers(self):
        self.assertEqual(roman(3), "III")
        self.assertEqual(roman(14), "XIV")
        self.assertEqual(roman(19), "XIX")
        self.assertEqual(roman(44), "XLIV")
        self.assertEqual(roman(68), "LXVIII")
        self.assertEqual(roman(99), "XCIX")
        self.assertEqual(roman(444), "CDXLIV")
        self.assertEqual(roman(999), "CMXCIX")
        self.assertEqual(roman(1984), "MCMLXXXIV")
        self.assertEqual(roman(2023), "MMXXIII")
        self.assertEqual(roman(3999), "MMMCMXCIX")

    def test_boundary_values(self):
        self.assertEqual(roman(1), "I")
        self.assertEqual(roman(3999), "MMMCMXCIX")
        with self.assertRaises(ValueError):
            roman(0)
        with self.assertRaises(ValueError):
            roman(4000)
        with self.assertRaises(ValueError):
            roman(-1)

if __name__ == '__main__':
    unittest.main()
