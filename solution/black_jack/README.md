# Blackjack Helper

This module provides functions to help play and score a game of blackjack. It includes logic for determining card values, evaluating hands, and making decisions based on the rules of blackjack.

---

## 📋 Requirements

- Python 3.8 or higher
- No external dependencies needed

---

## 📝 Functions

### `value_of_card(card: str) -> int`
Determines the scoring value of a card.

#### Parameters:
- `card` (str): The card to evaluate. Can be `'2'` to `'10'`, `'J'`, `'Q'`, `'K'`, or `'A'`.

#### Returns:
- `int`: The value of the card:
  - `'J'`, `'Q'`, `'K'` = 10
  - `'A'` = 1
  - `'2'` to `'10'` = their numerical value.

---

### `higher_card(card_one: str, card_two: str) -> str | tuple[str, str]`
Determines which card has a higher value in the hand.

#### Parameters:
- `card_one` (str): The first card dealt.
- `card_two` (str): The second card dealt.

#### Returns:
- `str`: The higher card when one card has a higher value.
- `tuple[str, str]`: Both cards as a tuple if they have equal value.

---

### `value_of_ace(card_one: str, card_two: str) -> int`
Calculates the most advantageous value for the ace card.

#### Parameters:
- `card_one` (str): The first card dealt.
- `card_two` (str): The second card dealt.

#### Returns:
- `int`: Either 1 or 11, depending on the total value of the hand.

---

### `is_blackjack(card_one: str, card_two: str) -> bool`
Determines if the hand is a "natural" or "blackjack".

#### Parameters:
- `card_one` (str): The first card dealt.
- `card_two` (str): The second card dealt.

#### Returns:
- `bool`: `True` if the hand is a blackjack (two cards worth 21), `False` otherwise.

---

### `can_split_pairs(card_one: str, card_two: str) -> bool`
Determines if a player can split their hand into two hands.

#### Parameters:
- `card_one` (str): The first card dealt.
- `card_two` (str): The second card dealt.

#### Returns:
- `bool`: `True` if the hand can be split into two pairs, `False` otherwise.

---

### `can_double_down(card_one: str, card_two: str) -> bool`
Determines if a blackjack player can place a double down bet.

#### Parameters:
- `card_one` (str): The first card dealt.
- `card_two` (str): The second card dealt.

#### Returns:
- `bool`: `True` if the hand can be doubled down (totals 9, 10, or 11 points), `False` otherwise.

---

## 🚀 Usage Examples

### Example 1: Value of a Card
```python
from black_jack import value_of_card

print(value_of_card("K"))  # Output: 10
print(value_of_card("3"))  # Output: 3
print(value_of_card("A"))  # Output: 1
```

### Example 2: Comparing Cards
```python
from black_jack import higher_card

print(higher_card("10", "5"))    # Output: "10"
print(higher_card("K", "A"))     # Output: "K"
print(higher_card("5", "5"))     # Output: ("5", "5") - a tuple of both cards
```

### Example 3: Determining Ace Value
```python
from black_jack import value_of_ace

print(value_of_ace("5", "5"))    # Output: 11
print(value_of_ace("10", "A"))   # Output: 1
```

### Example 4: Checking for Blackjack
```python
from black_jack import is_blackjack

print(is_blackjack("A", "10"))   # Output: True
print(is_blackjack("10", "9"))   # Output: False
```

### Example 5: Splitting Pairs
```python
from black_jack import can_split_pairs

print(can_split_pairs("5", "5"))  # Output: True
print(can_split_pairs("10", "K")) # Output: True (both worth 10)
print(can_split_pairs("10", "5")) # Output: False
```

### Example 6: Double Down
```python
from black_jack import can_double_down

print(can_double_down("5", "4"))  # Output: True (total is 9)
print(can_double_down("K", "A"))  # Output: False (total is 11 or 21)
```

---

## 🧪 Testing

The module comes with a comprehensive test suite. You can run the tests using pytest:

```bash
pytest black_jack_test.py
```

All tests should pass, verifying that the functions work as expected according to the rules of blackjack.