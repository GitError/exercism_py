# Saddle Points

This exercise involves finding "saddle points" in a matrix of numbers.

## Description

A saddle point is a position in a matrix where the value is:
- The **largest** value in its **row**
- The **smallest** value in its **column**

In other words, a saddle point is a cell whose value is greater than or equal to any cell in the same row and less than or equal to any cell in the same column.

Saddle points are interesting because they represent local maxima in one direction and local minima in another direction.

## Example

Given this matrix:
```
    1  2  3  4
   ---------
1 | 9  8  7  8
2 | 5  3  2  4
3 | 6  6  7  1
```

The saddle point is at position (2,1) with value 5 because:
- 5 is the largest number in row 2
- 5 is the smallest number in column 1

## Requirements

- The function should return a list of positions (row, column) for all saddle points.
- Positions use 1-based indexing (not 0-based).
- If the matrix is irregular (rows of different lengths), raise a ValueError with the message "irregular matrix".
- An empty matrix has no saddle points.

## Performance Considerations

The optimal solution pre-calculates the maximum values in each row and minimum values in each column to avoid redundant calculations, achieving O(n²) time complexity.

## Testing

Run the included tests with:
```
python -m unittest saddle_points_test.py
```

## Edge Cases

- Empty matrices
- Single row or single column matrices
- Matrices where all values are identical
- Matrices with multiple saddle points

## Implementation Notes

The solution provided uses a two-pass approach:
1. First pass: calculate all row maxima and column minima
2. Second pass: identify all saddle points

This approach is more efficient than checking each cell individually against all values in its row and column.
