# Scrabble Score

This solution calculates the Scrabble score for a given word.

## Description

In the game of Scrabble, each letter has a specific value. The score of a word is the sum of the letter values of all letters in the word.

Here's how letters are scored in Scrabble:

| Letters                      | Value |
|------------------------------|-------|
| A, E, I, O, U, L, N, R, S, T | 1     |
| D, G                         | 2     |
| B, C, M, P                   | 3     |
| F, H, V, W, Y                | 4     |
| K                            | 5     |
| J, X                         | 8     |
| Q, Z                         | 10    |

## Example

The word "cabbage" scores 14 points:
- 'c': 3 points
- 'a': 1 point
- 'b': 3 points
- 'b': 3 points
- 'a': 1 point
- 'g': 2 points
- 'e': 1 point

Total: 14 points

## Implementation Details

The solution uses a dictionary to map each letter to its corresponding score value. The word is processed character by character, with each letter's score added to the total.

Features:
- Case-insensitive scoring
- Handles empty strings and None inputs
- Ignores non-letter characters (they score 0)

## Running Tests

```bash
python -m unittest test_scrabble_score.py
```
