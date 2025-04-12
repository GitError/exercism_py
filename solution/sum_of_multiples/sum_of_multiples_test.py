import unittest
from sum_of_multiples import sum_of_multiples

class SumOfMultiplesTest(unittest.TestCase):
    """Test cases for sum_of_multiples function."""
    
    def test_multiples_of_3_or_5_up_to_1(self):
        """Test with multiples of 3 or 5 up to 1."""
        self.assertEqual(sum_of_multiples(1, [3, 5]), 0)
    
    def test_multiples_of_3_or_5_up_to_4(self):
        """Test with multiples of 3 or 5 up to 4."""
        self.assertEqual(sum_of_multiples(4, [3, 5]), 3)
    
    def test_multiples_of_3_or_5_up_to_10(self):
        """Test with multiples of 3 or 5 up to 10."""
        self.assertEqual(sum_of_multiples(10, [3, 5]), 23)
    
    def test_multiples_of_3_or_5_up_to_20(self):
        """Test with multiples of 3 or 5 up to 20."""
        self.assertEqual(sum_of_multiples(20, [3, 5]), 78)
    
    def test_multiples_of_3_or_5_up_to_100(self):
        """Test with multiples of 3 or 5 up to 100."""
        self.assertEqual(sum_of_multiples(100, [3, 5]), 2318)
    
    def test_multiples_of_3_or_5_up_to_1000(self):
        """Test with multiples of 3 or 5 up to 1000."""
        self.assertEqual(sum_of_multiples(1000, [3, 5]), 233168)
    
    def test_multiples_of_7_13_or_17_up_to_20(self):
        """Test with multiples of 7, 13, or 17 up to 20."""
        self.assertEqual(sum_of_multiples(20, [7, 13, 17]), 51)
    
    def test_multiples_of_4_or_6_up_to_15(self):
        """Test with multiples of 4 or 6 up to 15."""
        self.assertEqual(sum_of_multiples(15, [4, 6]), 30)
    
    def test_multiples_of_5_6_or_8_up_to_150(self):
        """Test with multiples of 5, 6, or 8 up to 150."""
        self.assertEqual(sum_of_multiples(150, [5, 6, 8]), 4419)
    
    def test_multiples_of_empty_list_up_to_10(self):
        """Test with an empty list of multiples up to 10."""
        self.assertEqual(sum_of_multiples(10, []), 0)
    
    def test_multiples_with_zero_in_list(self):
        """Test with zero in the list of multiples."""
        self.assertEqual(sum_of_multiples(10, [0, 3, 5]), 23)

if __name__ == "__main__":
    unittest.main()
