import math

def cipher_text(plain_text):
    """Encode the given plain text using the square code cipher.

    :param plain_text: str - The input text to encode.
    :return: str - The encoded text in chunks separated by spaces.
    """
    # Normalize the input: remove spaces and punctuation, and convert to lowercase
    normalized_text = ''.join(char.lower() for char in plain_text if char.isalnum())
    if not normalized_text:
        return ""

    # Determine the number of columns (c) and rows (r)
    length = len(normalized_text)
    c = math.ceil(math.sqrt(length))
    r = math.ceil(length / c)

    # Read down the columns to encode the text
    encoded_chunks = [
        ''.join(normalized_text[row * c + col] if row * c + col < length else ' ' for row in range(r))
        for col in range(c)
    ]

    # Join the chunks with spaces
    return ' '.join(encoded_chunks)
