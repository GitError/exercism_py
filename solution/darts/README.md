# Darts

Write a function that calculates the earned points in a single toss of a Darts game.

## 🎯 Description

[Darts](https://en.wikipedia.org/wiki/Darts) is a game where players throw darts at a target board which is divided into regions.

In our simplified version of the game, the target is a circle divided into 4 concentric regions:
- Inner circle (radius 1) - 10 points
- Middle circle (radius 5) - 5 points
- Outer circle (radius 10) - 1 point
- Outside the target - 0 points

```
┌────────────────────────────┐
│             ┌──────┐       │
│             │ ┌──┐ │       │
│             │ │··│ │       │
│             │ └──┘ │       │
│             └──────┘       │
│                            │
└────────────────────────────┘
    Outermost: 1 point
    Middle: 5 points
    Inner: 10 points
```

---

## 📝 Function

### `score(x: float, y: float) -> int`
Calculates the score of a dart throw based on its position.

#### Parameters:
- `x` (float): The x-coordinate of the dart.
- `y` (float): The y-coordinate of the dart.

#### Returns:
- `int`: The score based on the distance from the center:
  - 10 points for a distance ≤ 1.
  - 5 points for a distance ≤ 5.
  - 1 point for a distance ≤ 10.
  - 0 points otherwise.

#### Mathematical Approach:
The distance from the center is calculated using the Pythagorean theorem:
`distance = √(x² + y²)`

---

## 🚀 Usage Examples

### Example 1: Bull's Eye (Center)
```python
from darts import score

result = score(0, 0)
print(result)  # Output: 10
```

### Example 2: Middle Circle
```python
from darts import score

result = score(3, 3)  # Distance ≈ 4.24
print(result)  # Output: 5
```

### Example 3: Outer Circle
```python
from darts import score

result = score(7, 7)  # Distance ≈ 9.90
print(result)  # Output: 1
```

### Example 4: Outside Target
```python
from darts import score

result = score(11, 11)  # Distance ≈ 15.56
print(result)  # Output: 0
```

### Example 5: On Circle Boundaries
```python
from darts import score

print(score(1, 0))  # Output: 10 (exactly on inner circle)
print(score(5, 0))  # Output: 5 (exactly on middle circle)
print(score(10, 0))  # Output: 1 (exactly on outer circle)
```

---

## 🧪 Testing

The module comes with test cases to verify functionality. Run the tests using pytest:

```bash
pytest darts_test.py
```

Test cases include:
- Inner circle scoring
- Middle circle scoring
- Outer circle scoring
- Outside target scoring
- Boundary conditions