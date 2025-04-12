# Pig Latin

This module provides a function to translate English words or phrases into Pig Latin.

## 📋 About Pig Latin

Pig Latin is a language game that involves altering English words according to a simple set of rules:

1. If a word begins with a vowel sound (a, e, i, o, u) or "xr"/"yt", add "ay" to the end of the word.
   - Example: "apple" → "appleay"
   - Example: "xray" → "xrayay"

2. If a word begins with a consonant sound, move all consonants before the first vowel to the end of the word and add "ay".
   - Example: "banana" → "ananabay"
   - Example: "chair" → "airchay"

3. If a word starts with a consonant followed by "qu", move the consonant and "qu" to the end of the word and add "ay".
   - Example: "square" → "aresquay"

4. If a word contains a "y" after one or more consonants, treat the "y" as a vowel.
   - Example: "rhythm" → "ythmrhay"

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

### Example 1: Words Starting with Vowels
```python
from pig_latin import translate

result = translate("apple")
print(result)  # Output: "appleay"

result = translate("eat pie")
print(result)  # Output: "eatay iepay"
```

### Example 2: Words Starting with Consonants
```python
from pig_latin import translate

result = translate("hello")
print(result)  # Output: "ellohay"

result = translate("school")
print(result)  # Output: "oolschay"
```

### Example 3: Words with Special Rules
```python
from pig_latin import translate

result = translate("square")
print(result)  # Output: "aresquay"

result = translate("rhythm")
print(result)  # Output: "ythmrhay"
```

---

## 🛠️ Installation

1. Clone the repository:
```bash
cd pig-latin
```

2. Import the module in your Python code:
```python
from pig_latin import translate
```

---

## 🧪 Testing

Run the tests using pytest:

```bash
pytest pig_latin_test.py
```

---

## 📚 Implementation Details

The implementation handles various edge cases and follows all the rules of Pig Latin translation. It can translate both single words and complete phrases, preserving word boundaries.