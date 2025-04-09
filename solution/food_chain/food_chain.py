def recite(start_verse, end_verse):
    """
    Generate lyrics for 'I Know an Old Lady Who Swallowed a Fly' song.
    
    This function returns the lyrics for verses from start_verse to end_verse inclusive.
    The song follows a cumulative pattern where each verse adds an animal and describes
    why it was swallowed in reverse order.
    
    Args:
        start_verse (int): The starting verse number (1-indexed)
        end_verse (int): The ending verse number (1-indexed)
        
    Returns:
        list: A list of strings, each representing a line in the song
    """
    animals = [
        "fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"
    ]
    
    special_lines = {
        "fly": "I don't know why she swallowed the fly. Perhaps she'll die.",
        "spider": "It wriggled and jiggled and tickled inside her.",
        "bird": "How absurd to swallow a bird!",
        "cat": "Imagine that, to swallow a cat!",
        "dog": "What a hog, to swallow a dog!",
        "goat": "Just opened her throat and swallowed a goat!",
        "cow": "I don't know how she swallowed a cow!",
        "horse": "She's dead, of course!"
    }
    
    # Generate a single verse based on the animal
    def generate_verse(animal_idx):
        """
        Generate lyrics for a single verse.
        
        Args:
            animal_idx (int): Index of the animal in the animals list (0-indexed)
            
        Returns:
            list: A list of strings representing the lines of the verse
        """
        animal = animals[animal_idx]
        verse = [f"I know an old lady who swallowed a {animal}."]
        
        # Special case for horse - only has two lines
        if animal == "horse":
            verse.append(special_lines[animal])
            return verse
        
        # Add the special line for the current animal
        if animal != "fly":
            verse.append(special_lines[animal])
        
        # Add the recursive "she swallowed X to catch Y" lines
        for i in range(animal_idx, 0, -1):
            current = animals[i]
            previous = animals[i-1]
            
            # Special case for the spider
            if previous == "spider":
                verse.append(f"She swallowed the {current} to catch the {previous} that wriggled and jiggled and tickled inside her.")
            else:
                verse.append(f"She swallowed the {current} to catch the {previous}.")
        
        # Always end with the fly line for all verses except horse
        verse.append(special_lines["fly"])
        return verse
    
    # Generate all requested verses
    result = []
    for i in range(start_verse, end_verse + 1):
        verse = generate_verse(i - 1)  # Verses are 1-indexed, animals are 0-indexed
        result.extend(verse)
        
        # Add a blank line between verses, but not after the last one
        if i < end_verse:
            result.append("")
    
    return result
