def is_paired(input_string):
    """Check if all brackets, braces, and parentheses in the input string are balanced.

    :param input_string: str - The input string containing brackets, braces, and parentheses.
    :return: bool - True if all pairs are matched and nested correctly, False otherwise.
    """
    stack = []
    matching_brackets = {')': '(', ']': '[', '}': '{'}

    for char in input_string:
        if char in matching_brackets.values():  # Opening brackets
            stack.append(char)
        elif char in matching_brackets.keys():  # Closing brackets
            if not stack or stack.pop() != matching_brackets[char]:
                return False

    return not stack
