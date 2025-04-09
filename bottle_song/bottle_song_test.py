import unittest
from bottle_song import recite


class BottleSongTest(unittest.TestCase):
    def test_first_generic_verse(self):
        expected = [
            "Ten green bottles hanging on the wall,",
            "Ten green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be nine green bottles hanging on the wall.",
        ]
        self.assertEqual(recite(start=10), expected)

    def test_last_generic_verse(self):
        expected = [
            "Three green bottles hanging on the wall,",
            "Three green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be two green bottles hanging on the wall.",
        ]
        self.assertEqual(recite(start=3), expected)

    def test_verse_with_2_bottles(self):
        expected = [
            "Two green bottles hanging on the wall,",
            "Two green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be one green bottle hanging on the wall.",
        ]
        self.assertEqual(recite(start=2), expected)

    def test_verse_with_1_bottle(self):
        expected = [
            "One green bottle hanging on the wall,",
            "One green bottle hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be no green bottles hanging on the wall.",
        ]
        self.assertEqual(recite(start=1), expected)

    def test_first_two_verses(self):
        expected = [
            "Ten green bottles hanging on the wall,",
            "Ten green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be nine green bottles hanging on the wall.",
            "",
            "Nine green bottles hanging on the wall,",
            "Nine green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be eight green bottles hanging on the wall.",
        ]
        self.assertEqual(recite(start=10, take=2), expected)

    def test_last_three_verses(self):
        expected = [
            "Three green bottles hanging on the wall,",
            "Three green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be two green bottles hanging on the wall.",
            "",
            "Two green bottles hanging on the wall,",
            "Two green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be one green bottle hanging on the wall.",
            "",
            "One green bottle hanging on the wall,",
            "One green bottle hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            "There'll be no green bottles hanging on the wall.",
        ]
        self.assertEqual(recite(start=3, take=3), expected)
    
    def test_invalid_start_value(self):
        # Testing with a value outside our defined number_to_word dictionary
        result = recite(start=11)
        self.assertTrue("11" in result[0])  # Should use the string representation
    
    def test_zero_take_value(self):
        # Should return an empty list if take is 0
        self.assertEqual(recite(start=10, take=0), [])
    
    def test_negative_take_value(self):
        # Should handle negative take values gracefully (return empty list)
        self.assertEqual(recite(start=10, take=-2), [])


if __name__ == '__main__':
    unittest.main()
