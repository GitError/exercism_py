
---

### **Exchange**
```markdown
# Currency Exchange

This module provides functions to calculate currency exchange rates and conversions.

---

## 📝 Functions

### `exchange_money(budget: float, exchange_rate: float) -> float`
Calculates the amount of foreign currency received after exchange.

### `get_change(budget: float, exchanging_value: float) -> float`
Calculates the remaining budget after exchanging a specific amount.

---

## 🚀 Usage

### Example 1: Exchange Money
```python
from exchange import exchange_money

result = exchange_money(100, 1.2)
print(result)  # Output: 83.33