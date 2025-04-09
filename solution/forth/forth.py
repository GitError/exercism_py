class StackUnderflowError(Exception):
    """Exception raised when an operation needs more items than available on the stack."""
    pass


def evaluate(input_data):
    """
    Evaluates a series of Forth commands and returns the resulting stack.
    
    Supports basic arithmetic (+, -, *, /), stack manipulation (DUP, DROP, SWAP, OVER),
    and word definitions.
    
    Args:
        input_data (list): List of strings, each containing Forth commands
        
    Returns:
        list: The resulting stack after evaluation
        
    Raises:
        StackUnderflowError: When there aren't enough items on the stack for an operation
        ZeroDivisionError: When attempting to divide by zero
        ValueError: For undefined operations or invalid definitions
    """
    stack = []
    definitions = {}
    
    def parse_and_evaluate(tokens):
        """
        Parse and evaluate a list of tokens according to Forth rules.
        
        Args:
            tokens (list): List of Forth tokens to evaluate
        """
        i = 0
        while i < len(tokens):
            token = tokens[i].lower()  # Case-insensitive
            
            # Check if this is a definition
            if token == ':':
                if i + 2 >= len(tokens) or tokens.index(';', i) <= i + 1:
                    raise ValueError("Invalid definition syntax")
                
                # Get the word name and ensure it's not a number
                word_name = tokens[i + 1].lower()
                # Check if it's a number (including negative numbers)
                if word_name.isdigit() or (word_name[0] == '-' and word_name[1:].isdigit()):
                    raise ValueError("illegal operation")
                
                # Replace any previously defined words in the definition
                definition = []
                for def_token in tokens[i + 2:tokens.index(';', i)]:
                    def_token = def_token.lower()
                    if def_token in definitions:
                        definition.extend(definitions[def_token])
                    else:
                        definition.append(def_token)
                
                definitions[word_name] = definition
                i = tokens.index(';', i) + 1
            
            # Handle defined words
            elif token in definitions:
                parse_and_evaluate(definitions[token])
                i += 1
            
            # Handle numbers
            elif token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                stack.append(int(token))
                i += 1
            
            # Handle arithmetic operations
            elif token in ['+', '-', '*', '/']:
                if len(stack) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    if b == 0:
                        raise ZeroDivisionError("divide by zero")
                    stack.append(a // b)  # Integer division
                
                i += 1
            
            # Handle stack manipulation
            elif token == 'dup':
                if not stack:
                    raise StackUnderflowError("Insufficient number of items in stack")
                stack.append(stack[-1])
                i += 1
            
            elif token == 'drop':
                if not stack:
                    raise StackUnderflowError("Insufficient number of items in stack")
                stack.pop()
                i += 1
            
            elif token == 'swap':
                if len(stack) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                stack[-1], stack[-2] = stack[-2], stack[-1]
                i += 1
            
            elif token == 'over':
                if len(stack) < 2:
                    raise StackUnderflowError("Insufficient number of items in stack")
                stack.append(stack[-2])
                i += 1
            
            else:
                raise ValueError("undefined operation")
    
    # Process each line of input
    for line in input_data:
        # Tokenize the input
        tokens = []
        current_token = ""
        in_definition = False
        
        for char in line:
            if char.isspace():
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
            elif char == ':':
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
                tokens.append(':')
                in_definition = True
            elif char == ';':
                if current_token:
                    tokens.append(current_token)
                    current_token = ""
                tokens.append(';')
                in_definition = False
            else:
                current_token += char
        
        if current_token:
            tokens.append(current_token)
        
        parse_and_evaluate(tokens)
    
    return stack
