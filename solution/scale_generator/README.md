# Scale Generator

This is an implementation of a musical scale generator. The program can generate chromatic scales and custom scales based on interval patterns from any given tonic.

## Background

In Western music, scales are based on the chromatic (12-note) scale, which consists of:

- Sharp notation: A, A♯, B, C, C♯, D, D♯, E, F, F♯, G, G♯
- Flat notation: A, B♭, B, C, D♭, D, E♭, E, F, G♭, G, A♭

The choice of sharps or flats depends on the tonic (starting note):

- **Sharp keys**: C, G, D, A, E, B, F♯ (major) and a, e, b, f♯, c♯, g♯, d♯ (minor)
- **Flat keys**: F, B♭, E♭, A♭, D♭, G♭ (major) and d, g, c, f, b♭, e♭ (minor)

## Features

The `Scale` class provides the following functionality:

1. **Chromatic Scale Generation**: Generate a 12-note chromatic scale starting from any tonic.
2. **Custom Interval-Based Scales**: Generate scales using specific interval patterns.

### Intervals

The interval patterns use the following notation:

- `m` - minor second (half step)
- `M` - major second (whole step)
- `A` - augmented second (whole step + half step)

Common scale patterns include:

- Major Scale: `MMmMMMm` (W-W-H-W-W-W-H)
- Natural Minor Scale: `MmMMmMM` (W-H-W-W-H-W-W)
- Dorian Mode: `MmMMMmM`
- Mixolydian Mode: `MMmMMmM`
- Lydian Mode: `MMMmMMm`
- Phrygian Mode: `mMMMmMM`
- Locrian Mode: `mMMmMMM`

## Usage

```python
from scale_generator import Scale

# Create a chromatic scale starting from C
c_chromatic = Scale('C').chromatic()
# Returns ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Create a major scale starting from G
g_major = Scale('G').interval('MMmMMMm')
# Returns ['G', 'A', 'B', 'C', 'D', 'E', 'F#', 'G']

# Create a natural minor scale starting from a
a_minor = Scale('a').interval('MmMMmMM')
# Returns ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'A']
```

## Testing

Run the included test file to verify the functionality:

```bash
python scale_generator_test.py
```

The test suite verifies both chromatic scale generation and various interval-based scale patterns across different tonics.
