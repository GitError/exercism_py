# Football Tournament Table Generator

This module provides a solution for tallying the results of a small football competition and generating a formatted standings table.

## Problem Description

Given a list of match results in the format `Team1;Team2;result`, the code generates a standings table that includes each team's statistics:

- MP: Matches Played
- W: Matches Won
- D: Matches Drawn (Tied)
- L: Matches Lost
- P: Points (3 for a win, 1 for a draw, 0 for a loss)

The table is sorted by points (descending) with ties broken alphabetically by team name.

## Usage

```python
from tournament import tally

# Example input
results = [
    "Allegoric Alaskans;Blithering Badgers;win",
    "Devastating Donkeys;Courageous Californians;draw",
    "Devastating Donkeys;Allegoric Alaskans;win",
    "Courageous Californians;Blithering Badgers;loss",
    "Blithering Badgers;Devastating Donkeys;loss",
    "Allegoric Alaskans;Courageous Californians;win"
]

# Generate the standings table
table = tally(results)

# Print the table
for line in table:
    print(line)
```

## Output

This will produce a formatted standings table:

```
Team                           | MP |  W |  D |  L |  P
Devastating Donkeys            |  3 |  2 |  1 |  0 |  7
Allegoric Alaskans             |  3 |  2 |  0 |  1 |  6
Blithering Badgers             |  3 |  1 |  0 |  2 |  3
Courageous Californians        |  3 |  0 |  1 |  2 |  1
```

## Implementation Details

The solution uses the following approach:

1. Parses each match result and updates team statistics in a dictionary
2. Calculates points based on match outcomes (win=3, draw=1, loss=0)
3. Sorts teams by points (highest first) and then alphabetically by name
4. Formats the output with proper spacing and alignment

## Features

- Robust handling of various input formats
- Skips empty lines and malformed input
- Properly handles teams with equal points
- Clean, efficient implementation with detailed docstrings
- Extensive test coverage for various scenarios

