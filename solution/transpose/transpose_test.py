import unittest
from transpose import transpose

class TransposeTest(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(transpose(""), "")
        
    def test_single_line(self):
        self.assertEqual(transpose("Single line."), "Single line.")
        
    def test_two_lines(self):
        input_text = "Hello\nWorld!"
        expected = "HW\neo\nl \nl\no!\nd"
        self.assertEqual(transpose(input_text), expected)
        
    def test_mixed_line_length(self):
        input_text = "The fourth line.\nThe fifth line."
        expected = "TT\nhh\nee\n  \nff\noi\nuf\nrt\nth\nh \n l\nli\nin\nne\ne.\n."
        self.assertEqual(transpose(input_text), expected)
        
    def test_square(self):
        input_text = "HEART\nEMBER\nABUSE\nRESIN\nTREND"
        expected = "HEART\nEMBER\nABUSE\nRESIN\nTREND"
        self.assertEqual(transpose(input_text), expected)
        
    def test_triangle(self):
        input_text = "T\nEE\nAAA\nSSSS\nEEEEE\nRRRRRR"
        expected = "TEASER\nEASER\nASER\nSER\nER\nR"
        self.assertEqual(transpose(input_text), expected)
        
    def test_jagged_triangle(self):
        input_text = "11\n2\n3333\n444\n555555\n66666"
        expected = "123456\n1 3456\n  3456\n   456\n    56\n     6"
        self.assertEqual(transpose(input_text), expected)
        
    def test_many_lines(self):
        input_text = "The longest line.\nA longer line.\nLong line.\nLonger line.\nVery long line.\nA very long line.\nA more than very long line."
        expected = "TAL\nhAo\neLn\n og\nln e\noer\nnn r\nggl\nei \ngs \nti \ntl \n l\ni \nn\ne\n."
        self.assertEqual(transpose(input_text), expected)
        
if __name__ == "__main__":
    unittest.main()
