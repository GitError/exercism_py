def score(word):
    """
    Calculate the Scrabble score for a given word.
    
    In Scrabble, each letter has a specific point value. The score of a word
    is the sum of the point values of all letters in the word.
    
    Args:
        word (str): The word to calculate the score for. Case-insensitive.
                    If None is provided, returns 0.
    
    Returns:
        int: The Scrabble score for the given word.
    
    Example:
        >>> score("cabbage")
        14
        >>> score("QUIZ")
        22
    """
    # Letter values according to Scrabble rules
    letter_values = {
        'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
        'D': 2, 'G': 2,
        'B': 3, 'C': 3, 'M': 3, 'P': 3,
        'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
        'K': 5,
        'J': 8, 'X': 8,
        'Q': 10, 'Z': 10
    }
    
    # Convert word to uppercase and sum the values of each letter
    if word is None:
        return 0
        
    return sum(letter_values.get(char.upper(), 0) for char in word)
