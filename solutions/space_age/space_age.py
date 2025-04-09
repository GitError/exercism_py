class SpaceAge:
    """
    A class to calculate a person's age on various planets in the Solar System.
    
    The calculation is based on the orbital period of each planet relative to Earth,
    where one Earth year equals 31,557,600 seconds.
    """
    
    def __init__(self, seconds):
        """
        Initialize the SpaceAge class.
        
        Parameters:
            seconds (int or float): The person's age in seconds.
        """
        self.seconds = seconds
        self._earth_year_in_seconds = 31557600
    
    def _years_on_planet(self, orbital_period):
        """
        Calculate age on a planet given its orbital period ratio to Earth.
        
        Parameters:
            orbital_period (float): The planet's orbital period in Earth years.
            
        Returns:
            float: Age on the specified planet, rounded to 2 decimal places.
        """
        earth_years = self.seconds / self._earth_year_in_seconds
        return round(earth_years / orbital_period, 2)
    
    def on_earth(self):
        """
        Calculate age in Earth years.
        
        Returns:
            float: Age in Earth years, rounded to 2 decimal places.
        """
        return self._years_on_planet(1.0)
    
    def on_mercury(self):
        """
        Calculate age in Mercury years.
        
        Returns:
            float: Age in Mercury years, rounded to 2 decimal places.
        """
        return self._years_on_planet(0.2408467)
    
    def on_venus(self):
        """
        Calculate age in Venus years.
        
        Returns:
            float: Age in Venus years, rounded to 2 decimal places.
        """
        return self._years_on_planet(0.61519726)
    
    def on_mars(self):
        """
        Calculate age in Mars years.
        
        Returns:
            float: Age in Mars years, rounded to 2 decimal places.
        """
        return self._years_on_planet(1.8808158)
    
    def on_jupiter(self):
        """
        Calculate age in Jupiter years.
        
        Returns:
            float: Age in Jupiter years, rounded to 2 decimal places.
        """
        return self._years_on_planet(11.862615)
    
    def on_saturn(self):
        """
        Calculate age in Saturn years.
        
        Returns:
            float: Age in Saturn years, rounded to 2 decimal places.
        """
        return self._years_on_planet(29.447498)
    
    def on_uranus(self):
        """
        Calculate age in Uranus years.
        
        Returns:
            float: Age in Uranus years, rounded to 2 decimal places.
        """
        return self._years_on_planet(84.016846)
    
    def on_neptune(self):
        """
        Calculate age in Neptune years.
        
        Returns:
            float: Age in Neptune years, rounded to 2 decimal places.
        """
        return self._years_on_planet(164.79132)
