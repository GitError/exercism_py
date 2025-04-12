# Atbash Cipher

This module provides an implementation of the Atbash cipher, an ancient encryption system that substitutes each letter in the alphabet with its reverse counterpart.

## 📜 Background

The Atbash cipher is a simple substitution cipher that originated in ancient Hebrew. For each letter in the alphabet, it substitutes the letter with the letter from the opposite end of the alphabet. For example:
- 'a' becomes 'z'
- 'b' becomes 'y'
- 'z' becomes 'a'
- 'y' becomes 'b'

The cipher retains numbers as they are and removes punctuation and spaces, making it a straightforward but effective way to encode messages.

## 💻 Installation

Clone this repository and navigate to the directory:

```bash
git clone <repository-url>
cd <repository-directory>/solution/atbash_cipher
```

No additional dependencies are required as the implementation uses only standard Python libraries.

## 📝 Functions

### `encode(plain_text: str) -> str`
Encodes the given plain text using the Atbash cipher.

#### Parameters:
- `plain_text` (str): The input text to encode.

#### Returns:
- `str`: The encoded text in groups of 5 characters, with punctuation removed and all letters converted to lowercase.

---

### `decode(ciphered_text: str) -> str`
Decodes the given ciphered text using the Atbash cipher.

#### Parameters:
- `ciphered_text` (str): The input text to decode.

#### Returns:
- `str`: The decoded plain text with spaces removed.

---

## 🚀 Usage

### Example 1: Encoding
```python
from atbash_cipher import encode

result = encode("test")
print(result)  # Output: "gvhg"

result = encode("x123 yes!")
print(result)  # Output: "c123b vh"

# Longer example
result = encode("The quick brown fox jumps over the lazy dog")
print(result)  # Output: "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"
```

### Example 2: Decoding
```python
from atbash_cipher import decode

result = decode("gvhg")
print(result)  # Output: "test"

result = decode("c123b vh")
print(result)  # Output: "x123yes"

# Longer example
result = decode("gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt")
print(result)  # Output: "thequickbrownfoxjumpsoverthelazydog"
```

## 🧪 Testing

Run the included tests with pytest:

```bash
pytest atbash_cipher_test.py
```

## ⚙️ Implementation Details

The implementation uses Python's `string` module and the `str.maketrans()` method to create efficient translation tables for encoding and decoding. The algorithm:

1. For encoding:
   - Removes all non-alphanumeric characters
   - Converts all letters to lowercase
   - Substitutes each letter with its reverse counterpart
   - Groups the result into chunks of 5 characters

2. For decoding:
   - Removes all spaces
   - Substitutes each letter with its reverse counterpart

## 📄 License

This project is available under the [MIT License](https://opensource.org/licenses/MIT).