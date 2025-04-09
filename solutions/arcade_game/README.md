# Arcade Game: Pac-Man Rules

This module provides functions to implement the rules of the classic arcade game Pac-Man. It includes logic for determining when Pac-Man can eat a ghost, score points, lose the game, or win the game.

---

## 📝 Functions

### `eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool`
Determines if Pac-Man can eat a ghost.

#### Parameters:
- `power_pellet_active` (bool): Indicates if Pac-Man has an active power pellet.
- `touching_ghost` (bool): Indicates if Pac-Man is touching a ghost.

#### Returns:
- `bool`: `True` if Pac-Man can eat the ghost, `False` otherwise.

---

### `score(touching_power_pellet: bool, touching_dot: bool) -> bool`
Determines if Pac-Man has scored by eating a power pellet or a dot.

#### Parameters:
- `touching_power_pellet` (bool): Indicates if Pac-Man is touching a power pellet.
- `touching_dot` (bool): Indicates if Pac-Man is touching a dot.

#### Returns:
- `bool`: `True` if Pac-Man has scored, `False` otherwise.

---

### `lose(power_pellet_active: bool, touching_ghost: bool) -> bool`
Determines if Pac-Man has lost the game by touching a ghost without an active power pellet.

#### Parameters:
- `power_pellet_active` (bool): Indicates if Pac-Man has an active power pellet.
- `touching_ghost` (bool): Indicates if Pac-Man is touching a ghost.

#### Returns:
- `bool`: `True` if Pac-Man has lost the game, `False` otherwise.

---

### `win(has_eaten_all_dots: bool, power_pellet_active: bool, touching_ghost: bool) -> bool`
Determines if Pac-Man has won the game by eating all dots without losing.

#### Parameters:
- `has_eaten_all_dots` (bool): Indicates if Pac-Man has eaten all the dots.
- `power_pellet_active` (bool): Indicates if Pac-Man has an active power pellet.
- `touching_ghost` (bool): Indicates if Pac-Man is touching a ghost.

#### Returns:
- `bool`: `True` if Pac-Man has won the game, `False` otherwise.

---

## 🚀 Usage

### Example 1: Eating a Ghost
```python
from arcade_game import eat_ghost

result = eat_ghost(power_pellet_active=True, touching_ghost=True)
print(result)  # Output: True