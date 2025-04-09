# Pig Latin

This module provides a function to translate English words or phrases into Pig Latin.

---

## 📝 Function

### `translate(text: str) -> str`
Translates a given word or phrase into Pig Latin.

#### Parameters:
- `text` (str): The word or phrase to translate.

#### Returns:
- `str`: The translated text in Pig Latin.

---

## 🚀 Usage

### Example 1: Single Word
```python
from pig_latin import translate

result = translate("hello")
print(result)  # Output: "ellohay"