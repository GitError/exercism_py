# Transpose

This is a solution to the Exercism Python track's "Transpose" challenge.

## Problem Description

The challenge is to transpose a given input text. Transposing means converting rows to columns and columns to rows.

### Rules:
1. If the input has rows of different lengths, pad to the left with spaces
2. Don't pad to the right
3. All characters from the input should be present in the output
4. If a column in the input contains only spaces in its bottom-most rows, the corresponding output row should contain spaces in its right-most columns

## Solution Approach

The solution uses a column-by-column approach to build the transposed text. The key challenges addressed are:

1. **Handling Different Row Lengths**: The algorithm calculates the maximum line length and processes each column up to this length.

2. **Left Padding**: The algorithm adds spaces where needed to ensure proper left-padding when rows have different lengths.

3. **Character Preservation**: All characters from the input, including spaces, are preserved in the output.

## Time and Space Complexity

- **Time Complexity**: O(n × m) where n is the number of rows and m is the maximum row length
- **Space Complexity**: O(n × m) to store the transposed result

## Example

Input:
```
ABC
DE
```

Output:
```
AD
BE
C
```

## Running Tests

To run the tests for this implementation:

```bash
python transpose_test.py
```
