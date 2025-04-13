import unittest
from classes import Alien, new_aliens_collection

class AlienTest(unittest.TestCase):
    def test_constructor(self):
        """Test that an Alien is initialized with correct coordinates and health"""
        alien = Alien(2, 3)
        self.assertEqual(alien.x_coordinate, 2)
        self.assertEqual(alien.y_coordinate, 3)
        self.assertEqual(alien.health, 3)
    
    def test_hit_method(self):
        """Test that the hit method decrements health by 1"""
        alien = Alien(0, 0)
        self.assertEqual(alien.health, 3)
        alien.hit()
        self.assertEqual(alien.health, 2)
        alien.hit()
        self.assertEqual(alien.health, 1)
    
    def test_is_alive_method(self):
        """Test that is_alive returns correct status based on health"""
        alien = Alien(0, 0)
        self.assertTrue(alien.is_alive())
        alien.hit()
        self.assertTrue(alien.is_alive())
        alien.hit()
        self.assertTrue(alien.is_alive())
        alien.hit()
        self.assertFalse(alien.is_alive())
        alien.hit()  # health would be -1
        self.assertFalse(alien.is_alive())
    
    def test_teleport_method(self):
        """Test that teleport correctly updates coordinates"""
        alien = Alien(0, 0)
        alien.teleport(10, -5)
        self.assertEqual(alien.x_coordinate, 10)
        self.assertEqual(alien.y_coordinate, -5)
    
    def test_collision_detection_exists(self):
        """Test that collision_detection method exists and doesn't raise errors"""
        alien = Alien(0, 0)
        other = Alien(1, 1)
        # Just testing that it doesn't raise an exception
        alien.collision_detection(other)
    
    def test_total_aliens_created(self):
        """Test that total_aliens_created increases with each new alien"""
        # Reset to ensure a clean test
        initial_count = Alien.total_aliens_created
        
        alien1 = Alien(0, 0)
        self.assertEqual(Alien.total_aliens_created, initial_count + 1)
        
        alien2 = Alien(1, 1)
        self.assertEqual(Alien.total_aliens_created, initial_count + 2)
        
        # Check that the count is accessible from instances
        self.assertEqual(alien1.total_aliens_created, initial_count + 2)
        self.assertEqual(alien2.total_aliens_created, initial_count + 2)
    
    def test_new_aliens_collection(self):
        """Test that new_aliens_collection creates aliens at the correct positions"""
        positions = [(1, 2), (3, 4), (5, 6)]
        aliens = new_aliens_collection(positions)
        
        self.assertEqual(len(aliens), 3)
        
        self.assertEqual(aliens[0].x_coordinate, 1)
        self.assertEqual(aliens[0].y_coordinate, 2)
        
        self.assertEqual(aliens[1].x_coordinate, 3)
        self.assertEqual(aliens[1].y_coordinate, 4)
        
        self.assertEqual(aliens[2].x_coordinate, 5)
        self.assertEqual(aliens[2].y_coordinate, 6)

if __name__ == '__main__':
    unittest.main()
