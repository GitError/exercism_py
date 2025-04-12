# Two Fer

## Introduction
"Two-fer" is short for "two for one". One for X, one for me.

## Instructions
Your task is to determine what to say as you give away the extra cookie.

If you know the person's name, you will say:
```
One for {name}, one for me.
```

If you don't know the person's name, you will say "you" instead.
```
One for you, one for me.
```

## Examples
- For input "Alice": "One for Alice, one for me."
- For input "Bob": "One for Bob, one for me."
- For no input: "One for you, one for me."

## How to Run Tests
To run the tests, execute the following command in your terminal from the project directory:
```
python -m unittest two_fer_test.py
```

## Implementation Notes
This solution uses a conditional expression within an f-string to make the code concise while maintaining readability.
