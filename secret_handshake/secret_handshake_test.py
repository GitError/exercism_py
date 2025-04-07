import unittest
from secret_handshake import commands

class SecretHandshakeTest(unittest.TestCase):
    def test_wink_for_1(self):
        """Test that input 1 (binary 1) returns just a wink."""
        self.assertEqual(commands("1"), ["wink"])
    
    def test_double_blink_for_10(self):
        """Test that input 2 (binary 10) returns just a double blink."""
        self.assertEqual(commands("10"), ["double blink"])
    
    def test_close_your_eyes_for_100(self):
        """Test that input 4 (binary 100) returns just close your eyes."""
        self.assertEqual(commands("100"), ["close your eyes"])
    
    def test_jump_for_1000(self):
        """Test that input 8 (binary 1000) returns just jump."""
        self.assertEqual(commands("1000"), ["jump"])
    
    def test_combination_without_reverse(self):
        """Test that input 19 (binary 10011) returns wink and jump (no reverse)."""
        self.assertEqual(commands("10011"), ["wink", "jump"])
    
    def test_reverse_for_10000(self):
        """Test that input 16 (binary 10000) returns an empty list (just reverse)."""
        self.assertEqual(commands("10000"), [])
    
    def test_all_actions_in_order(self):
        """Test that input 15 (binary 1111) returns all actions in order."""
        self.assertEqual(
            commands("1111"), 
            ["wink", "double blink", "close your eyes", "jump"]
        )
    
    def test_all_actions_reversed(self):
        """Test that input 31 (binary 11111) returns all actions reversed."""
        self.assertEqual(
            commands("11111"), 
            ["jump", "close your eyes", "double blink", "wink"]
        )
    
    def test_example_from_instructions_1(self):
        """Test the first example from the instructions (binary 1001)."""
        self.assertEqual(commands("1001"), ["wink", "jump"])
    
    def test_example_from_instructions_2(self):
        """Test the second example from the instructions (binary 11010)."""
        self.assertEqual(commands("11010"), ["jump", "double blink"])
    
    def test_example_from_instructions_3(self):
        """Test the third example from the instructions (binary 00011)."""
        self.assertEqual(commands("00011"), ["wink", "double blink"])
    
    def test_do_not_reverse_empty_list(self):
        """Test that an input that would result in an empty list doesn't change when reversed."""
        self.assertEqual(commands("10000"), [])
    
    def test_ignore_extra_bits(self):
        """Test that bits beyond the 5 rightmost are ignored."""
        self.assertEqual(commands("1100001"), ["wink"])
    
    def test_input_0(self):
        """Test that input 0 returns an empty list."""
        self.assertEqual(commands("0"), [])
    
    def test_input_with_leading_zeros(self):
        """Test that leading zeros don't affect the result."""
        self.assertEqual(commands("000010"), ["double blink"])
    
    def test_partial_reverse(self):
        """Test reversing a subset of actions."""
        self.assertEqual(commands("10110"), ["close your eyes", "double blink"])

if __name__ == "__main__":
    unittest.main()