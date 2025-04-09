import unittest
from acronym import abbreviate

class AbbreviateTest(unittest.TestCase):
    def test_basic_phrase(self):
        self.assertEqual(abbreviate("As Soon As Possible"), "ASAP")

    def test_phrase_with_hyphens(self):
        self.assertEqual(abbreviate("Liquid-crystal display"), "LCD")

    def test_phrase_with_punctuation(self):
        self.assertEqual(abbreviate("Thank George It's Friday!"), "TGIF")

    def test_phrase_with_underscores(self):
        self.assertEqual(abbreviate("The Road _Not_ Taken"), "TRNT")

    def test_single_word(self):
        self.assertEqual(abbreviate("Python"), "P")

    def test_empty_string(self):
        self.assertEqual(abbreviate(""), "")

    def test_punctuation_only(self):
        self.assertEqual(abbreviate("!!!"), "")

    def test_mixed_case(self):
        self.assertEqual(abbreviate("HyperText Markup Language"), "HTML")

    def test_numbers_in_phrase(self):
        self.assertEqual(abbreviate("3D Graphics Processing Unit"), "3DGPU")

    def test_phrase_with_extra_spaces(self):
        self.assertEqual(abbreviate("  National   Aeronautics   and Space   Administration  "), "NASA")

    def test_phrase_with_special_characters(self):
        self.assertEqual(abbreviate("Don't Repeat Yourself!"), "DRY")

if __name__ == "__main__":
    unittest.main()