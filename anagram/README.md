# Anagram

This module provides a function to find all anagrams of a given word from a list of candidate words.

## 📝 Function

### `find_anagrams(word: str, candidates: list[str]) -> list[str]`

Finds all anagrams of a word from a list of candidates.

#### Parameters:
- `word` (str): The target word to find anagrams for.
- `candidates` (list[str]): A list of candidate words to check.

#### Returns:
- `list[str]`: A list of words from `candidates` that are anagrams of the target word.

---

## 🚀 Usage

### Example 1: Basic Anagram Search
```python
from anagram import find_anagrams

word = "listen"
candidates = ["enlist", "google", "inlets", "banana"]
result = find_anagrams(word, candidates)
print(result)  # Output: ["enlist", "inlets"]