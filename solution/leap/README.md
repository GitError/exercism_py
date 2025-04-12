# Leap Year

This module provides a function to determine if a given year is a leap year.

## 📋 Overview

In the Gregorian calendar, a leap year occurs:
- Every year that is divisible by 4
- **Except** every year that is divisible by 100
- **Unless** the year is also divisible by 400

For example, 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, and 2300 are not leap years.

---

## 🔧 Installation

```bash
# Navigate to the project directory
cd leap-year
```

---

## 📝 Function

### `is_leap_year(year: int) -> bool`
Determines if a given year is a leap year.

#### Parameters:
- `year` (int): The year to check.

#### Returns:
- `bool`: `True` if the year is a leap year, `False` otherwise.

---

## 🚀 Usage

### Example 1: Leap Years
```python
from leap import is_leap_year

# Years divisible by 4 (except those divisible by 100 but not 400)
print(is_leap_year(2024))  # Output: True
print(is_leap_year(2000))  # Output: True (divisible by 400)
print(is_leap_year(1996))  # Output: True
```

### Example 2: Non-Leap Years
```python
from leap import is_leap_year

# Years not divisible by 4
print(is_leap_year(2023))  # Output: False

# Years divisible by 100 but not by 400
print(is_leap_year(1900))  # Output: False
print(is_leap_year(2100))  # Output: False
```

---

## 🧪 Testing

Run tests using pytest:

```bash
pytest leap_test.py -v
```

---

## 📜 License

This project is open source and available under the [MIT License](LICENSE).