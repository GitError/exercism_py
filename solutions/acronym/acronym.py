import re

def abbreviate(words):
    """Convert a phrase to its acronym."""
    # Replace hyphens with spaces and remove all other punctuation, including underscores
    words = re.sub(r"[^A-Za-z\s-]", "", words.replace("-", " "))
    
    # Split the words and take the first letter of each word
    acronym = "".join(word[0].upper() for word in words.split() if word)
    
    return acronym
