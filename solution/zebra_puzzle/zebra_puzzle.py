import itertools

# Constants for readability
# House positions are 0-indexed in the algorithm
FIRST, SECOND, THIRD, FOURTH, FIFTH = range(5)

# Colors
RED, GREEN, IVORY, YELLOW, BLUE = range(5)
colors_map = {RED: "red", GREEN: "green", IVORY: "ivory", YELLOW: "yellow", BLUE: "blue"}

# Nationalities
ENGLISH, SPANISH, UKRAINIAN, NORWEGIAN, JAPANESE = range(5)
nationalities_map = {ENGLISH: "Englishman", SPANISH: "Spaniard", UKRAINIAN: "Ukrainian", 
                     NORWEGIAN: "Norwegian", JAPANESE: "Japanese"}

# Drinks
COFFEE, TEA, MILK, ORANGE_JUICE, WATER = range(5)
drinks_map = {COFFEE: "coffee", TEA: "tea", MILK: "milk", ORANGE_JUICE: "orange juice", WATER: "water"}

# Pets
DOG, SNAIL, FOX, HORSE, ZEBRA = range(5)
pets_map = {DOG: "dog", SNAIL: "snail", FOX: "fox", HORSE: "horse", ZEBRA: "zebra"}

# Hobbies
DANCING, PAINTING, READING, FOOTBALL, CHESS = range(5)
hobbies_map = {DANCING: "dancing", PAINTING: "painting", READING: "reading", 
               FOOTBALL: "football", CHESS: "chess"}

def solve_zebra_puzzle():
    """
    Solve the famous Zebra Puzzle (also known as Einstein's Puzzle).
    
    The puzzle involves five houses, each with a resident of different nationality,
    who has a different pet, drinks a different beverage, and enjoys a different hobby.
    A set of 15 constraints defines the relationships between these attributes.
    
    Returns:
        tuple: A pair consisting of (water_drinker, zebra_owner) where each is a string
               representing the nationality of the person who drinks water and who owns the zebra.
    """
    # Initialize solution variables
    water_drinker = None
    zebra_owner = None
    
    # Try all possible color permutations
    for colors in itertools.permutations([RED, GREEN, IVORY, YELLOW, BLUE]):
        # Skip if the green house is not immediately to the right of the ivory house (6)
        green_index = colors.index(GREEN)
        ivory_index = colors.index(IVORY)
        if green_index != ivory_index + 1:
            continue
            
        for nationalities in itertools.permutations([ENGLISH, SPANISH, UKRAINIAN, NORWEGIAN, JAPANESE]):
            # Skip if the Norwegian does not live in the first house (10)
            if nationalities[FIRST] != NORWEGIAN:
                continue
                
            # Skip if the Englishman does not live in the red house (2)
            english_index = nationalities.index(ENGLISH)
            red_index = colors.index(RED)
            if english_index != red_index:
                continue
                
            # Skip if the Norwegian does not live next to the blue house (15)
            norwegian_index = nationalities.index(NORWEGIAN)
            blue_index = colors.index(BLUE)
            if abs(norwegian_index - blue_index) != 1:
                continue
                
            for drinks in itertools.permutations([COFFEE, TEA, MILK, ORANGE_JUICE, WATER]):
                # Skip if the Ukrainian does not drink tea (5)
                ukrainian_index = nationalities.index(UKRAINIAN)
                if drinks[ukrainian_index] != TEA:
                    continue
                    
                # Skip if the person in the green house does not drink coffee (4)
                if drinks[green_index] != COFFEE:
                    continue
                    
                # Skip if the person in the middle house does not drink milk (9)
                if drinks[THIRD] != MILK:
                    continue
                    
                for pets in itertools.permutations([DOG, SNAIL, FOX, HORSE, ZEBRA]):
                    # Skip if the Spaniard does not own the dog (3)
                    spanish_index = nationalities.index(SPANISH)
                    if pets[spanish_index] != DOG:
                        continue
                        
                    for hobbies in itertools.permutations([DANCING, PAINTING, READING, FOOTBALL, CHESS]):
                        # Skip if the snail owner does not like dancing (7)
                        snail_index = pets.index(SNAIL)
                        if hobbies[snail_index] != DANCING:
                            continue
                            
                        # Skip if the person in the yellow house is not a painter (8)
                        yellow_index = colors.index(YELLOW)
                        if hobbies[yellow_index] != PAINTING:
                            continue
                            
                        # Skip if the person who plays football does not drink orange juice (13)
                        football_index = hobbies.index(FOOTBALL)
                        if drinks[football_index] != ORANGE_JUICE:
                            continue
                            
                        # Skip if the Japanese person does not play chess (14)
                        japanese_index = nationalities.index(JAPANESE)
                        if hobbies[japanese_index] != CHESS:
                            continue
                            
                        # Skip if the person who enjoys reading does not live next to the person with the fox (11)
                        reading_index = hobbies.index(READING)
                        fox_index = pets.index(FOX)
                        if abs(reading_index - fox_index) != 1:
                            continue
                            
                        # Skip if the painter's house is not next to the house with the horse (12)
                        painting_index = hobbies.index(PAINTING)
                        horse_index = pets.index(HORSE)
                        if abs(painting_index - horse_index) != 1:
                            continue
                            
                        # If we've passed all constraints, we have a solution
                        water_index = drinks.index(WATER)
                        zebra_index = pets.index(ZEBRA)
                        
                        water_drinker = nationalities_map[nationalities[water_index]]
                        zebra_owner = nationalities_map[nationalities[zebra_index]]
                        
                        # Store solution for result
                        return water_drinker, zebra_owner
    
    return None, None  # No solution found (should not happen)

# Cache the solution to avoid recomputation
_solution = None

def drinks_water():
    """
    Return the nationality of the person who drinks water.
    
    This function solves the Zebra Puzzle once (or uses a cached solution)
    and returns the nationality of the resident who drinks water.
    
    Returns:
        str: The nationality of the water drinker (e.g., "Norwegian", "Japanese", etc.)
    """
    global _solution
    if _solution is None:
        _solution = solve_zebra_puzzle()
    return _solution[0]

def owns_zebra():
    """
    Return the nationality of the person who owns the zebra.
    
    This function solves the Zebra Puzzle once (or uses a cached solution)
    and returns the nationality of the resident who owns the zebra.
    
    Returns:
        str: The nationality of the zebra owner (e.g., "Norwegian", "Japanese", etc.)
    """
    global _solution
    if _solution is None:
        _solution = solve_zebra_puzzle()
    return _solution[1]
