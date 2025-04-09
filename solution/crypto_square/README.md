# Crypto Square

This module provides a function to encode a given plain text using the square code cipher.

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