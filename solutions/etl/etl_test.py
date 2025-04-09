import unittest
from etl import transform


class EtlTest(unittest.TestCase):
    def test_single_letter(self):
        legacy_data = {1: ["A"]}
        expected = {"a": 1}
        self.assertEqual(transform(legacy_data), expected)

    def test_multiple_letters_same_score(self):
        legacy_data = {1: ["A", "E", "I"]}
        expected = {"a": 1, "e": 1, "i": 1}
        self.assertEqual(transform(legacy_data), expected)

    def test_multiple_scores(self):
        legacy_data = {1: ["A", "E"], 2: ["D", "G"]}
        expected = {"a": 1, "e": 1, "d": 2, "g": 2}
        self.assertEqual(transform(legacy_data), expected)

    def test_full_dataset(self):
        legacy_data = {
            1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
            2: ["D", "G"],
            3: ["B", "C", "M", "P"],
            4: ["F", "H", "V", "W", "Y"],
            5: ["K"],
            8: ["J", "X"],
            10: ["Q", "Z"],
        }
        expected = {
            "a": 1, "e": 1, "i": 1, "o": 1, "u": 1, "l": 1, "n": 1, "r": 1, "s": 1, "t": 1,
            "d": 2, "g": 2,
            "b": 3, "c": 3, "m": 3, "p": 3,
            "f": 4, "h": 4, "v": 4, "w": 4, "y": 4,
            "k": 5,
            "j": 8, "x": 8,
            "q": 10, "z": 10,
        }
        self.assertEqual(transform(legacy_data), expected)


if __name__ == "__main__":
    unittest.main()
