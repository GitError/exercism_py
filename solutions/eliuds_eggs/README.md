# Eliud's Eggs

## Problem Description

Eliud inherited a chicken coop from her grandmother Tigist, who was known for her inventive but complex solutions. The coop has a digital display that shows an encoded number representing the positions of eggs that can be collected.

### The Encoding Process

1. The coop scans all potential egg-laying spots
2. It marks a `1` for spots with an egg and `0` for empty spots
3. This binary number is converted to decimal and displayed

### Examples

**Example 1**: Seven nests with eggs in positions 1, 3, 4, and 7
```
 _ _ _ _ _ _ _
|E| |E|E| | |E|  -> Binary: 1011001 -> Decimal: 89 -> Actual eggs: 4
```

**Example 2**: Seven nests with an egg only in position 4
```
 _ _ _ _ _ _ _
| | | |E| | | |  -> Binary: 0001000 -> Decimal: 16 -> Actual eggs: 1
```

## Solution

Our solution implements the `egg_count` function, which counts the number of 1 bits in the binary representation of a number. This represents the actual count of eggs in the coop.

### Approach

We use bitwise operations to efficiently count the 1 bits:
- Check if the least significant bit is 1 using bitwise AND (`&`) with 1
- Shift the number right by one position (`>>`) to process the next bit
- Continue until all bits are processed (when the number becomes 0)

## Usage

```python
from eliuds_eggs import egg_count

# Get the number of eggs for display value 89
eggs = egg_count(89)  # Returns 4

# Get the number of eggs for display value 16
eggs = egg_count(16)  # Returns 1
```

## Running Tests

Tests can be run using the Python unittest framework:

```bash
python -m unittest eliuds_eggs_test.py
```
