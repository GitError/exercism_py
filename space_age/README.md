# Space Age

This exercise calculates how old someone would be on different planets in our Solar System, given an age in seconds.

## Background

One Earth year equals 365.25 Earth days, or 31,557,600 seconds. However, planets in our Solar System have different orbital periods relative to Earth. For example, a year on Mercury is much shorter than a year on Earth, so someone would be much older in Mercury years than in Earth years.

## The Task

Given an age in seconds, the SpaceAge class calculates how old someone would be on each planet in our Solar System.

## Orbital Periods (in Earth years)

- Mercury: 0.2408467
- Venus: 0.61519726
- Earth: 1.0
- Mars: 1.8808158
- Jupiter: 11.862615
- Saturn: 29.447498
- Uranus: 84.016846
- Neptune: 164.79132

## Example

```python
# Creating an instance with one billion seconds
space_age = SpaceAge(1000000000)

# This is one billion seconds on Earth in years
earth_age = space_age.on_earth()  # Returns 31.69

# This is one billion seconds on Mercury in years
mercury_age = space_age.on_mercury()  # Returns 131.57
```

## Running the Tests

To run the tests, use the following command:

```bash
python space_age_test.py
```

## Why Pluto is Not Included

Pluto is no longer classified as a planet in our Solar System by the International Astronomical Union (IAU). In 2006, the IAU defined three criteria for a celestial body to be considered a planet:

1. It must orbit the Sun.
2. It must have sufficient mass to assume a nearly round shape.
3. It must have "cleared the neighborhood" around its orbit.

Pluto fails to meet the third criterion, as it shares its orbital neighborhood with many other objects.
