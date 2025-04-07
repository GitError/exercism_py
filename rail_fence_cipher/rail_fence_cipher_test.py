import unittest
from rail_fence_cipher import encode, decode


class RailFenceCipherTest(unittest.TestCase):
    def test_encode_with_two_rails(self):
        self.assertEqual(encode("XOXOXOXOXOXOXOXOXO", 2), "XXXXXXXXXOOOOOOOOO")

    def test_encode_with_three_rails(self):
        self.assertEqual(
            encode("WEAREDISCOVEREDFLEEATONCE", 3), 
            "WECRLTEERDSOEEFEAOCAIVDEN"
        )

    def test_encode_with_ending_up(self):
        self.assertEqual(encode("HELLO", 3), "HOELL")

    def test_encode_with_ending_down(self):
        self.assertEqual(encode("HELLO", 2), "HLOEL")

    def test_encode_with_empty_string(self):
        self.assertEqual(encode("", 4), "")

    def test_encode_with_more_rails_than_letters(self):
        self.assertEqual(encode("ABC", 4), "ABC")
    
    def test_encode_with_spaces(self):
        self.assertEqual(
            encode("WE ARE DISCOVERED FLEE AT ONCE", 3), 
            "WECRLTEERDSOEEFEAOCAIVDEN"
        )

    def test_decode_with_three_rails(self):
        self.assertEqual(
            decode("WECRLTEERDSOEEFEAOCAIVDEN", 3),
            "WEAREDISCOVEREDFLEEATONCE"
        )

    def test_decode_with_two_rails(self):
        self.assertEqual(decode("XXXXXXXXXOOOOOOOOO", 2), "XOXOXOXOXOXOXOXOXO")

    def test_decode_with_empty_string(self):
        self.assertEqual(decode("", 3), "")

    def test_decode_with_more_rails_than_letters(self):
        self.assertEqual(decode("ABC", 4), "ABC")
    
    def test_encode_and_decode_are_inverses(self):
        message = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
        rails = 4
        encoded = encode(message, rails)
        self.assertEqual(decode(encoded, rails).replace(" ", ""), message.replace(" ", ""))


if __name__ == "__main__":
    unittest.main()
