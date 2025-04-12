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

## 🚀 Usage Examples

### Example 1: Eating a Ghost
```python
from arcade_game import eat_ghost

result = eat_ghost(power_pellet_active=True, touching_ghost=True)
print(result)  # Output: True
```

### Example 2: Scoring Points
```python
from arcade_game import score

result = score(touching_power_pellet=True, touching_dot=False)
print(result)  # Output: True

result = score(touching_power_pellet=False, touching_dot=True)
print(result)  # Output: True
```

### Example 3: Losing the Game
```python
from arcade_game import lose

result = lose(power_pellet_active=False, touching_ghost=True)
print(result)  # Output: True
```

### Example 4: Winning the Game
```python
from arcade_game import win

result = win(has_eaten_all_dots=True, power_pellet_active=True, touching_ghost=False)
print(result)  # Output: True
```

## 🎮 Game Logic Summary

| Scenario | Power Pellet | Touching Ghost | All Dots Eaten | Outcome |
|----------|--------------|----------------|----------------|---------|
| Eat Ghost | Active ✅ | Yes ✅ | - | Ghost eaten ✅ |
| Lose | Not Active ❌ | Yes ✅ | - | Game Over ❌ |
| Score | - | - | Touching dot/pellet ✅ | Points earned ✅ |
| Win | - | Not touching ghost or has power pellet | Yes ✅ | Game Won 🏆 |

## 🧪 Testing

Run the included tests to verify functionality:

```bash
pytest arcade_game_test.py
```