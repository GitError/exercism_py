import string

# Create a reusable translation table for encoding and decoding
ALPHABET = string.ascii_lowercase
CIPHER = ALPHABET[::-1]
TRANSLATION_TABLE = str.maketrans(ALPHABET + string.digits, CIPHER + string.digits)
REVERSE_TRANSLATION_TABLE = str.maketrans(CIPHER + string.digits, ALPHABET + string.digits)

def encode(plain_text):
    """Encode the given plain text using the Atbash cipher.

    :param plain_text: str - The input text to encode.
    :return: str - The encoded text in groups of 5 characters.
    """
    # Normalize the input: remove punctuation, convert to lowercase, and translate
    normalized_text = ''.join(char.lower() for char in plain_text if char.isalnum())
    encoded_text = normalized_text.translate(TRANSLATION_TABLE)

    # Group the encoded text into chunks of 5 characters
    return ' '.join(encoded_text[i:i + 5] for i in range(0, len(encoded_text), 5))


def decode(ciphered_text):
    """Decode the given ciphered text using the Atbash cipher.

    :param ciphered_text: str - The input text to decode.
    :return: str - The decoded plain text.
    """
    # Normalize the input: remove spaces and translate
    normalized_text = ciphered_text.replace(' ', '')
    return normalized_text.translate(REVERSE_TRANSLATION_TABLE)
