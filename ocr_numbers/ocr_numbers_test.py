import unittest
import pytest
from ocr_numbers import convert

class OcrNumbersTest(unittest.TestCase):
    def test_recognizes_0(self):
        self.assertEqual(convert([
            " _ ",
            "| |",
            "|_|",
            "   "
        ]), "0")
        
    def test_recognizes_1(self):
        self.assertEqual(convert([
            "   ",
            "  |",
            "  |",
            "   "
        ]), "1")
    
    def test_unreadable_but_correct_size(self):
        self.assertEqual(convert([
            "   ",
            "  _",
            "  |",
            "   "
        ]), "?")
    
    def test_line_number_not_multiple_of_four(self):
        with self.assertRaisesRegex(ValueError, "Number of input lines is not a multiple of four"):
            convert([" _ ", "| |", "|_|"])
    
    def test_columns_not_multiple_of_three(self):
        with self.assertRaisesRegex(ValueError, "Number of input columns is not a multiple of three"):
            convert([
                "    ",
                "   |",
                "   |",
                "    "
            ])
    
    def test_rows_with_different_length(self):
        with self.assertRaisesRegex(ValueError, "Input rows don't have the same length"):
            convert([
                " _ ",
                "| |",
                "|_|  ",
                "   "
            ])
            
    def test_recognizes_string_of_single_digits(self):
        self.assertEqual(convert([
            "    _  _     _  _  _  _  _ ",
            "  | _| _||_||_ |_   ||_||_|",
            "  ||_  _|  | _||_|  ||_| _|",
            "                           "
        ]), "1234567890")
            
    def test_numbers_separated_by_empty_lines(self):
        self.assertEqual(convert([
            "    _  _ ",
            "  | _| _|",
            "  ||_  _|",
            "         ",
            "    _  _ ",
            "|_||_ |_ ",
            "  | _||_|",
            "         ",
            " _  _  _ ",
            "  ||_||_|",
            "  ||_| _|",
            "         "
        ]), "123,456,789")

    def test_full_ocr_text_mixed_case(self):
        self.assertEqual(convert([
            "    _  _  _  _  _  _  _  _ ",
            "  | _| _||_|| ||_ |_   ||_|",
            "  ||_  _|  ||_||_|  | _||_|",
            "                           "
        ]), "12345678?0")


if __name__ == "__main__":
    unittest.main()
