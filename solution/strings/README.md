# Strings

This module provides functions to perform basic string operations.

---

## 📝 Functions

### `reverse_string(s: str) -> str`
Reverses a given string.

### `capitalize_string(s: str) -> str`
Capitalizes the first letter of a string.

### `add_prefix_un(word: str) -> str`
Adds the prefix 'un' to the given word.

### `make_word_groups(vocab_words: list[str]) -> str`
Transforms a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

### `remove_suffix_ness(word: str) -> str`
Removes the suffix 'ness' from the word while keeping spelling in mind.

### `adjective_to_verb(sentence: str, index: int) -> str`
Changes the adjective at the specified index within the sentence to a verb.

### `is_pangram(sentence: str) -> bool`
Determines if a sentence is a pangram (contains every letter of the alphabet).

### `is_isogram(string: str) -> bool`
Determines if a word or phrase is an isogram (no repeating letters).

### `is_palindrome(s: str) -> bool`
Checks if a string reads the same forward and backward.

### `is_valid_isbn(isbn: str) -> bool`
Validates if a string is a valid ISBN-10.

### `rotate(text: str, key: int) -> str`
Encrypts text using a rotational cipher (Caesar cipher).

### `capitalize_title(title: str) -> str`
Converts the first letter of each word in the title to uppercase.

### `check_sentence_ending(sentence: str) -> bool`
Checks if a sentence ends with a period.

### `clean_up_spacing(sentence: str) -> str`
Removes leading and trailing whitespace from a sentence.

### `replace_word_choice(sentence: str, old_word: str, new_word: str)`
Replaces a word in the provided sentence with a new one.

---

## 🚀 Usage

### Example 1: Reverse String
```python
from strings import reverse_string

result = reverse_string("hello")
print(result)  # Output: "olleh"
```

### Example 2: Check if a String is a Palindrome
```python
from strings import is_palindrome

print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False
```

### Example 3: Add Prefix 'un'
```python
from strings import add_prefix_un

print(add_prefix_un("happy"))     # Output: "unhappy"
print(add_prefix_un("manageable")) # Output: "unmanageable"
```

### Example 4: Create Word Groups with Prefix
```python
from strings import make_word_groups

vocab_words = ['en', 'close', 'joy', 'lighten']
print(make_word_groups(vocab_words))  # Output: "en :: enclose :: enjoy :: enlighten"
```

### Example 5: Caesar Cipher Encryption
```python
from strings import rotate

print(rotate("Hello, World!", 5))  # Output: "Mjqqt, Btwqi!"
```