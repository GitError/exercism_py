# Proverb

This exercise demonstrates the generation of a proverb based on a list of input words.

## Description

For want of a horseshoe nail, a kingdom was lost, or so the saying goes.

Given a list of inputs, this program generates the relevant proverb. For example, given the list `["nail", "shoe", "horse", "rider", "message", "battle", "kingdom"]`, it will output the full text of this proverbial rhyme:

```
For want of a nail the shoe was lost.
For want of a shoe the horse was lost.
For want of a horse the rider was lost.
For want of a rider the message was lost.
For want of a message the battle was lost.
For want of a battle the kingdom was lost.
And all for the want of a nail.
```

## Implementation

The implementation provides a `proverb` function that:
- Takes a variable number of words as positional arguments
- Accepts an optional `qualifier` keyword argument to modify the final verse
- Returns a list of strings representing each line of the proverb

### Time Complexity

The solution has O(n) time complexity, where n is the number of input words. This is optimal as we need to process each word at least once to generate the proverb.

### Space Complexity

The space complexity is also O(n), as the output size grows linearly with the input size.

## Examples

```python
>>> proverb("nail", "shoe", "horse")
[
  "For want of a nail the shoe was lost.",
  "For want of a shoe the horse was lost.",
  "And all for the want of a nail."
]

>>> proverb("nail", "shoe", qualifier="rusty")
[
  "For want of a nail the shoe was lost.",
  "And all for the want of a rusty nail."
]
```

## Running Tests

To run the tests, execute:

```
python -m unittest proverb_test.py
```

or alternatively:

```
pytest proverb_test.py
```
