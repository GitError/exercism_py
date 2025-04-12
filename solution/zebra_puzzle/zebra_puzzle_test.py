import unittest
from zebra_puzzle import drinks_water, owns_zebra

class ZebraPuzzleTest(unittest.TestCase):
    """Test cases for the Zebra Puzzle solution."""

    def test_resident_who_drinks_water(self):
        """Test that the correct resident drinks water."""
        self.assertEqual(drinks_water(), "Norwegian")

    def test_resident_who_owns_zebra(self):
        """Test that the correct resident owns the zebra."""
        self.assertEqual(owns_zebra(), "Japanese")
    
    def test_solution_consistency(self):
        """Test that multiple calls return consistent results."""
        first_water_drinker = drinks_water()
        first_zebra_owner = owns_zebra()
        
        # Call again to ensure the cached solution is consistent
        second_water_drinker = drinks_water()
        second_zebra_owner = owns_zebra()
        
        self.assertEqual(first_water_drinker, second_water_drinker)
        self.assertEqual(first_zebra_owner, second_zebra_owner)

if __name__ == "__main__":
    unittest.main()
