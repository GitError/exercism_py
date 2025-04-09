def transform(legacy_data):
    """
    Transform the legacy letter-score data format to a new one-to-one mapping.
    
    The legacy format maps scores to lists of uppercase letters.
    The new format maps lowercase letters to their individual scores.
    
    Args:
        legacy_data (dict): A dictionary mapping scores to lists of uppercase letters
                           Example: {1: ["A", "E"], 2: ["D", "G"]}
    
    Returns:
        dict: A dictionary mapping lowercase letters to their scores
              Example: {"a": 1, "e": 1, "d": 2, "g": 2}
    """
    new_data = {}
    
    for score, letters in legacy_data.items():
        for letter in letters:
            new_data[letter.lower()] = score
            
    return new_data
