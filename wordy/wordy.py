def answer(question):
    """Parse and evaluate simple math word problems returning the answer as an integer."""
    # Normalize the question
    question = question.strip().lower()
    
    # Handle special cases
    if question == "what is?":
        raise ValueError("syntax error")
        
    # Check if this is a math question
    if not question.startswith("what is ") or not question.endswith("?"):
        raise ValueError("unknown operation")
    
    # Extract the equation part
    equation = question[8:-1].strip()
    if not equation:
        raise ValueError("syntax error")
    
    # Quickly check for unknown operations before proceeding
    allowed_words = {"plus", "minus", "multiplied", "by", "divided"}
    for word in equation.split():
        # Skip numbers
        if word.lstrip('-').replace('.', '', 1).isdigit():
            continue
        # If it's not an allowed operation word, reject it
        if word not in allowed_words:
            raise ValueError("unknown operation")
    
    # Check for proper structure of operations
    if " multiplied " in equation and " multiplied by " not in equation:
        raise ValueError("syntax error")
    if " divided " in equation and " divided by " not in equation:
        raise ValueError("syntax error")
    
    # Replace operation words with symbols
    equation = (equation.replace("plus", "+")
                         .replace("minus", "-")
                         .replace("multiplied by", "*")
                         .replace("divided by", "/"))
    
    # Split into tokens and validate
    tokens = equation.split()
    
    # Check for proper alternating pattern of numbers and operators
    if len(tokens) % 2 == 0:
        raise ValueError("syntax error")
    
    # Calculate in a single pass
    result = None
    op = None
    
    for i, token in enumerate(tokens):
        if i % 2 == 0:  # Should be a number
            if token in "+-*/":
                raise ValueError("syntax error")
            
            try:
                num = float(token)
                
                if result is None:
                    result = num
                else:
                    if op == "+":
                        result += num
                    elif op == "-":
                        result -= num
                    elif op == "*":
                        result *= num
                    elif op == "/":
                        result /= num
            except ValueError:
                raise ValueError("syntax error")
        else:  # Should be an operator
            if token not in "+-*/":
                raise ValueError("syntax error")
            op = token
    
    # Return integer if result is a whole number
    return int(result) if result == int(result) else result