# Inventory Management System

This Python module provides functions for managing an inventory system using dictionaries.

## Features

The module includes functions to:

1. Create an inventory from a list of items
2. Add items to an existing inventory
3. Decrement item quantities in inventory
4. Remove items entirely from inventory
5. List available items (with quantity > 0)

## Usage

### Creating an Inventory

```python
from dicts import create_inventory

# Create an inventory from a list of items
items = ["coal", "wood", "wood", "diamond", "diamond", "diamond"]
inventory = create_inventory(items)
# Result: {"coal": 1, "wood": 2, "diamond": 3}
```

### Adding Items to Inventory

```python
from dicts import add_items

# Add items to existing inventory
current_inventory = {"coal": 1}
new_items = ["wood", "iron", "coal", "wood"]
updated_inventory = add_items(current_inventory, new_items)
# Result: {"coal": 2, "wood": 2, "iron": 1}
```

### Decrementing Items in Inventory

```python
from dicts import decrement_items

# Decrement items from inventory
inventory = {"coal": 3, "diamond": 1, "iron": 5}
items_used = ["diamond", "coal", "iron", "iron"]
updated_inventory = decrement_items(inventory, items_used)
# Result: {"coal": 2, "diamond": 0, "iron": 3}
```

### Removing an Item from Inventory

```python
from dicts import remove_item

# Remove an item completely from inventory
inventory = {"coal": 2, "wood": 1, "diamond": 2}
updated_inventory = remove_item(inventory, "coal")
# Result: {"wood": 1, "diamond": 2}
```

### Listing Available Inventory

```python
from dicts import list_inventory

# List only available items (quantity > 0)
inventory = {"coal": 7, "wood": 11, "diamond": 2, "iron": 7, "silver": 0}
available_items = list_inventory(inventory)
# Result: [('coal', 7), ('wood', 11), ('diamond', 2), ('iron', 7)]
```

## Running Tests

The module includes a comprehensive test suite. Run the tests with:

```bash
python -m unittest dicts_test.py
```

## Notes

- Item counts will not drop below 0.
- When an item's count reaches 0, it remains in the inventory but is not included in the list_inventory results.
- Removing an item completely removes it from the inventory dictionary.
