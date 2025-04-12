import unittest
from saddle_points import saddle_points

class SaddlePointsTest(unittest.TestCase):
    def sorted_points(self, point_list):
        """Helper method to sort points for comparison"""
        return sorted(point_list, key=lambda p: (p["row"], p["column"]))
        
    def test_can_identify_single_saddle_point(self):
        matrix = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
        self.assertEqual(
            self.sorted_points(saddle_points(matrix)),
            self.sorted_points([{"row": 2, "column": 1}]),
        )
    
    def test_can_identify_that_empty_matrix_has_no_saddle_points(self):
        matrix = []
        self.assertEqual(self.sorted_points(saddle_points(matrix)), [])
    
    def test_can_identify_lack_of_saddle_points_when_there_are_none(self):
        matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]
        self.assertEqual(self.sorted_points(saddle_points(matrix)), [])
    
    def test_can_identify_multiple_saddle_points_in_a_column(self):
        matrix = [[4, 5, 4], [3, 5, 5], [1, 5, 4]]
        self.assertEqual(
            self.sorted_points(saddle_points(matrix)),
            self.sorted_points([
                {"row": 1, "column": 2},
                {"row": 2, "column": 2},
                {"row": 3, "column": 2},
            ]),
        )
    
    def test_can_identify_multiple_saddle_points_in_a_row(self):
        matrix = [[6, 7, 8], [5, 5, 5], [7, 5, 6]]
        self.assertEqual(
            self.sorted_points(saddle_points(matrix)),
            self.sorted_points([
                {"row": 2, "column": 1},
                {"row": 2, "column": 2},
                {"row": 2, "column": 3},
            ]),
        )
    
    def test_can_identify_saddle_point_in_bottom_right_corner(self):
        matrix = [[8, 7, 9], [6, 7, 6], [3, 2, 5]]
        self.assertEqual(
            self.sorted_points(saddle_points(matrix)),
            self.sorted_points([{"row": 3, "column": 3}]),
        )
    
    def test_can_identify_saddle_points_in_a_non_square_matrix(self):
        matrix = [[3, 1, 3], [3, 2, 4]]
        self.assertEqual(
            self.sorted_points(saddle_points(matrix)),
            self.sorted_points([{"row": 1, "column": 3}, {"row": 1, "column": 1}]),
        )
    
    def test_can_identify_saddle_points_in_a_single_column_matrix(self):
        matrix = [[2], [1], [4], [1]]
        self.assertEqual(
            self.sorted_points(saddle_points(matrix)),
            self.sorted_points([{"row": 2, "column": 1}, {"row": 4, "column": 1}]),
        )
    
    def test_can_identify_saddle_points_in_a_single_row_matrix(self):
        matrix = [[2, 5, 3, 5]]
        self.assertEqual(
            self.sorted_points(saddle_points(matrix)),
            self.sorted_points([{"row": 1, "column": 2}, {"row": 1, "column": 4}]),
        )
    
    def test_irregular_matrix(self):
        matrix = [[3, 2, 1], [0, 1], [2, 1, 0]]
        with self.assertRaises(ValueError) as err:
            saddle_points(matrix)
        self.assertEqual(type(err.exception), ValueError)
        self.assertEqual(err.exception.args[0], "irregular matrix")
    
    def test_edge_case_all_same_value(self):
        matrix = [[5, 5], [5, 5]]
        self.assertEqual(
            self.sorted_points(saddle_points(matrix)),
            self.sorted_points([
                {"row": 1, "column": 1}, {"row": 1, "column": 2},
                {"row": 2, "column": 1}, {"row": 2, "column": 2}
            ]),
        )
    
    def test_performance_large_matrix(self):
        # A large matrix to test performance
        import time
        large_matrix = [[i + j for j in range(100)] for i in range(100)]
        start_time = time.time()
        result = saddle_points(large_matrix)
        end_time = time.time()
        # This should complete in a reasonable time
        self.assertLess(end_time - start_time, 1.0)  # Should execute in less than 1 second

if __name__ == '__main__':
    unittest.main()
