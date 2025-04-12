# Markdown Parser

A simple Markdown to HTML parser implemented in Python.

## Features

This parser supports the following Markdown syntax:

- Headers (h1 through h6)
- Paragraphs
- Bold text (using `__text__`)
- Italic text (using `_text_`)
- Unordered lists (using `*` for list items)

## Usage

```python
from markdown import parse

# Parse a simple paragraph
html = parse("This is a paragraph")
# Returns: "<p>This is a paragraph</p>"

# Parse headers
html = parse("# This is an H1")
# Returns: "<h1>This is an H1</h1>"

# Parse text formatting
html = parse("This is _italic_ and __bold__ text")
# Returns: "<p>This is <em>italic</em> and <strong>bold</strong> text</p>"

# Parse unordered lists
html = parse("* Item 1\n* Item 2\n* Item 3")
# Returns: "<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>"
```

## Implementation Details

The parser is implemented using a modular approach:

1. `parse_header`: Handles header formatting (h1-h6)
2. `parse_list_item`: Processes formatting within list items
3. `apply_emphasis`: Processes bold and italic formatting
4. `parse`: The main function that processes markdown text line by line

Regular expressions are used to identify and transform Markdown patterns into their HTML equivalents.

## Testing

Run the tests using the following command:

```
python -m unittest test_markdown.py
```

The test suite includes a comprehensive set of test cases to ensure the parser handles all supported Markdown syntax correctly.

## Limitations

- The parser supports basic Markdown syntax but doesn't support more advanced features like tables, code blocks, or nested lists.
- Bold and italic formatting is applied with a simple regex approach, which might not handle all edge cases properly.
- Only unordered lists (with `*`) are supported; ordered lists are not implemented.

## Future Improvements

- Support for ordered lists
- Support for nested lists
- Support for code blocks and inline code
- Support for links and images
- Better handling of emphasis (bold/italic) when nested
