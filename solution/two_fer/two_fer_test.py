import unittest
from two_fer import two_fer

class TwoFerTest(unittest.TestCase):
    def test_no_name_given(self):
        """Test the output when no name is provided."""
        self.assertEqual(two_fer(), "One for you, one for me.")

    def test_a_name_given(self):
        """Test the output when 'Alice' is provided."""
        self.assertEqual(two_fer("Alice"), "One for Alice, one for me.")
    
    def test_another_name_given(self):
        """Test the output when 'Bob' is provided."""
        self.assertEqual(two_fer("Bob"), "One for Bob, one for me.")
        
    def test_empty_string_name(self):
        """Test the output when an empty string is provided."""
        self.assertEqual(two_fer(""), "One for , one for me.")

if __name__ == '__main__':
    unittest.main()
