# Word Count

This exercise counts how many times each word occurs in a subtitle or text passage.

## Description

The solution analyzes text and counts word frequency while handling various text formatting cases:

- Case insensitivity (e.g., "You" and "you" count as the same word)
- Contractions like "they're" or "it's" are counted as single words
- Words can be separated by any form of punctuation or whitespace
- Numbers are considered valid words

## Examples

Input:
```
"That's the password: 'PASSWORD 123'!", cried the Special Agent.\nSo I fled.
```

Output:
```
{
  "that's": 1,
  "the": 2,
  "password": 2,
  "123": 1,
  "agent": 1,
  "cried": 1,
  "fled": 1,
  "i": 1,
  "so": 1,
  "special": 1
}
```

## Usage

```python
from word_count import count_words

# Count words in a string
result = count_words("Hello, hello world!")
print(result)  # {'hello': 2, 'world': 1}
```

## Testing

Run the tests with:

```
python -m unittest test_word_count.py
```

## Notes

- Punctuation does not form part of words, except for apostrophes in contractions
- The solution handles different types of whitespace (tabs, newlines, spaces)
- Empty strings and strings containing only whitespace will return an empty dictionary
