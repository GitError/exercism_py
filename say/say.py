def say(number):
    """
    Convert a number to its English representation in words.
    
    Args:
        number (int): A non-negative integer from 0 to 999,999,999,999 to convert.
        
    Returns:
        str: The English representation of the number.
        
    Raises:
        ValueError: If the input number is negative or greater than 999,999,999,999.
    """
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")
    
    if number == 0:
        return "zero"
    
    # Names for basic numbers
    ones = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
    }
    
    tens = {
        2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 
        6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
    }
    
    scales = ["", "thousand", "million", "billion"]
    
    # Convert a number between 1-99 to words
    def convert_under_hundred(n):
        """
        Convert a number from 1 to 99 to its English representation.
        
        Args:
            n (int): A number between 1 and 99.
            
        Returns:
            str: The English representation of the number.
        """
        if n < 20:
            return ones[n]
        else:
            ten, remainder = divmod(n, 10)
            if remainder == 0:
                return tens[ten]
            else:
                return f"{tens[ten]}-{ones[remainder]}"
    
    # Convert a number between 1-999 to words
    def convert_hundreds(n):
        """
        Convert a number from 1 to 999 to its English representation.
        
        Args:
            n (int): A number between 1 and 999.
            
        Returns:
            str: The English representation of the number.
        """
        if n < 100:
            return convert_under_hundred(n)
        else:
            hundreds, remainder = divmod(n, 100)
            if remainder == 0:
                return f"{ones[hundreds]} hundred"
            else:
                return f"{ones[hundreds]} hundred {convert_under_hundred(remainder)}"
    
    # Split number into groups of thousands and convert each
    chunks = []
    if number == 0:
        return "zero"
    
    num = number
    while num > 0:
        chunks.append(num % 1000)
        num //= 1000
    
    words = []
    for i, chunk in enumerate(chunks):
        if chunk > 0:
            scale = scales[i]
            if scale:
                words.append(f"{convert_hundreds(chunk)} {scale}")
            else:
                words.append(convert_hundreds(chunk))
    
    # Reverse the order since we processed from smallest to largest
    words.reverse()
    
    return " ".join(words)
