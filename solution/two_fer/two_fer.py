"""
Two-fer or 2-fer is short for two for one.
This module provides functionality to generate the string "One for X, one for me."
where X is a name or "you" by default.
"""

def two_fer(name="you"):
    """
    Return a string in the format "One for X, one for me."
    
    :param name: The name to use in the returned string.
                 If None, "you" is used instead.
    :type name: str or None
    :return: A formatted string based on the name parameter
    :rtype: str
    """
    return f"One for {name}, one for me."
