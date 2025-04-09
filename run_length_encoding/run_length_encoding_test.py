import unittest
from run_length_encoding import encode, decode


class RunLengthEncodingTest(unittest.TestCase):
    def test_encode_empty_string(self):
        self.assertEqual(encode(""), "")

    def test_encode_single_characters_only(self):
        self.assertEqual(encode("XYZ"), "XYZ")

    def test_encode_with_no_single_characters(self):
        self.assertEqual(encode("AABBBCCCC"), "2A3B4C")

    def test_encode_with_mixed_characters(self):
        self.assertEqual(encode("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"), 
                                "12WB12W3B24WB")

    def test_encode_multiple_spaces(self):
        self.assertEqual(encode("  hsqq qww  "), "2 hsqq qww2 ")

    def test_encode_lowercase(self):
        self.assertEqual(encode("aabbbcccc"), "2a3b4c")

    def test_decode_empty_string(self):
        self.assertEqual(decode(""), "")

    def test_decode_single_characters_only(self):
        self.assertEqual(decode("XYZ"), "XYZ")

    def test_decode_string_with_numbers(self):
        self.assertEqual(decode("2A3B4C"), "AABBBCCCC")

    def test_decode_string_with_mixed_characters(self):
        self.assertEqual(decode("12WB12W3B24WB"), 
                              "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB")

    def test_decode_multiple_spaces(self):
        self.assertEqual(decode("2 hsqq qww2 "), "  hsqq qww  ")

    def test_decode_lowercase(self):
        self.assertEqual(decode("2a3b4c"), "aabbbcccc")

    def test_encode_then_decode(self):
        original = "zzz ZZ  zZ"
        self.assertEqual(decode(encode(original)), original)


if __name__ == '__main__':
    unittest.main()
