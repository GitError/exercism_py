# Locomotive Engineer

This exercise is focused on implementing functions to help a locomotive engineer keep track of trains, focusing on Python techniques like packing, unpacking, and dictionary manipulation.

## Function Descriptions

### 1. `get_list_of_wagons(*args)`
Creates a unified list of all wagon IDs passed as arguments.

```python
get_list_of_wagons(1, 7, 12, 3, 14, 8, 5)
# Output: [1, 7, 12, 3, 14, 8, 5]
```

### 2. `fix_list_of_wagons(each_wagons_id, missing_wagons)`
Reorganizes wagons by:
- Moving the first two wagons to the end
- Putting the locomotive (ID 1) at the front
- Adding missing wagons behind the locomotive

```python
fix_list_of_wagons([2, 5, 1, 7, 4, 12, 6, 3, 13], [3, 17, 6, 15])
# Output: [1, 3, 17, 6, 15, 7, 4, 12, 6, 3, 13, 2, 5]
```

### 3. `add_missing_stops(route, **kwargs)`
Updates a route dictionary with additional stops along the way.

```python
add_missing_stops({"from": "New York", "to": "Miami"},
                 stop_1="Washington, DC", stop_2="Charlotte", stop_3="Atlanta",
                 stop_4="Jacksonville", stop_5="Orlando")
# Output: {"from": "New York", "to": "Miami", "stops": ["Washington, DC", "Charlotte", "Atlanta", "Jacksonville", "Orlando"]}
```

### 4. `extend_route_information(route, more_route_information)`
Extends route information by merging two dictionaries.

```python
extend_route_information({"from": "Berlin", "to": "Hamburg"}, 
                        {"length": "100", "speed": "50"})
# Output: {"from": "Berlin", "to": "Hamburg", "length": "100", "speed": "50"}
```

### 5. `fix_wagon_depot(wagons_rows)`
Transforms a matrix of wagons organized by color into columns of the same color.

```python
fix_wagon_depot([
    [(2, "red"), (4, "red"), (8, "red")],
    [(5, "blue"), (9, "blue"), (13,"blue")],
    [(3, "orange"), (7, "orange"), (11, "orange")],
])
# Output: [
#    [(2, "red"), (5, "blue"), (3, "orange")],
#    [(4, "red"), (9, "blue"), (7, "orange")],
#    [(8, "red"), (13,"blue"), (11, "orange")]
# ]
```

## Running the Tests

To run the tests, execute:

```bash
python -m unittest locomotive_engineer_test.py
```

## Notes on Implementation

- Each function uses Python's packing and unpacking features
- The `fix_wagon_depot` function uses Python's `zip` function to efficiently transform the matrix
- The `add_missing_stops` function uses dictionary unpacking and list comprehension for concise code
