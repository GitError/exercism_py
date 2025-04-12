# House

This module provides a function to recite the nursery rhyme "This is the House that Jack Built," a classic cumulative tale that builds upon itself with each verse.

## 📖 About the Rhyme

"This is the House that Jack Built" is a popular English nursery rhyme and cumulative tale that dates back to the early 19th century. Each verse builds upon the previous one, making it longer and more complex as the rhyme progresses.

## 📝 Function

### `recite(start_verse: int, end_verse: int) -> list[str]`
Generates the verses of the nursery rhyme "This is the House that Jack Built" for the specified range of verses.

#### Parameters:
- `start_verse` (int): The starting verse number (1-based index).
- `end_verse` (int): The ending verse number (1-based index).

#### Returns:
- `list[str]`: A list of strings, where each string is a verse of the nursery rhyme.

## 🚀 Usage Examples

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
#     'This is the cat that killed the rat that ate the malt that lay in the house that Jack built.',
#     'This is the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.',
#     'This is the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.',
#     'This is the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.',
#     'This is the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.',
#     'This is the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.',
#     'This is the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.',
#     'This is the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.',
#     'This is the horse and the hound and the horn that belonged to the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.'
# ]
```

### Example 4: Specific Range
```python
from house import recite

print(recite(5, 7))
# Output:
# [
#     'This is the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.',
#     'This is the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.',
#     'This is the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.'
# ]
```

## 📋 Verses Overview

1. the house that Jack built
2. the malt that lay in...
3. the rat that ate...
4. the cat that killed...
5. the dog that worried...
6. the cow with the crumpled horn that tossed...
7. the maiden all forlorn that milked...
8. the man all tattered and torn that kissed...
9. the priest all shaven and shorn that married...
10. the rooster that crowed in the morn that woke...
11. the farmer sowing his corn that kept...
12. the horse and the hound and the horn that belonged to...

## 🧪 Testing

Run the tests using:

```bash
python house_test.py
```