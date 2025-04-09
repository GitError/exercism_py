def roman(number):
    """Convert an Arabic numeral to a Roman numeral."""
    # Define the Roman numeral mappings including the special cases
    roman_numerals = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    # Validate input range
    if not 0 < number < 4000:
        raise ValueError("Number must be between 1 and 3999")
    
    result = ""
    
    # Iterate through the Roman numeral mappings
    for value, symbol in roman_numerals:
        # Add the symbol as many times as the value fits into the number
        while number >= value:
            result += symbol
            number -= value
    
    return result

