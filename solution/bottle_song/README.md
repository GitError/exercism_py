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

### Helper Functions

The implementation uses several helper functions:

- **`number_to_word(num)`**: Converts numbers (0-10) to their word representation
- **`bottle_form(num)`**: Returns "bottle" or "bottles" based on plurality
- **`generate_verse(num)`**: Creates a complete verse for a specific number of bottles

## Example Output

```
Ten green bottles hanging on the wall,
Ten green bottles hanging on the wall,
And if one green bottle should accidentally fall,
There'll be nine green bottles hanging on the wall.

Nine green bottles hanging on the wall,
...
```

## Edge Cases

The implementation handles:

- Numbers beyond the predefined word list (uses string representation)
- Zero or negative `take` values (returns empty list)
- Correct singular/plural forms throughout the song

## Running Tests

Tests can be run using Python's unittest framework:

```bash
python -m unittest bottle_song_test.py
```

or if you prefer to run the test module directly:

```bash
python bottle_song_test.py
```

## Test Coverage

The test suite verifies:
- Individual verses function correctly
- Multiple verses are properly concatenated with blank line separators  
- Edge cases like the final verse with "one" and "no" bottles
- Input validation for various `start` and `take` values
