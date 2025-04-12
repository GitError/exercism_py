# OCR Numbers

This exercise involves parsing a string representation of numbers into their decimal equivalents.

## Description

Given a 3 x 4 grid of pipes, underscores, and spaces, this program determines which number is represented, or whether it is garbled.

## OCR Patterns

The binary font uses pipes and underscores, four rows high and three columns wide:

```
 _     _  _     _  _  _  _  _ 
| |  |  _| _||_||_ |_   ||_||_|
|_|  | |_  _|  | _||_|  ||_| _|
                              
```

These parse to the digits "0123456789".

Here's each digit individually:

```
 _       _   _       _   _   _   _   _ 
| |   |  _|  _|  |_| |_  |_    | |_| |_|
|_|   | |_   _|    |  _| |_|   | |_|  _|
                                        
 0    1   2   3    4   5   6   7   8   9
```

## Rules

1. If the input is the correct size but not recognizable, the program returns '?'
2. If the input is the incorrect size (not a multiple of 3 columns or 4 rows), the program raises an error
3. Multi-character binary strings are supported
4. Multiple numbers, one per line, are joined with commas in the output

## Examples

### Single digit recognition

```
 _ 
| |
|_|
   
```

is converted to "0"

### Multiple digits on one line

```
    _  _     _  _  _  _  _ 
  | _| _||_||_ |_   ||_||_|
  ||_  _|  | _||_|  ||_| _|
                           
```

is converted to "1234567890"

### Multiple lines of digits

```
    _  _ 
  | _| _|
  ||_  _|
         
    _  _ 
|_||_ |_ 
  | _||_|
         
 _  _  _ 
  ||_||_|
  ||_| _|
         
```

is converted to "123,456,789"

## Usage

```python
from ocr_numbers import convert

# Single digit example
result = convert([
    " _ ",
    "| |",
    "|_|",
    "   "
])
print(result)  # "0"

# Multiple digits example
result = convert([
    "    _  _ ",
    "  | _| _|",
    "  ||_  _|",
    "         ",
    "    _  _ ",
    "|_||_ |_ ",
    "  | _||_|",
    "         "
])
print(result)  # "123,456"
```