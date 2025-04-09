import re

def count_words(sentence):
    """
    Count occurrences of each word in a sentence.
    
    Words are case insensitive. Contractions like "don't" count as a single word.
    Words can be separated by any form of punctuation or whitespace.
    Numbers are considered as words.
    Underscores act as separators between words.
    
    Args:
        sentence (str): The input text to analyze.
        
    Returns:
        dict: A dictionary with words as keys and their counts as values.
        
    Example:
        >>> count_words("That's the password: 'PASSWORD 123'!")
        {'that's': 1, 'the': 1, 'password': 2, '123': 1}
    """
    # Convert to lowercase
    sentence = sentence.lower()
    
    # Replace underscores with spaces
    sentence = sentence.replace('_', ' ')
    
    # Replace all punctuation except apostrophes with spaces
    # and handle apostrophes properly (only keep them when they're inside words)
    sentence = re.sub(r'[^\w\s\']', ' ', sentence)
    
    # Handle apostrophes: remove them when they're at the beginning or end of words
    sentence = re.sub(r'\s\'|\'\s|^\'|\'$', ' ', sentence)
    
    # Split the sentence into words
    words = sentence.split()
    
    # Count the occurrences of each word
    word_count = {}
    for word in words:
        # Remove any remaining apostrophes at the beginning or end of the word
        word = word.strip("'")
        if word:  # Skip empty strings
            word_count[word] = word_count.get(word, 0) + 1
    
    return word_count
