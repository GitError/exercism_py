import unittest
from proverb import proverb

class ProverbTest(unittest.TestCase):
    def test_empty_input(self):
        """Test that an empty input returns an empty list"""
        self.assertEqual(proverb(), [])
    
    def test_single_word(self):
        """Test that a single word returns just the final verse"""
        expected = ["And all for the want of a nail."]
        self.assertEqual(proverb("nail"), expected)
        
    def test_two_words(self):
        """Test proverb with two words"""
        expected = [
            "For want of a nail the shoe was lost.",
            "And all for the want of a nail."
        ]
        self.assertEqual(proverb("nail", "shoe"), expected)
        
    def test_full_proverb(self):
        """Test with a complete proverb sequence"""
        words = ["nail", "shoe", "horse", "rider", "message", "battle", "kingdom"]
        expected = [
            "For want of a nail the shoe was lost.",
            "For want of a shoe the horse was lost.",
            "For want of a horse the rider was lost.",
            "For want of a rider the message was lost.",
            "For want of a message the battle was lost.",
            "For want of a battle the kingdom was lost.",
            "And all for the want of a nail."
        ]
        self.assertEqual(proverb(*words), expected)
        
    def test_with_qualifier(self):
        """Test with a qualifier in the final verse"""
        words = ["nail", "shoe", "horse"]
        expected = [
            "For want of a nail the shoe was lost.",
            "For want of a shoe the horse was lost.",
            "And all for the want of a horseshoe nail."
        ]
        self.assertEqual(proverb(*words, qualifier="horseshoe"), expected)
        
    def test_different_words(self):
        """Test with a non-standard set of words"""
        words = ["pin", "gun", "soldier", "battle"]
        expected = [
            "For want of a pin the gun was lost.",
            "For want of a gun the soldier was lost.",
            "For want of a soldier the battle was lost.",
            "And all for the want of a pin."
        ]
        self.assertEqual(proverb(*words), expected)

if __name__ == "__main__":
    unittest.main()
