# Run-Length Encoding

This is a simple implementation of run-length encoding (RLE) in Python. Run-length encoding is a form of lossless data compression where runs of data (sequences with the same value) are stored as a single data value and count.

## What is Run-Length Encoding?

Run-length encoding (RLE) is a simple form of data compression where runs (consecutive data elements) are replaced by just one data value and a count. It's particularly useful for data that contains many such runs, for example simple graphic images like icons, line drawings, etc.

For example:
```
"WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"  ->  "12WB12W3B24WB"
```

RLE allows the original data to be perfectly reconstructed from the compressed data, which makes it a lossless data compression.

```
"AABCCCDEEEE"  ->  "2AB3CD4E"  ->  "AABCCCDEEEE"
```

## Implementation Details

This implementation provides two main functions:

- `encode(string)`: Converts a string to its run-length encoded form
- `decode(string)`: Converts a run-length encoded string back to its original form

For this implementation:
- The unencoded string only contains letters A through Z (either lower or upper case) and whitespace
- Numbers in the encoded data always represent the count for the following character

## Usage

```python
from run_length_encoding import encode, decode

# Encode a string
encoded = encode("AABBBCCCC")  # Returns "2A3B4C"

# Decode a string
decoded = decode("2A3B4C")     # Returns "AABBBCCCC"
```

## Running Tests

Run the included tests with:

```bash
python -m unittest run_length_encoding_test.py
```

## License

This project is open-source and available under the MIT License.
