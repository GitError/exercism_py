import unittest
from scrabble_score import score


class ScrabbleScoreTest(unittest.TestCase):
    def test_lowercase_letter(self):
        self.assertEqual(score('a'), 1)
        
    def test_uppercase_letter(self):
        self.assertEqual(score('A'), 1)
        
    def test_valuable_letter(self):
        self.assertEqual(score('f'), 4)
        
    def test_short_word(self):
        self.assertEqual(score('at'), 2)
        
    def test_short_valuable_word(self):
        self.assertEqual(score('zoo'), 12)
        
    def test_medium_word(self):
        self.assertEqual(score('street'), 6)
        
    def test_medium_valuable_word(self):
        self.assertEqual(score('quirky'), 22)
        
    def test_long_mixed_case_word(self):
        self.assertEqual(score('OxyphenButazone'), 41)
        
    def test_english_like_word(self):
        self.assertEqual(score('pinata'), 8)
        
    def test_empty_input(self):
        self.assertEqual(score(''), 0)
        
    def test_none_input(self):
        self.assertEqual(score(None), 0)
        
    def test_symbols_score_zero(self):
        self.assertEqual(score('#$%^'), 0)
        
    def test_word_with_spaces_and_symbols(self):
        self.assertEqual(score('hello world!'), 15)
        
    def test_examples_from_description(self):
        self.assertEqual(score('cabbage'), 14)
        self.assertEqual(score('QUIZ'), 22)


if __name__ == '__main__':
    unittest.main()
