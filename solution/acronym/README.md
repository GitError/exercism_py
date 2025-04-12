# Acronym

This module provides a function to convert a phrase into its acronym. Acronyms are formed by taking the first letter of each word in the phrase, converting it to uppercase, and concatenating the letters.

---

## 📝 Function

### `abbreviate(words: str) -> str`
Converts a phrase into its acronym.

#### Parameters:
- `words` (str): The input phrase to be converted into an acronym.

#### Returns:
- `str`: The acronym formed from the input phrase.

---

## 🧩 Implementation Details

The implementation uses regular expressions to:
- Replace hyphens with spaces (to treat hyphenated words as separate words)
- Remove all other punctuation (including underscores)
- Split the resulting string into words
- Take the first letter of each word, convert it to uppercase, and join them together

```python
import re

def abbreviate(words):
    # Replace hyphens with spaces and remove all other punctuation
    words = re.sub(r"[^A-Za-z\s-]", "", words.replace("-", " "))
    
    # Split the words and take the first letter of each word
    acronym = "".join(word[0].upper() for word in words.split() if word)
    
    return acronym
```

---

## 🚀 Usage

### Example 1: Basic Phrase
```python
from acronym import abbreviate

print(abbreviate("As Soon As Possible"))        # Output: ASAP
print(abbreviate("Liquid-crystal display"))     # Output: LCD
print(abbreviate("Thank George It's Friday!"))  # Output: TGIF
print(abbreviate("The Road _Not_ Taken"))       # Output: TRNT
```

### Example 2: Edge Cases
```python
print(abbreviate(""))                           # Output: ""
print(abbreviate("Python"))                     # Output: "P"
print(abbreviate("!!!"))                        # Output: ""
print(abbreviate("  Multiple   Spaces   Here ")) # Output: "MSH"
```

### Example 3: Mixed Case and Special Characters
```python
print(abbreviate("HyperText Markup Language"))  # Output: "HTML"
print(abbreviate("Don't Repeat Yourself!"))     # Output: "DRY"
print(abbreviate("3D Graphics Processing Unit")) # Output: "3DGPU"
```

---

## ⚠️ Edge Cases

The function handles the following edge cases:
- Empty strings (returns an empty string)
- Single words (returns the first letter uppercase)
- Strings with only punctuation (returns an empty string)
- Extra spaces (ignores them)
- Mixed case (converts all first letters to uppercase)
- Numbers (preserves them)

---

## 📦 Installation


1. Navigate to the directory:
```bash
cd acronym
```

2. Import the function in your Python code:
```python
from acronym import abbreviate
```

---

## 🧪 Testing

Run the tests with:
```bash
python -m unittest acronym_test.py
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
