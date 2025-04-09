# Hamming Distance Calculator

## Introduction

The Hamming distance is a metric for comparing two DNA strands. It is named after Richard Hamming, who introduced the concept in his work on error-detecting and error-correcting codes.

In the context of genetics, the Hamming distance measures the number of point mutations that could have transformed one DNA strand into another. It's a crucial concept in bioinformatics and is used to measure the similarity between genetic sequences.

## Problem Description

Calculate the Hamming distance between two DNA strands.

The Hamming distance is calculated by comparing two DNA strands and counting how many of the nucleotides are different from their equivalent in the other string.

Example:
```
GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT
^ ^ ^  ^ ^    ^^
```
These two strands have 7 differences, so the Hamming distance is 7.

## Implementation Details

The implementation follows these rules:
- The function takes two string parameters representing DNA strands
- It returns an integer representing the Hamming distance
- If the strands are of different lengths, it raises a ValueError
- The function compares each character at the same position and counts differences

## Usage Examples

```python
from hamming import distance

# Example 1: Calculate distance between identical strands
distance("AAA", "AAA")  # Returns 0

# Example 2: Calculate distance between different strands
distance("AGT", "ACT")  # Returns 1

# Example 3: Handle error case with different strand lengths
try:
    distance("AGTC", "AGT")  # Raises ValueError
except ValueError as e:
    print(e)  # Outputs: "Strands must be of equal length."
```

## Testing

Run the provided test suite to verify your implementation:

```bash
python -m unittest hamming_test.py
```

or:

```bash
pytest hamming_test.py
```
