# Secret Handshake

This module implements a secret handshake protocol that converts binary numbers into a sequence of actions.

## 📝 Overview

The secret handshake is a way to recognize members of a secret coding club. One person says a number between 1 and 31, and the other person converts it into a series of actions based on its binary representation.

Each bit in the binary representation corresponds to a specific action:

| Binary | Decimal | Action |
|--------|---------|--------|
| 00001  | 1       | wink |
| 00010  | 2       | double blink |
| 00100  | 4       | close your eyes |
| 01000  | 8       | jump |
| 10000  | 16      | Reverse the order of the actions |

## 🧠 How It Works

The algorithm works by checking each bit position in the binary input:
1. If the 1st bit (least significant) is set, add "wink" to the result
2. If the 2nd bit is set, add "double blink" to the result
3. If the 3rd bit is set, add "close your eyes" to the result 
4. If the 4th bit is set, add "jump" to the result
5. If the 5th bit is set, reverse the order of all actions

## 🔍 Edge Cases & Special Considerations

- If the 5th bit (reverse) is set but no action bits are set, the result will be an empty list
- Leading zeros are ignored (e.g., "00001" is treated the same as "1")
- Any bits beyond the 5 rightmost bits are ignored
- Input "0" results in an empty list (no actions)

## 💻 Implementation Details

The implementation uses bitwise operations to efficiently check each bit:
- `binary_int = int(binary_str, 2)` converts the binary string to an integer
- `binary_int & (1 << i)` checks if the bit at position i is set
- `binary_int & 0b10000` checks if the reverse bit is set

## 🧪 Testing

The module includes comprehensive test cases covering:
- Individual actions
- Combined actions
- Reversed actions
- Edge cases like empty results and inputs with leading zeros

Run tests using Python's unittest framework:
```
python secret_handshake_test.py
```

## 🚀 Usage Examples

```python
from secret_handshake import commands

# Basic examples
print(commands("1"))         # Output: ["wink"]
print(commands("10"))        # Output: ["double blink"]
print(commands("100"))       # Output: ["close your eyes"]
print(commands("1000"))      # Output: ["jump"]

# Combined actions (no reverse)
print(commands("11"))        # Output: ["wink", "double blink"]
print(commands("1001"))      # Output: ["wink", "jump"]
print(commands("1111"))      # Output: ["wink", "double blink", "close your eyes", "jump"]

# With reverse bit (5th bit set)
print(commands("10000"))     # Output: [] (empty list, as there are no actions to reverse)
print(commands("10001"))     # Output: ["wink"] (no change with just one action)
print(commands("10011"))     # Output: ["double blink", "wink"] (reversed from "wink", "double blink")
print(commands("11111"))     # Output: ["jump", "close your eyes", "double blink", "wink"] (all actions reversed)

# Leading zeros and ignored bits
print(commands("000011"))    # Output: ["wink", "double blink"] (leading zeros ignored)
print(commands("1100001"))   # Output: ["wink"] (bits beyond 5th are ignored)
```