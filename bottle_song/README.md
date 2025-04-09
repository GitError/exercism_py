# Bottle Song

This is a Python implementation of the "Ten Green Bottles" children's song. The solution generates the lyrics for a specified number of verses starting from a given number of bottles.

## Description

The "Ten Green Bottles" song is a classic counting song where bottles fall from a wall one by one. The song starts with ten bottles and counts down to zero.

The implementation handles the following special cases:
- Singular/plural form: "bottle" vs "bottles"
- Special wording: "one" bottle vs "no" bottles
- Multiple verses with blank lines between them

## Usage

```python
from bottle_song import recite

# Get the first verse (10 bottles)
lyrics = recite(start=10)

# Get the first 3 verses
lyrics = recite(start=10, take=3)

# Get the last verse
lyrics = recite(start=1)

# Print the entire song
lyrics = recite(start=10, take=10)
print("\n".join(lyrics))
```

## Functions

### `recite(start, take=1)`

Recites the lyrics to the Ten Green Bottles song.

**Parameters:**
- `start` (int): The number of bottles to start with (10 for the full song)
- `take` (int, optional): The number of verses to recite. Defaults to 1.

**Returns:**
- A list of strings, each representing a line of the song. Empty strings are used as separators between verses.

## Running Tests

Tests can be run using Python's unittest framework:

```bash
python -m unittest bottle_song_test.py
```

or if you prefer to run the test module directly:

```bash
python bottle_song_test.py
```
