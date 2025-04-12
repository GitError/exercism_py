import unittest
from word_count import count_words


class WordCountTest(unittest.TestCase):
    def test_simple_sentence(self):
        self.assertEqual(
            {"hello": 1, "world": 1},
            count_words("hello world")
        )
        
    def test_case_insensitive(self):
        self.assertEqual(
            {"hello": 2, "world": 1},
            count_words("Hello hello world")
        )
        
    def test_with_punctuation(self):
        self.assertEqual(
            {"hello": 1, "world": 1, "how": 1, "are": 1, "you": 1},
            count_words("Hello, world! How are you?")
        )
        
    def test_with_contractions(self):
        self.assertEqual(
            {"can't": 1, "don't": 1, "it's": 1, "that's": 1},
            count_words("can't don't it's that's")
        )
        
    def test_with_numbers(self):
        self.assertEqual(
            {"testing": 1, "123": 1, "numbers": 1, "456": 1},
            count_words("Testing 123 numbers 456")
        )
        
    def test_apostrophes_examples(self):
        self.assertEqual(
            {"that's": 1, "the": 2, "password": 2, "123": 1,
             "agent": 1, "cried": 1, "so": 1, "i": 1, "fled": 1, "special": 1},
            count_words("That's the password: 'PASSWORD 123'!, cried the Special Agent.\nSo I fled.")
        )
        
    def test_apostrophe_at_word_boundary(self):
        self.assertEqual(
            {"don't": 2, "fence": 1, "me": 1, "in": 1},
            count_words("'Don't' 'fence' 'me' 'in'")
        )


if __name__ == "__main__":
    unittest.main()
