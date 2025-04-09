# Secret Handshake

This module implements a secret handshake protocol that converts binary numbers into a sequence of actions.

## 📝 Overview

The secret handshake is a way to recognize members of a secret coding club. One person says a number between 1 and 31, and the other person converts it into a series of actions based on its binary representation.

Each bit in the binary representation corresponds to a specific action:

| Binary | Action |
|--------|--------|
| 00001  | wink |
| 00010  | double blink |
| 00100  | close your eyes |
| 01000  | jump |
| 10000  | Reverse the order of the actions |

## 🚀 Usage

```python
from secret_handshake import commands

# Convert binary strings to handshake actions
print(commands("1"))         # Output: ["wink"]
print(commands("10"))        # Output: ["double blink"]
print(commands("1001"))      # Output: ["wink", "jump"]
print(commands("11010"))     # Output: ["jump", "double blink"]
print(commands("11111"))     # Output: ["jump", "close your eyes", "double blink", "wink"]

# Additional examples
print(commands("1"))     # Returns ["wink"]
print(commands("10"))    # Returns ["double blink"]
print(commands("100"))   # Returns ["close your eyes"]
print(commands("1000"))  # Returns ["jump"]
print(commands("11"))    # Returns ["wink", "double blink"]
print(commands("1001"))  # Returns ["wink", "jump"]
print(commands("1111"))  # Returns ["wink", "double blink", "close your eyes", "jump"]
print(commands("10000"))  # Returns [] (empty list, as there are no actions to reverse)
print(commands("10001"))  # Returns ["wink"] (no change with just one action)
print(commands("10011"))  # Returns ["double blink", "wink"] (reversed from "wink", "double blink")
print(commands("11111"))  # Returns ["jump", "close your eyes", "double blink", "wink"] (all actions reversed)
```