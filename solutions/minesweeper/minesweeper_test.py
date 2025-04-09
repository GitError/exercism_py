import unittest
from minesweeper import annotate


class MinesweeperTest(unittest.TestCase):
    def test_empty_board(self):
        self.assertEqual(annotate([]), [])

    def test_board_with_no_mines(self):
        minefield = [
            "     ",
            "     ",
            "     "
        ]
        expected = [
            "     ",
            "     ",
            "     "
        ]
        self.assertEqual(annotate(minefield), expected)

    def test_board_with_only_mines(self):
        minefield = [
            "***",
            "***",
            "***"
        ]
        expected = [
            "***",
            "***",
            "***"
        ]
        self.assertEqual(annotate(minefield), expected)

    def test_board_with_mines_and_empty_spaces(self):
        minefield = [
            " * * ",
            "  *  ",
            "  *  ",
            "     "
        ]
        expected = [
            "1*3*1",
            "13*31",
            " 2*2 ",
            " 111 "
        ]
        self.assertEqual(annotate(minefield), expected)

    def test_invalid_board_with_inconsistent_row_lengths(self):
        with self.assertRaises(ValueError) as err:
            annotate(["* ", " **"])
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "The board is invalid with current input.")

    def test_invalid_board_with_invalid_characters(self):
        with self.assertRaises(ValueError) as err:
            annotate(["X  * "])
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "The board is invalid with current input.")

    def test_small_board(self):
        minefield = [
            "*"
        ]
        expected = [
            "*"
        ]
        self.assertEqual(annotate(minefield), expected)

    def test_single_row_board(self):
        minefield = [
            " * * "
        ]
        expected = [
            "1*2*1"
        ]
        self.assertEqual(annotate(minefield), expected)

    def test_single_column_board(self):
        minefield = [
            " ",
            "*",
            " ",
            "*",
            " "
        ]
        expected = [
            "1",
            "*",
            "2",
            "*",
            "1"
        ]
        self.assertEqual(annotate(minefield), expected)


if __name__ == "__main__":
    unittest.main()