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

## 🚀 Usage

### Example 1: Basic Phrase
```python
from acronym import abbreviate

print(abbreviate("As Soon As Possible"))        # Output: ASAP
print(abbreviate("Liquid-crystal display"))     # Output: LCD
print(abbreviate("Thank George It's Friday!"))  # Output: TGIF
print(abbreviate("The Road _Not_ Taken"))       # Output: TRNT
```
