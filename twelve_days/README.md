# Twelve Days

This exercise implements the lyrics of the Christmas carol "The Twelve Days of Christmas".

## Description

The traditional Christmas carol "The Twelve Days of Christmas" lists the gifts given on each of the twelve days. The program recites the lyrics to that beloved Christmas carol.

In this exercise, you'll write a Python function that returns the lyrics of the Christmas carol "The Twelve Days of Christmas". Each verse should be a string in a list of strings.

## Usage

```python
from twelve_days import recite

# Get a single verse (the first one)
first_verse = recite(1, 1)
# Result: ["On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."]

# Get a range of verses (first three)
three_verses = recite(1, 3)
# Result: [
#   "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.",
#   "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.",
#   "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."
# ]
```

## Implementation Details

The solution uses:
- A list of ordinal names for days (first, second, etc.)
- A list of gifts in reverse order to simplify verse construction
- Special handling for the first day which has a different pattern
- String formatting to create each verse with proper punctuation

The `recite(start_verse, end_verse)` function takes two parameters:
- `start_verse`: The first verse to generate (1-12)
- `end_verse`: The last verse to generate (1-12)

It returns a list of strings, where each string is one complete verse of the song.

## Running the Tests

To run the tests for this exercise, navigate to the directory containing this exercise and run:

```
pytest twelve_days_test.py
```

## Source

This is a classic Christmas carol.
