import unittest
import pytest
from hamming import distance


class HammingTest(unittest.TestCase):
    def test_empty_strands(self):
        self.assertEqual(distance("", ""), 0, "Empty strands should have distance 0")
        
    def test_single_identical_strands(self):
        self.assertEqual(distance("A", "A"), 0, "Identical single-character strands should have distance 0")
        
    def test_single_different_strands(self):
        self.assertEqual(distance("G", "T"), 1, "Different single-character strands should have distance 1")
        
    def test_complete_distance_in_small_strands(self):
        self.assertEqual(distance("AG", "CT"), 2, "Small strands with no matching characters should have distance equal to length")
        
    def test_small_distance_in_small_strands(self):
        self.assertEqual(distance("AT", "CT"), 1, "Small strands with one matching character")
        
    def test_small_distance(self):
        self.assertEqual(distance("GGACG", "GGTCG"), 1, "Distance with single difference")
        
    def test_small_distance_in_long_strands(self):
        self.assertEqual(distance("ACCAGGG", "ACTATGG"), 2, "Distance in longer strands")
        
    def test_large_distance(self):
        self.assertEqual(distance("GATACA", "GCATAA"), 4, "Larger distance")
        
    def test_large_distance_in_off_by_one_strand(self):
        self.assertEqual(distance("GGACGGATTCTG", "AGGACGGATTCT"), 9, "Large distance in off-by-one strand")
        
    def test_empty_strands(self):
        self.assertEqual(distance("", ""), 0, "Zero distance between empty strands")
        
    def test_disallow_first_strand_longer(self):
        with self.assertRaisesRegex(ValueError, "Strands must be of equal length."):
            distance("AATG", "AAA")
            
    def test_disallow_second_strand_longer(self):
        with self.assertRaisesRegex(ValueError, "Strands must be of equal length."):
            distance("ATA", "AGTG")
            
    def test_disallow_left_empty_strand(self):
        with self.assertRaisesRegex(ValueError, "Strands must be of equal length."):
            distance("", "G")
            
    def test_disallow_right_empty_strand(self):
        with self.assertRaisesRegex(ValueError, "Strands must be of equal length."):
            distance("G", "")
            
    def test_real_example_from_assignment(self):
        self.assertEqual(distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"), 7,
                         "Real example from assignment should return 7")


if __name__ == "__main__":
    unittest.main()
