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

#### Implementation Notes:
- Case-insensitive comparison is used (e.g., "Listen" and "Silent" are considered anagrams)
- A word is not considered an anagram of itself
- Special characters and numbers are considered part of the anagram

---

## 🚀 Usage

### Example 1: Basic Anagram Search
```python
from anagram import find_anagrams

word = "listen"
candidates = ["enlist", "google", "inlets", "banana"]
result = find_anagrams(word, candidates)
print(result)  # Output: ["enlist", "inlets"]
```

### Example 2: Case Insensitivity
```python
from anagram import find_anagrams

word = "Orchestra"
candidates = ["cashregister", "Carthorse", "radishes"]
result = find_anagrams(word, candidates)
print(result)  # Output: ["Carthorse"]
```

### Example 3: Same Word is Not an Anagram
```python
from anagram import find_anagrams

word = "banana"
candidates = ["banana", "BANANA", "anaban"]
result = find_anagrams(word, candidates)
print(result)  # Output: ["anaban"]
```

### Example 4: Special Characters
```python
from anagram import find_anagrams

word = "a-b-c"
candidates = ["c-b-a", "abc", "cab"]
result = find_anagrams(word, candidates)
print(result)  # Output: ["c-b-a"]
```

### Example 5: Numbers
```python
from anagram import find_anagrams

word = "123"
candidates = ["321", "231", "456"]
result = find_anagrams(word, candidates)
print(result)  # Output: ["321", "231"]
```

## ⚠️ Edge Cases

- Empty word: If the target word is empty, only empty strings in the candidates list will match.
- Empty candidates list: Returns an empty list.
- No matches: Returns an empty list if no anagrams are found.

## 📚 Related Concepts

- Anagram: A word or phrase formed by rearranging the letters of a different word or phrase, using all the original letters exactly once.
- Character sorting: The implementation uses character sorting to determine if two words are anagrams.