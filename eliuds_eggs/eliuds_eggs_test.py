import unittest
from eliuds_eggs import egg_count

class EliudsEggsTest(unittest.TestCase):
    def test_zero_eggs(self):
        self.assertEqual(egg_count(0), 0, "Should return 0 eggs for display value 0")
        
    def test_single_egg(self):
        self.assertEqual(egg_count(1), 1, "Should detect a single egg")
        self.assertEqual(egg_count(2), 1, "Should detect a single egg at position 2")
        self.assertEqual(egg_count(16), 1, "Should detect a single egg at position 5")
        
    def test_multiple_eggs(self):
        self.assertEqual(egg_count(89), 4, "Example case 1: Should detect 4 eggs for display value 89")
        self.assertEqual(egg_count(7), 3, "Should detect 3 eggs for display value 7 (binary 111)")
        self.assertEqual(egg_count(42), 3, "Should detect 3 eggs for display value 42 (binary 101010)")
        
    def test_powers_of_two_minus_one(self):
        # These numbers have all bits set to 1 up to a certain position
        self.assertEqual(egg_count(3), 2, "Should detect 2 eggs for display value 3 (binary 11)")
        self.assertEqual(egg_count(15), 4, "Should detect 4 eggs for display value 15 (binary 1111)")
        self.assertEqual(egg_count(255), 8, "Should detect 8 eggs for display value 255 (binary 11111111)")
        
    def test_large_numbers(self):
        self.assertEqual(egg_count(65535), 16, "Should detect 16 eggs for display value 65535")
        self.assertEqual(egg_count(2147483647), 31, "Should detect 31 eggs for max signed 32-bit integer")

if __name__ == '__main__':
    unittest.main()
