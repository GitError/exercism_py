# Bob

This module provides a function to determine Bob's response to various conversational inputs.

---

## 📋 Installation

No special installation required. Simply include the bob.py file in your project.

```bash
# Clone the repository (if applicable)
git clone <repository-url>
cd solution/bob
```

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
```

### Example 2: Shouting
```python
from bob import response

result = response("HELLO THERE!")
print(result)  # Output: "Whoa, chill out!"
```

### Example 3: Shouted Question
```python
from bob import response

result = response("WHY ARE YOU DOING THIS?")
print(result)  # Output: "Calm down, I know what I'm doing!"
```

### Example 4: Silence
```python
from bob import response

result = response("   ")
print(result)  # Output: "Fine. Be that way!"
```

### Example 5: Statement
```python
from bob import response

result = response("This is just a statement.")
print(result)  # Output: "Whatever."
```

---

## 🧪 Testing

Run the included test file to verify all functionality is working as expected:

```bash
pytest bob_test.py
```

---

## 👦 About Bob

Bob is a lackadaisical teenager. He's fairly taciturn and tends to respond in a very limited way to conversations:

- He answers questions with "Sure."
- He answers yelling with "Whoa, chill out!"
- He answers yelling questions with "Calm down, I know what I'm doing!"
- He says "Fine. Be that way!" if you address him without actually saying anything
- He answers everything else with "Whatever."

Bob's conversational skills are limited at best, but at least he's consistent!