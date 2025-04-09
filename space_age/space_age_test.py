import unittest
from space_age import SpaceAge


class SpaceAgeTest(unittest.TestCase):
    def test_age_on_earth(self):
        space_age = SpaceAge(1000000000)
        self.assertEqual(space_age.on_earth(), 31.69)
    
    def test_age_on_mercury(self):
        space_age = SpaceAge(2134835688)
        self.assertEqual(space_age.on_mercury(), 280.88)
    
    def test_age_on_venus(self):
        space_age = SpaceAge(189839836)
        self.assertEqual(space_age.on_venus(), 9.78)
    
    def test_age_on_mars(self):
        space_age = SpaceAge(2129871239)
        self.assertEqual(space_age.on_mars(), 35.88)
    
    def test_age_on_jupiter(self):
        space_age = SpaceAge(901876382)
        self.assertEqual(space_age.on_jupiter(), 2.41)
    
    def test_age_on_saturn(self):
        space_age = SpaceAge(2000000000)
        self.assertEqual(space_age.on_saturn(), 2.15)
    
    def test_age_on_uranus(self):
        space_age = SpaceAge(1210123456)
        self.assertEqual(space_age.on_uranus(), 0.46)
    
    def test_age_on_neptune(self):
        space_age = SpaceAge(1821023456)
        self.assertEqual(space_age.on_neptune(), 0.35)
    
    def test_invalid_input(self):
        # Test with negative seconds
        space_age = SpaceAge(-1000)
        # The calculation should still work mathematically, resulting in negative ages
        self.assertEqual(space_age.on_earth(), -0.03)
    
    def test_zero_seconds(self):
        space_age = SpaceAge(0)
        self.assertEqual(space_age.on_earth(), 0.0)
        self.assertEqual(space_age.on_mercury(), 0.0)


if __name__ == "__main__":
    unittest.main()
