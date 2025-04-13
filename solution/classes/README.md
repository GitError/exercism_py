# Ellen's Alien Game

This project implements an Alien class for Ellen's game where the player has to fight aliens.

## Class Overview

The `Alien` class represents enemies in Ellen's game with the following features:

### Attributes
- `x_coordinate`: Position on the x-axis
- `y_coordinate`: Position on the y-axis
- `health`: Number of health points (starts at 3)
- `total_aliens_created`: Class variable tracking the number of aliens created

### Methods
- `hit()`: Decrements the alien's health by 1
- `is_alive()`: Returns True if the alien has health > 0, False otherwise
- `teleport(new_x, new_y)`: Updates the alien's coordinates
- `collision_detection(other)`: Placeholder method for future collision detection logic

## Helper Functions

- `new_aliens_collection(positions)`: Creates a list of Alien objects from a list of coordinate tuples

## Complexity Analysis

All methods in the Alien class have O(1) time complexity:
- Constructor: O(1) - Just initializes instance variables
- hit(): O(1) - Simple decrement operation
- is_alive(): O(1) - Simple comparison
- teleport(): O(1) - Simple assignment operations
- collision_detection(): O(1) - Currently just a placeholder

The `new_aliens_collection()` function has:
- Time complexity: O(n) where n is the number of positions
- Space complexity: O(n) for storing the new Alien objects

## Usage Example

```python
# Create an alien
alien = Alien(5, 10)

# Check its position and health
print(f"Alien at ({alien.x_coordinate}, {alien.y_coordinate}) with {alien.health} health")

# Take a hit
alien.hit()
print(f"After hit: {alien.health} health left")

# Teleport away
alien.teleport(20, 30)
print(f"Teleported to: ({alien.x_coordinate}, {alien.y_coordinate})")

# Create multiple aliens
positions = [(0, 0), (10, 10), (20, 20)]
alien_squad = new_aliens_collection(positions)
print(f"Created {len(alien_squad)} aliens")
print(f"Total aliens created: {Alien.total_aliens_created}")
```

## Testing

Run the included unit tests to verify functionality:

```
python -m unittest classes_test.py
```
