# ETL - Extract, Transform, Load

## Description

This small Python module implements an ETL (Extract, Transform, Load) process for the fictional game Lexiconia. The task is to transform the legacy data format for letter scores to a new format.

### Legacy Format
In the legacy format, scores are mapped to lists of letters:
```python
{
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J", "X"],
    10: ["Q", "Z"]
}
```

### New Format
In the new format, individual lowercase letters are mapped to their scores:
```python
{
    "a": 1, "e": 1, "i": 1, "o": 1, "u": 1, "l": 1, "n": 1, "r": 1, "s": 1, "t": 1,
    "d": 2, "g": 2,
    "b": 3, "c": 3, "m": 3, "p": 3,
    "f": 4, "h": 4, "v": 4, "w": 4, "y": 4,
    "k": 5,
    "j": 8, "x": 8,
    "q": 10, "z": 10
}
```

## Usage

```python
from etl import transform

legacy_data = {1: ["A", "E"], 2: ["D", "G"]}
new_data = transform(legacy_data)
# new_data = {"a": 1, "e": 1, "d": 2, "g": 2}
```

## Running Tests

To run the tests, execute the test file from the command line:

```bash
python etl_test.py
```

## Background

This exercise is part of the Exercism Python track and focuses on data transformation. It simulates a real-world scenario where data formats need to change as an application evolves.
