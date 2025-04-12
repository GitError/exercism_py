# Conditionals

This module provides functions to demonstrate the use of conditional statements in Python, with a focus on monitoring and controlling a nuclear reactor's critical parameters.

---

## 📝 Functions

### `example_function(condition: bool) -> str`
Demonstrates the use of a simple conditional statement.

#### Parameters:
- `condition` (bool): A boolean value.

#### Returns:
- `str`: A message based on the condition.

### `is_criticality_balanced(temperature: float, neutrons_emitted: float) -> bool`
Verifies if the nuclear reactor's criticality is balanced.

#### Parameters:
- `temperature` (float): Temperature value in kelvin.
- `neutrons_emitted` (float): Number of neutrons emitted per second.

#### Returns:
- `bool`: `True` if criticality is balanced, `False` otherwise.

### `reactor_efficiency(voltage: float, current: float, theoretical_max_power: float) -> str`
Assesses the reactor's efficiency zone.

#### Parameters:
- `voltage` (float): Voltage value.
- `current` (float): Current value.
- `theoretical_max_power` (float): Power that corresponds to 100% efficiency.

#### Returns:
- `str`: Efficiency band - one of 'green', 'orange', 'red', or 'black'.

### `fail_safe(temperature: float, neutrons_produced_per_second: float, threshold: float) -> str`
Assesses and returns status code for the reactor.

#### Parameters:
- `temperature` (float): Value of the temperature in kelvin.
- `neutrons_produced_per_second` (float): Neutron flux.
- `threshold` (float): Threshold for category.

#### Returns:
- `str`: Status code - one of 'LOW', 'NORMAL', or 'DANGER'.

---

## 🚀 Usage

### Example 1: Basic Conditional Logic
```python
from conditionals import example_function

result = example_function(True)
print(result)  # Output: "Condition is True"
```

### Example 2: Checking Reactor Balance
```python
from conditionals import is_criticality_balanced

# Check if reactor is balanced with temperature 750K and 600 neutrons/sec
balance_status = is_criticality_balanced(750, 600)
print(f"Reactor balanced: {balance_status}")  # Output: "Reactor balanced: True"
```

### Example 3: Monitoring Reactor Efficiency
```python
from conditionals import reactor_efficiency

# Check efficiency with 200V, 50A, and theoretical max of 15000W
efficiency_band = reactor_efficiency(200, 50, 15000)
print(f"Reactor efficiency: {efficiency_band}")  # Output depends on calculated efficiency
```

### Example 4: Fail-Safe Mechanism
```python
from conditionals import fail_safe

# Check safety status with temperature 400K, 500 neutrons/sec, and threshold 10000
status = fail_safe(400, 500, 10000)
print(f"Reactor status: {status}")  # Output depends on calculated values
```

## 📦 Installation

No special installation required. Simply clone the repository and import the module:

```bash
cd exercism_py
```

## 💡 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.