class Scale:
    """
    A class for generating different musical scales.
    
    This class provides functionality to create chromatic scales and custom interval-based scales
    from a given tonic (starting note).
    
    Attributes:
        S_FLATS (list): The chromatic scale using flat notation ('Bb', 'Eb', etc.)
        S_SHARP (list): The chromatic scale using sharp notation ('A#', 'C#', etc.)
        T_FLATS (list): Tonics that should use the flat notation scale
    """
    S_FLATS = 'A Bb B C Db D Eb E F Gb G Ab'.split()
    S_SHARP = 'A A# B C C# D D# E F F# G G#'.split()
    T_FLATS = 'F Bb Eb Ab Db Gb d g c f bb eb'.split()
    
    def __init__(self, tonic: str):
        """
        Initialize a Scale with the specified tonic.
        
        Args:
            tonic (str): The starting note of the scale
        """
        self.scale = self.S_FLATS if tonic in self.T_FLATS else self.S_SHARP
        self.tonic = tonic.capitalize()
        
    def chromatic(self) -> list[str]:
        """
        Generate a chromatic scale starting from the tonic.
        
        Returns:
            list[str]: A 12-note chromatic scale starting from the tonic
        """
        scale, index = self.scale, self.scale.index(self.tonic)
        return scale[index:] + scale[:index]
        
    def interval(self, intervals: str) -> list[str]:
        """
        Generate a scale based on specified intervals.
        
        Args:
            intervals (str): A string where each character represents an interval:
                            'm' for minor (1 semitone)
                            'M' for major (2 semitones)
                            'A' for augmented (3 semitones)
                            
        Returns:
            list[str]: The notes of the generated scale
            
        Raises:
            ValueError: If an invalid interval is provided
        """
        chromatic, notes, index = self.chromatic(), [], 0
        steps = {'m': 1, 'M': 2, 'A': 3}
        for i in intervals:
            try:
                notes += [chromatic[index]]
                index += steps[i] % len(chromatic)
            except:
                raise ValueError("Not a valid interval")
        notes += [chromatic[0]]
        return notes
