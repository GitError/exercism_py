import unittest
from variable_length_quantity import encode, decode


class AdditionalVLQTests(unittest.TestCase):
    """Additional tests to verify variable length quantity encoding/decoding."""

    def test_encode_zero_values(self):
        """Test encoding multiple zero values."""
        self.assertEqual(encode([0, 0, 0]), [0, 0, 0])

    def test_encode_small_consecutive_values(self):
        """Test encoding a sequence of small consecutive values."""
        self.assertEqual(encode([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_encode_mixed_values(self):
        """Test encoding a mix of small and large values."""
        self.assertEqual(
            encode([0, 0x100, 0, 0x7FFFFFFF]),
            [0, 0x81, 0x80, 0, 0xFF, 0xFF, 0xFF, 0xFF, 0x7F]
        )

    def test_decode_empty_list(self):
        """Test that decoding an empty list raises a ValueError."""
        with self.assertRaises(ValueError) as err:
            decode([])
        self.assertEqual(err.exception.args[0], "incomplete sequence")

    def test_decode_multiple_incomplete_sequences(self):
        """Test that multiple incomplete sequences raise a ValueError."""
        with self.assertRaises(ValueError) as err:
            decode([0x81, 0x81, 0x81])
        self.assertEqual(err.exception.args[0], "incomplete sequence")

    def test_encode_decode_roundtrip(self):
        """Test that encoding and then decoding returns the original numbers."""
        original = [0, 1, 127, 128, 255, 256, 16383, 16384, 0x7FFFFFFF]
        encoded = encode(original)
        decoded = decode(encoded)
        self.assertEqual(decoded, original)

    def test_max_32bit_integers(self):
        """Test encoding and decoding the maximum 32-bit unsigned integers."""
        max_integers = [0xFFFFFFFF, 0xFFFFFFFE, 0xFFFFFFFD]
        encoded = encode(max_integers)
        decoded = decode(encoded)
        self.assertEqual(decoded, max_integers)


if __name__ == "__main__":
    unittest.main()
