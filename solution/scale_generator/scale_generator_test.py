import unittest
from scale_generator import Scale

class ScaleGeneratorTest(unittest.TestCase):
    def test_chromatic_scale_with_sharps(self):
        scale = Scale('C')
        expected = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.assertEqual(scale.chromatic(), expected)

    def test_chromatic_scale_with_flats(self):
        scale = Scale('F')
        expected = ['F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E']
        self.assertEqual(scale.chromatic(), expected)
        
    def test_chromatic_scale_with_lowercase_tonic(self):
        scale = Scale('d')
        expected = ['D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B', 'C', 'Db']
        self.assertEqual(scale.chromatic(), expected)

    def test_major_scale(self):
        # Major scale uses the WWHWWWH pattern (M = W, m = H)
        scale = Scale('C')
        expected = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']
        self.assertEqual(scale.interval('MMmMMMm'), expected)
        
    def test_minor_scale(self):
        # Natural minor scale uses the WHWWHWW pattern
        scale = Scale('a')
        expected = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A']
        self.assertEqual(scale.interval('MmMMmMM'), expected)
        
    def test_dorian_mode(self):
        # Dorian mode uses the WHWWWHW pattern
        scale = Scale('d')
        expected = ['D', 'E', 'F', 'G', 'A', 'B', 'C', 'D']
        self.assertEqual(scale.interval('MmMMMmM'), expected)

    def test_mixolydian_mode(self):
        # Mixolydian mode uses the WWHWWWH pattern
        scale = Scale('G')
        expected = ['G', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.assertEqual(scale.interval('MMmMMmM'), expected)

    def test_lydian_mode(self):
        # Lydian mode uses the WWWHWWH pattern
        scale = Scale('F')
        expected = ['F', 'G', 'A', 'B', 'C', 'D', 'E', 'F']
        self.assertEqual(scale.interval('MMMmMMm'), expected)
        
    def test_phrygian_mode(self):
        # Phrygian mode uses the HWWWHWW pattern
        scale = Scale('e')
        expected = ['E', 'F', 'G', 'A', 'B', 'C', 'D', 'E']
        self.assertEqual(scale.interval('mMMMmMM'), expected)
        
    def test_locrian_mode(self):
        # Locrian mode uses the HWWHWWW pattern
        scale = Scale('b')
        expected = ['B', 'C', 'D', 'E', 'F', 'G', 'A', 'B']
        self.assertEqual(scale.interval('mMMmMMM'), expected)
        
    def test_harmonic_minor(self):
        # Harmonic minor uses the WHWWHWH pattern (with an augmented second)
        scale = Scale('d')
        expected = ['D', 'E', 'F', 'G', 'A', 'Bb', 'Db', 'D']
        self.assertEqual(scale.interval('MmMMmAm'), expected)
        
    def test_pentatonic(self):
        # Major pentatonic uses the WWWWA pattern (augmented second skip)
        scale = Scale('C')
        expected = ['C', 'D', 'E', 'G', 'A', 'C']
        self.assertEqual(scale.interval('MMAMA'), expected)

    def test_enigmatic(self):
        # Enigmatic scale uses the HAWWWWW pattern
        scale = Scale('G')
        expected = ['G', 'G#', 'B', 'C#', 'D#', 'F', 'G']
        self.assertEqual(scale.interval('mAMMMMm'), expected)

if __name__ == '__main__':
    unittest.main()
