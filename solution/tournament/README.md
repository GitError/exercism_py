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

