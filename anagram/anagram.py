def find_anagrams(word, candidates):
    """
    Find all anagrams of a word from a list of candidates.
    
    Args:
        word (str): The target word to find anagrams for
        candidates (list): A list of candidate words to check
        
    Returns:
        list: A list of words from candidates that are anagrams of the target word
    """
    # Convert the target word to lowercase and sort its characters
    word_sorted = sorted(word.lower())
    
    # Initialize an empty list to store anagrams
    anagrams = []
    
    # Check each candidate
    for candidate in candidates:
        # Skip if the candidate is the same word as the target (case-insensitive)
        if candidate.lower() == word.lower():
            continue
            
        # Sort the characters of the candidate (lowercase for comparison)
        candidate_sorted = sorted(candidate.lower())
        
        # If the sorted characters match, it's an anagram
        if candidate_sorted == word_sorted:
            anagrams.append(candidate)
    
    return anagrams