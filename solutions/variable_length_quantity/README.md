# Variable Length Quantity Encoding/Decoding

## Overview

This project implements Variable Length Quantity (VLQ) encoding and decoding for integer values. VLQ is a universal code that uses a variable number of bytes to represent an arbitrary integer. It is commonly used in file formats where saving space is important.

## How VLQ Works

In VLQ encoding:
- Only the 7 least significant bits of each byte are used for data (bits 0-6)
- The most significant bit (bit 7) is used as a continuation flag:
  - If bit 7 is set (1), it indicates that more bytes follow
  - If bit 7 is clear (0), it indicates the end of the encoded integer

For example:
- Small numbers (0-127) require only one byte
- Larger numbers require multiple bytes, with each byte contributing 7 bits to the value

## Examples

| Number (decimal) | Number (hex) | VLQ Encoded (hex) |
|-----------------|--------------|-------------------|
| 0               | 0x0          | [0x0]             |
| 64              | 0x40         | [0x40]            |
| 127             | 0x7F         | [0x7F]            |
| 128             | 0x80         | [0x81, 0x0]       |
| 8192            | 0x2000       | [0xC0, 0x0]       |
| 16383           | 0x3FFF       | [0xFF, 0x7F]      |
| 16384           | 0x4000       | [0x81, 0x80, 0x0] |

## Implementation

The implementation includes two key functions:

1. `encode(numbers)`: Encodes a list of integers into their VLQ representation
2. `decode(bytes_)`: Decodes a list of VLQ-encoded bytes into the original integers

## Usage

```python
from variable_length_quantity import encode, decode

# Encoding examples
encoded = encode([0x7F])                  # [0x7F]
encoded = encode([0x4000])                # [0x81, 0x80, 0x0]
encoded = encode([0x2000, 0x123456])      # [0xC0, 0x0, 0xC8, 0xE8, 0x56]

# Decoding examples
decoded = decode([0x7F])                  # [0x7F]
decoded = decode([0xC0, 0x0])             # [0x2000]
decoded = decode([0x81, 0x80, 0x0])       # [0x4000]

# Error handling
try:
    decoded = decode([0x81])  # Will raise ValueError - incomplete sequence
except ValueError as e:
    print(e)  # Output: incomplete sequence
```

## Testing

Run the provided test suite to verify the implementation:

```bash
python -m unittest variable_length_quantity_test.py
```

## Resources

- [Wikipedia: Variable-length quantity](https://en.wikipedia.org/wiki/Variable-length_quantity)
- [MIDI file format specification](https://www.midi.org/specifications)
- [Protocol Buffers encoding (uses VLQ variants)](https://developers.google.com/protocol-buffers/docs/encoding)
