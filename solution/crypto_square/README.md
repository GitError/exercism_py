# Crypto Square

This module provides a function to encode a given plain text using the square code cipher.

---

## 🔍 Algorithm Explanation

The square code cipher follows these steps:
1. Normalize the text by removing spaces and punctuation and converting to lowercase
2. Determine the rectangular grid size (columns × rows) based on the text length
3. Place the characters in a row-wise fashion into the grid
4. Read the grid column by column to create the encoded message
5. Group the encoded characters into chunks separated by spaces

---

## 📝 Function

### `cipher_text(plain_text: str) -> str`
Encodes the given plain text using the square code cipher.

#### Parameters:
- `plain_text` (str): The input text to encode.

#### Returns:
- `str`: The encoded text in chunks separated by spaces.

---

## 🚀 Usage

### Example 1: Encode Text
```python
from crypto_square import cipher_text

result = cipher_text("If man was meant to stay on the ground, god would have given us roots.")
print(result)
# Output: "imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn  sseoau "
```

### Example 2: Encode Empty Text
```python
from crypto_square import cipher_text

result = cipher_text("")
print(result)  # Output: ""
```

### Example 3: Encode Single Character
```python
from crypto_square import cipher_text

result = cipher_text("A")
print(result)  # Output: "a"
```

### Example 4: Perfect Square Length
```python
from crypto_square import cipher_text

result = cipher_text("abcd efgh ijkl mnop")
print(result)  # Output: "aeim bfjn cgko dhlp"
```

### Example 5: Non-Square Length
```python
from crypto_square import cipher_text

result = cipher_text("Hello, World!")
print(result)  # Output: "hwe olr llo d  "
```

---

## 📚 Further Details

The square code cipher is a classic transposition cipher that treats the message as a square (or rectangle). 

For the message "Hello, World!" the normalized text is "helloworld". With a length of 10, this gives us a 4×3 grid:

```
h e l l
o w o r
l d
```

Reading down the columns produces: "holw elod lr".

After formatting with spaces: "hol elo lr d  "

Note that the last column is padded with spaces if needed.