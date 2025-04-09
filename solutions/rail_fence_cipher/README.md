# Rail Fence Cipher

A Python implementation of the Rail Fence Cipher, a transposition cipher that follows a zig-zag pattern.

## Description

The Rail Fence cipher is a form of transposition cipher that derives its name from the way in which it's encoded. It was already used by the ancient Greeks.

In the Rail Fence cipher, the message is written downwards on successive "rails" of an imaginary fence, then moving up when reaching the bottom. This creates a zig-zag pattern. The message is then read off in rows.

## Example

For example, using three "rails" and the message "WE ARE DISCOVERED FLEE AT ONCE", the cipherer writes out:

```
W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . A . . . I . . . V . . . D . . . E . . . N . .
```

Then reads off:

```
WECRLTEERDSOEEFEAOCAIVDEN
```

## Usage

```python
from rail_fence_cipher import encode, decode

# Encoding a message
encoded = encode("HELLO WORLD", 3)
print(encoded)  # Outputs: "HOLELWRDLO"

# Decoding a message
decoded = decode("HOLELWRDLO", 3)
print(decoded)  # Outputs: "HELLOWORLD"
```

## Features

- Encode messages using the Rail Fence Cipher
- Decode messages that were encoded with the Rail Fence Cipher
- Supports variable number of rails
- Automatically handles spaces in input messages

## Running Tests

To run the tests, use the following command:

```bash
python rail_fence_cipher_test.py
```

## Implementation Details

The implementation consists of two main functions:

1. `encode(message, rails)`: Encodes a message using the Rail Fence Cipher
2. `decode(encoded_message, rails)`: Decodes a message encoded with the Rail Fence Cipher

Both functions have a time complexity of O(n) where n is the length of the input message.
