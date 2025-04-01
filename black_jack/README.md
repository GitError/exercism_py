# Blackjack Helper

This module provides functions to help play and score a game of blackjack. It includes logic for determining card values, evaluating hands, and making decisions based on the rules of blackjack.

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
- `str`: The higher card.
- `tuple[str, str]`: Both cards if they have equal value.

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

## 🚀 Usage

### Example 1: Value of a Card
```python
from black_jack import value_of_card

result = value_of_card("K")
print(result)  # Output: 10