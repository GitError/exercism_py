"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word: str) -> str:
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """
    return f"un{word}"


def make_word_groups(vocab_words: list[str]) -> str:
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
    by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """
    prefix = vocab_words[0]
    return " :: ".join([prefix] + [f"{prefix}{word}" for word in vocab_words[1:]])


def remove_suffix_ness(word: str) -> str:
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """
    root = word[:-4]  # Remove "ness"
    if root.endswith("i"):
        root = root[:-1] + "y"  # Adjust spelling if root ends with "i"
    return root


def adjective_to_verb(sentence: str, index: int) -> str:
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """
    words = sentence.strip(".").split()
    return f"{words[index]}en"


def reverse(text: str) -> str:
    """Reverse the given string.

    :param text: str - The string to reverse.
    :return: str - The reversed string.

    For example:
    "stressed" becomes "desserts".
    "strops" becomes "sports".
    "racecar" remains "racecar".
    """
    return text[::-1]


def is_palindrome(text: str) -> bool:
    """Check if the given string is a palindrome.

    :param text: str - The string to check.
    :return: bool - True if the string is a palindrome, False otherwise.

    A palindrome reads the same forward and backward.
    For example:
    "racecar" is a palindrome.
    "madam" is a palindrome.
    "hello" is not a palindrome.
    """
    return text == text[::-1]


def is_pangram(sentence: str) -> bool:
    """Determine if a sentence is a pangram.

    :param sentence: str - The sentence to check.
    :return: bool - True if the sentence is a pangram, False otherwise.

    A pangram is a sentence that contains every letter of the English alphabet
    at least once, case insensitive.
    """
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(set(sentence.lower()))


def is_isogram(string: str) -> bool:
    """Determine if a word or phrase is an isogram.

    :param string: str - The word or phrase to check.
    :return: bool - True if the input is an isogram, False otherwise.

    An isogram is a word or phrase without a repeating letter,
    ignoring spaces and hyphens.
    """
    # Normalize the string: convert to lowercase and remove spaces and hyphens
    normalized = string.lower().replace(" ", "").replace("-", "")

    # Check if all characters are unique
    return len(set(normalized)) == len(normalized)


def is_valid_isbn(isbn: str) -> bool:
    """Determine if the given string is a valid ISBN-10.

    :param isbn: str - The ISBN-10 string to validate.
    :return: bool - True if the ISBN-10 is valid, False otherwise.

    An ISBN-10 is valid if:
    - It contains exactly 10 characters (digits or 'X' as the check digit).
    - The check digit 'X' represents the value 10.
    - The weighted sum of the digits (using the formula) is divisible by 11.
    """
    # Remove hyphens from the ISBN
    isbn = isbn.replace("-", "")

    # Check if the length is exactly 10
    if len(isbn) != 10:
        return False

    # Validate the first 9 characters are digits and the last character is either a digit or 'X'
    if not isbn[:-1].isdigit() or (isbn[-1] not in "0123456789X"):
        return False

    # Convert the ISBN into a list of integers, treating 'X' as 10
    digits = [int(char) if char.isdigit() else 10 for char in isbn]

    # Calculate the weighted sum using the formula
    weighted_sum = sum(digit * (10 - i) for i, digit in enumerate(digits))

    # Check if the weighted sum is divisible by 11
    return weighted_sum % 11 == 0


def rotate(text: str, key: int) -> str:
    """Encrypt the given text using a rotational cipher (Caesar cipher).

    :param text: str - The input text to encrypt.
    :param key: int - The rotation key (0-26).
    :return: str - The encrypted text.

    The function preserves the case of letters and ignores non-alphabetic characters.
    """
    result = []

    for char in text:
        if char.isalpha():
            # Determine the ASCII offset (uppercase or lowercase)
            offset = ord('A') if char.isupper() else ord('a')
            # Rotate the character and wrap around using modular arithmetic
            rotated_char = chr((ord(char) - offset + key) % 26 + offset)
            result.append(rotated_char)
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)

    return ''.join(result)


def capitalize_title(title: str) -> str:
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """
    return title.title()


def check_sentence_ending(sentence: str) -> bool:
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """
    return sentence.endswith(".")


def clean_up_spacing(sentence: str) -> str:
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """
    return sentence.strip()


def replace_word_choice(sentence: str, old_word: str, new_word: str) -> str:
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """
    return sentence.replace(old_word, new_word)