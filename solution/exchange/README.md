# Currency Exchange

This module provides functions to calculate currency exchange rates and conversions for travelers handling different currencies.

## 📋 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/currency-exchange.git

# Navigate to the directory
cd currency-exchange
```

---

## 📝 Functions

### `exchange_money(budget: float, exchange_rate: float) -> float`
Calculates the amount of foreign currency received after exchange.
- **Parameters**:
  - `budget`: Amount of money you are planning to exchange
  - `exchange_rate`: Unit value of the foreign currency
- **Returns**: Amount of foreign currency after exchange

### `get_change(budget: float, exchanging_value: float) -> float`
Calculates the remaining budget after exchanging a specific amount.
- **Parameters**:
  - `budget`: Amount of money you own
  - `exchanging_value`: Amount you want to exchange
- **Returns**: Amount left of your starting currency

### `get_value_of_bills(denomination: int, number_of_bills: int) -> int`
Calculates the total value of bills based on denomination and quantity.
- **Parameters**:
  - `denomination`: Value of a single bill
  - `number_of_bills`: Number of bills
- **Returns**: Total value of the bills

### `get_number_of_bills(amount: float, denomination: int = 1) -> int`
Determines how many bills of a specific denomination can be obtained.
- **Parameters**:
  - `amount`: Total value to convert to bills
  - `denomination`: Value of a single bill (default: 1)
- **Returns**: Number of bills that can be obtained

### `get_leftover_of_bills(amount: float, denomination: int) -> float`
Calculates the amount left after getting maximum number of bills.
- **Parameters**:
  - `amount`: Total starting value
  - `denomination`: Value of a single bill
- **Returns**: Amount leftover after exchange

### `exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int`
Calculates maximum value obtainable in foreign currency bills considering exchange fees.
- **Parameters**:
  - `budget`: Amount to exchange
  - `exchange_rate`: Unit value of foreign currency
  - `spread`: Exchange fee percentage
  - `denomination`: Value of a single foreign bill
- **Returns**: Maximum value in foreign currency bills

---

## 🚀 Usage Examples

### Example 1: Exchange Money
```python
from exchange import exchange_money

result = exchange_money(100, 1.2)
print(result)  # Output: 83.33
```

### Example 2: Get Change
```python
from exchange import get_change

result = get_change(100, 45)
print(result)  # Output: 55
```

### Example 3: Calculate Value of Bills
```python
from exchange import get_value_of_bills

result = get_value_of_bills(10, 5)
print(result)  # Output: 50
```

### Example 4: Calculate Maximum Exchangeable Value
```python
from exchange import exchangeable_value

# With a budget of 100, exchange rate of 1.2, spread of 10%, and denomination of 5
result = exchangeable_value(100, 1.2, 10, 5)
print(result)  # Output depends on calculation with spread
```

## 📚 Resources

- [Python numbers documentation](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [Guide to exchanging currency for travel](https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/)