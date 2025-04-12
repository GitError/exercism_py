# Lasagna

This module provides functions to calculate the preparation and cooking time for a lasagna.

## 📋 Description

A utility library that helps you calculate various timing aspects of making a lasagna. The module keeps track of:
- Expected cooking time
- Remaining time in the oven
- Preparation time based on the number of layers
- Total elapsed cooking time

---

## 🛠️ Installation

Clone the repository and import the module:

```bash
cd lasagna
```

---

## 📝 Functions

### `expected_minutes_in_oven() -> int`
Returns the expected number of minutes the lasagna should be in the oven (40 minutes).

### `remaining_minutes_in_oven(elapsed_time: int) -> int`
Calculates the remaining time in the oven based on the expected cooking time and how long it has already been baking.

### `preparation_time_in_minutes(number_of_layers: int) -> int`
Calculates the preparation time in minutes based on the number of layers in the lasagna (2 minutes per layer).

### `elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int`
Calculates the total time spent making the lasagna, including both preparation and cooking time.

---

## 🚀 Usage

### Example 1: Expected Minutes in Oven
```python
from lasagna import expected_minutes_in_oven

result = expected_minutes_in_oven()
print(result)  # Output: 40
```

### Example 2: Remaining Minutes in Oven
```python
from lasagna import remaining_minutes_in_oven

result = remaining_minutes_in_oven(30)
print(result)  # Output: 10
```

### Example 3: Preparation Time
```python
from lasagna import preparation_time_in_minutes

result = preparation_time_in_minutes(3)
print(result)  # Output: 6
```

### Example 4: Elapsed Time
```python
from lasagna import elapsed_time_in_minutes

result = elapsed_time_in_minutes(3, 20)
print(result)  # Output: 26
```

---

## 🧪 Testing

Run the tests using pytest:

```bash
pytest lasagna_test.py
```