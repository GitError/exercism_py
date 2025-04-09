# Pirate Treasure Hunt Helper

This module provides functions to help Azara and Rui organize their treasure hunt by matching treasures with locations and cleaning up their records.

---

## 📝 Functions

### `get_coordinate(record: tuple) -> str`
Extracts the coordinate value from a tuple containing the treasure name and treasure coordinate.

#### Parameters:
- `record` (tuple): A tuple containing the treasure name and its coordinate.

#### Returns:
- `str`: The extracted map coordinate.

---

### `convert_coordinate(coordinate: str) -> tuple`
Splits a string coordinate into a tuple containing its individual components.

#### Parameters:
- `coordinate` (str): A string map coordinate.

#### Returns:
- `tuple`: The string coordinate split into its individual components.

---

### `compare_records(azara_record: tuple, rui_record: tuple) -> bool`
Compares two record types and determines if their coordinates match.

#### Parameters:
- `azara_record` (tuple): A tuple containing the treasure name and its coordinate.
- `rui_record` (tuple): A tuple containing the location name, coordinate, and quadrant.

#### Returns:
- `bool`: `True` if the coordinates match, `False` otherwise.

---

### `create_record(azara_record: tuple, rui_record: tuple) -> tuple | str`
Combines the two record types (if possible) and creates a combined record group.

#### Parameters:
- `azara_record` (tuple): A tuple containing the treasure name and its coordinate.
- `rui_record` (tuple): A tuple containing the location name, coordinate, and quadrant.

#### Returns:
- `tuple`: The combined record if the coordinates match.
- `str`: `"not a match"` if the coordinates do not match.

---

### `clean_up(combined_record_group: tuple) -> str`
Cleans up a combined record group into a multi-line string of single records.

#### Parameters:
- `combined_record_group` (tuple): A tuple containing all combined records.

#### Returns:
- `str`: A multi-line string with cleaned records, where excess coordinates and information are removed.

---

## 🚀 Usage

### Example 1: Extracting a Coordinate
```python
from tuples import get_coordinate

record = ("Amethyst Octopus", "1F")
coordinate = get_coordinate(record)
print(coordinate)  # Output: "1F"