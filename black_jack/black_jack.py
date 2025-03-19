"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card: str) -> int:
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.

    1. 'J', 'Q', or 'K' = 10
    2. 'A' = 1
    3. '2' - '10' = numerical value.
    """
    if card in {"J", "Q", "K"}:
        return 10
    if card == "A":
        return 1
    return int(card)


def higher_card(card_one: str, card_two: str) -> str | tuple[str, str]:
    """Determine which card has a higher value in the hand.

    :param card_one: str - first card dealt in hand.
    :param card_two: str - second card dealt in hand.
    :return: str or tuple - the higher card, or both cards if they are of equal value.
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one
    if value_two > value_one:
        return card_two
    return (card_one, card_two)


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for the ace card.

    :param card_one: str - first card dealt.
    :param card_two: str - second card dealt.
    :return: int - either 1 or 11 value of the upcoming ace card.
    """
    total = value_of_card(card_one) + value_of_card(card_two)
    if card_one == "A":
        total += 10
    if card_two == "A":
        total += 10
    return 11 if total + 11 <= 21 else 1


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one: str - first card dealt.
    :param card_two: str - second card dealt.
    :return: bool - True if the hand is a blackjack (two cards worth 21).
    """
    return (
        (card_one == "A" and value_of_card(card_two) == 10)
        or (card_two == "A" and value_of_card(card_one) == 10)
    )


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    :param card_one: str - first card dealt.
    :param card_two: str - second card dealt.
    :return: bool - True if the hand can be split into two pairs.
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet.

    :param card_one: str - first card dealt.
    :param card_two: str - second card dealt.
    :return: bool - True if the hand can be doubled down (totals 9, 10, or 11 points).
    """
    total = value_of_card(card_one) + value_of_card(card_two)
    return total in {9, 10, 11}