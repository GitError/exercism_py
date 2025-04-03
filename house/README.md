# House

This module provides a function to recite the nursery rhyme "This is the House that Jack Built."

---

## 📝 Function

### `recite(start_verse: int, end_verse: int) -> list[str]`
Generates the verses of the nursery rhyme "This is the House that Jack Built" for the specified range of verses.

#### Parameters:
- `start_verse` (int): The starting verse number (1-based index).
- `end_verse` (int): The ending verse number (1-based index).

#### Returns:
- `list[str]`: A list of strings, where each string is a verse of the nursery rhyme.

---

## 🚀 Usage

### Example 1: Single Verse
```python
from house import recite

print(recite(1, 1))
# Output:
# ['This is the house that Jack built.']
```

### Example 2: Multiple Verses
```python
from house import recite

print(recite(1, 3))
# Output:
# [
#     'This is the house that Jack built.',
#     'This is the malt that lay in the house that Jack built.',
#     'This is the rat that ate the malt that lay in the house that Jack built.'
# ]
```

### Example 3: Full Rhyme
```python
from house import recite

print(recite(1, 12))
# Output:
# [
#     'This is the house that Jack built.',
#     'This is the malt that lay in the house that Jack built.',
#     'This is the rat that ate the malt that lay in the house that Jack built.',
#     ...
#     'This is the horse and the hound and the horn that belonged to the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.'
# ]
```

---