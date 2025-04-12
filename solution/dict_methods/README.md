# Dictionary Methods - Shopping Cart Management

This module implements a set of functions for managing shopping carts and store inventory for Mecha Munch™, a grocery shopping automation company.

## Functions

### `add_item(current_cart, items_to_add)`

Adds items to a user's shopping cart. If an item is already in the cart, its quantity is increased.

```python
add_item({'Banana': 3, 'Apple': 2}, ['Banana', 'Orange'])
# Returns: {'Banana': 4, 'Apple': 2, 'Orange': 1}
```

### `read_notes(notes)`

Creates a shopping cart dictionary from a list-like iterable of items.

```python
read_notes(['Banana', 'Apple', 'Orange', 'Banana'])
# Returns: {'Banana': 2, 'Apple': 1, 'Orange': 1}
```

### `update_recipes(ideas, recipe_updates)`

Updates the "recipe ideas" dictionary with new or modified recipes.

```python
update_recipes(
    {'Banana Bread': {'Banana': 1, 'Flour': 1}},
    [('Banana Bread', {'Banana': 4, 'Flour': 1, 'Sugar': 2})]
)
# Returns: {'Banana Bread': {'Banana': 4, 'Flour': 1, 'Sugar': 2}}
```

### `sort_entries(cart)`

Sorts a shopping cart dictionary alphabetically by item name.

```python
sort_entries({'Banana': 3, 'Apple': 2, 'Orange': 1})
# Returns: {'Apple': 2, 'Banana': 3, 'Orange': 1}
```

### `send_to_store(cart, aisle_mapping)`

Combines a user's shopping cart with aisle and refrigeration information, returning a "fulfillment cart" sorted in reverse alphabetical order.

```python
send_to_store(
    {'Banana': 3, 'Apple': 2},
    {'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False]}
)
# Returns: {'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]}
```

### `update_store_inventory(fulfillment_cart, store_inventory)`

Updates the store's inventory based on a fulfillment cart. When an item's inventory falls to 0, it is marked as "Out of Stock".

```python
update_store_inventory(
    {'Banana': [3, 'Aisle 5', False]},
    {'Banana': [5, 'Aisle 5', False]}
)
# Returns: {'Banana': [2, 'Aisle 5', False]}
```

## Performance Optimizations

The implementation uses several optimizations:

- `Counter` from the `collections` module for efficiently counting items
- The `dict.get(key, default)` method to simplify code and reduce conditional checks
- Proper dictionary copying to avoid modifying input data

## Running Tests

The module includes comprehensive tests that validate all functionality:

```bash
python -m unittest dict_methods_test.py
```
