# Food Chain

This is a solution to the "Food Chain" exercise from Exercism's Python track.

## Description

The program generates the lyrics to the song "I Know an Old Lady Who Swallowed a Fly."

## Implementation Details

The solution uses an algorithmic approach to generate the song lyrics based on the cumulative nature of the song:

1. Each verse introduces a new animal that the old lady has swallowed.
2. Each animal (except the fly and the horse) has a special line describing the act.
3. After the special line, there's a cascading description of why each animal was swallowed, going backward through the chain.
4. Each verse ends with "I don't know why she swallowed the fly. Perhaps she'll die" (except for the horse).
5. The last verse about the horse is special and only has two lines.

## Key Features

- **Modular Design**: The solution uses a helper function to generate each verse independently.
- **Data-Driven Structure**: Animals and their special lines are stored in data structures, making the code more maintainable.
- **Special Cases**: The code handles special cases like the horse verse and the spider's extended description.
- **Flexible Range**: The function can generate any range of verses from the song.

## Usage

```python
from food_chain import recite

# Generate the first verse
lyrics = recite(1, 1)

# Generate the entire song
full_song = recite(1, 8)

# Generate a specific range of verses
verses_3_to_5 = recite(3, 5)
```

## Testing

Run the included test suite to verify all functionality:

```bash
python food_chain_test.py
```

The tests cover individual verses, combinations of verses, and the complete song.
