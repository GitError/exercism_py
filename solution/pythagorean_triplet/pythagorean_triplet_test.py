import unittest
from pythagorean_triplet import triplets_with_sum

class PythagoreanTripletTest(unittest.TestCase):
    def test_triplet_with_sum_12(self):
        expected = [[3, 4, 5]]
        self.assertCountEqual(triplets_with_sum(12), expected)
        
    def test_triplet_with_sum_108(self):
        expected = [[27, 36, 45]]
        self.assertCountEqual(triplets_with_sum(108), expected)
        
    def test_triplet_with_sum_1000(self):
        expected = [[200, 375, 425]]
        self.assertCountEqual(triplets_with_sum(1000), expected)
        
    def test_triplet_with_sum_1001(self):
        expected = []
        self.assertCountEqual(triplets_with_sum(1001), expected)
        
    def test_triplet_with_sum_90(self):
        expected = [[9, 40, 41], [15, 36, 39]]
        self.assertCountEqual(triplets_with_sum(90), expected)
        
    def test_triplet_with_sum_840(self):
        expected = [
            [40, 399, 401],
            [56, 390, 394],
            [105, 360, 375],
            [120, 350, 370],
            [140, 336, 364],
            [168, 315, 357],
            [210, 280, 350],
            [240, 252, 348]
        ]
        self.assertCountEqual(triplets_with_sum(840), expected)
        
    def test_no_triplet_exists(self):
        expected = []
        self.assertCountEqual(triplets_with_sum(14), expected)
        
    def test_performance_large_sum(self):
        # This tests the optimization by checking that it can handle larger sums efficiently
        result = triplets_with_sum(30000)
        # Just check that it completes in reasonable time and returns a list
        self.assertIsInstance(result, list)

if __name__ == "__main__":
    unittest.main()
