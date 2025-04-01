# Bob

This module provides a function to determine Bob's response to various conversational inputs.

---

## 📝 Function

### `response(hey_bob: str) -> str`
Determines Bob's response based on the input string.

#### Parameters:
- `hey_bob` (str): The input string representing what is said to Bob.

#### Returns:
- `str`: Bob's response based on the following rules:
  - If the input is a question and shouted, Bob responds with `"Calm down, I know what I'm doing!"`.
  - If the input is a question, Bob responds with `"Sure."`.
  - If the input is shouted, Bob responds with `"Whoa, chill out!"`.
  - If the input is silent or contains only whitespace, Bob responds with `"Fine. Be that way!"`.
  - Otherwise, Bob responds with `"Whatever."`.

---

## 🚀 Usage

### Example 1: Question
```python
from bob import response

result = response("How are you?")
print(result)  # Output: "Sure."