def recite(start_verse, end_verse):
    """
    Returns the lyrics for "The Twelve Days of Christmas" from start_verse to end_verse.
    
    Args:
        start_verse (int): The starting verse number (1-12)
        end_verse (int): The ending verse number (1-12)
        
    Returns:
        list: A list of strings with the lyrics for each verse
    """
    # Define the ordinal names for days
    ordinals = [
        "first", "second", "third", "fourth", "fifth", 
        "sixth", "seventh", "eighth", "ninth", "tenth", 
        "eleventh", "twelfth"
    ]
    
    # Define the gifts for each day (in reverse order for easy construction)
    gifts = [
        "twelve Drummers Drumming",
        "eleven Pipers Piping",
        "ten Lords-a-Leaping",
        "nine Ladies Dancing",
        "eight Maids-a-Milking",
        "seven Swans-a-Swimming",
        "six Geese-a-Laying",
        "five Gold Rings",
        "four Calling Birds",
        "three French Hens",
        "two Turtle Doves",
        "a Partridge in a Pear Tree"
    ]
    
    verses = []
    for day_num in range(start_verse, end_verse + 1):
        day_idx = day_num - 1  # Convert to 0-based index
        
        # Start of the verse
        verse = f"On the {ordinals[day_idx]} day of Christmas my true love gave to me: "
        
        # Add gifts for this day
        if day_num == 1:
            # Special case for day 1
            verse += gifts[-1] + "."
        else:
            # For days 2-12, list all gifts with "and" before the last one
            day_gifts = gifts[-(day_num):]
            verse += ", ".join(day_gifts[:-1])
            verse += f", and {day_gifts[-1]}."
        
        verses.append(verse)
    
    return verses
