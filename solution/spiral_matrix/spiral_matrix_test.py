import unittest
from spiral_matrix import spiral_matrix


class SpiralMatrixTest(unittest.TestCase):
    def test_empty_spiral(self):
        self.assertEqual(spiral_matrix(0), [])

    def test_size_1_spiral(self):
        self.assertEqual(spiral_matrix(1), [[1]])
        
    def test_size_2_spiral(self):
        expected = [[1, 2], [4, 3]]
        self.assertEqual(spiral_matrix(2), expected)

    def test_size_3_spiral(self):
        expected = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        self.assertEqual(spiral_matrix(3), expected)
        
    def test_size_4_spiral(self):
        expected = [
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7]
        ]
        self.assertEqual(spiral_matrix(4), expected)

    def test_size_5_spiral(self):
        expected = [
            [1, 2, 3, 4, 5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9]
        ]
        self.assertEqual(spiral_matrix(5), expected)


if __name__ == "__main__":
    unittest.main()
