
---

### **Lasagna**
```markdown
# Lasagna

This module provides functions to calculate the preparation and cooking time for a lasagna.

---

## 📝 Functions

### `expected_minutes_in_oven() -> int`
Returns the expected number of minutes the lasagna should be in the oven.

### `remaining_minutes_in_oven(elapsed_time: int) -> int`
Calculates the remaining time in the oven.

---

## 🚀 Usage

### Example 1: Remaining Minutes
```python
from lasagna import remaining_minutes_in_oven

result = remaining_minutes_in_oven(30)
print(result)  # Output: 10