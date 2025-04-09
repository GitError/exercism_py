# Series

This exercise focuses on extracting all possible contiguous substrings of a specified length from an input string.

## Instructions

Given a string of digits, output all the contiguous substrings of length `n` in that string in the order that they appear.

For example, the string "49142" has the following 3-digit series:
- "491"
- "914"
- "142"

And the following 4-digit series:
- "4914"
- "9142"

If you ask for a 6-digit series from a 5-digit string, the function will raise a ValueError.

## Exception Messages

The function will raise the following exceptions with meaningful error messages:

- `ValueError("series cannot be empty")` - If the input string is empty.
- `ValueError("slice length cannot be zero")` - If the requested slice length is zero.
- `ValueError("slice length cannot be negative")` - If the requested slice length is negative.
- `ValueError("slice length cannot be greater than series length")` - If the requested slice length exceeds the input string length.

## Example Usage

```python
>>> from series import slices
>>> slices("49142", 3)
['491', '914', '142']
>>> slices("49142", 4)
['4914', '9142']
```

## Testing

Run the tests with:

```bash
python series_test.py
```

## Note

This exercise does not require the substrings to be numerically consecutive.
It only requires that they occupy adjacent positions in the input series.
