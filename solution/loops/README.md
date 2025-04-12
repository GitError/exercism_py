# Loops

This module provides functions to demonstrate the use of loops in Python.

---

## 📝 Functions

### `sum_numbers(numbers: list[int]) -> int`
Calculates the sum of a list of numbers.

### `count_items(lst: list) -> int`
Counts the number of items in a list.

### `count_even_numbers(numbers: list[int]) -> int`
Counts the number of even numbers in a list.

### `round_scores(student_scores: list) -> list`
Rounds all provided student scores to the nearest integer.

### `count_failed_students(student_scores: list) -> int`
Counts the number of failing students (score <= 40).

### `above_threshold(student_scores: list, threshold: int) -> list`
Returns scores that are at or above the given threshold.

### `letter_grades(highest: int) -> list`
Creates a list of grade thresholds based on the highest grade.

### `student_ranking(student_scores: list, student_names: list) -> list`
Organizes student rank, name, and grade information.

### `perfect_score(student_info: list) -> list`
Finds the first student with a perfect score (100).

---

## 🚀 Usage

### Example 1: Sum Numbers
```python
from loops import sum_numbers

result = sum_numbers([1, 2, 3, 4])
print(result)  # Output: 10
```

### Example 2: Count Even Numbers
```python
from loops import count_even_numbers

result = count_even_numbers([1, 2, 3, 4, 6, 8])
print(result)  # Output: 4
```

### Example 3: Working with Student Scores
```python
from loops import round_scores, letter_grades, student_ranking

# Round decimal scores
scores = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
rounded = round_scores(scores)
print(rounded)  # Output: [90, 40, 55, 70, 31, 25, 80, 95, 39, 40]

# Generate letter grade thresholds
thresholds = letter_grades(100)
print(thresholds)  # Output: [41, 56, 71, 86]

# Create student rankings
names = ["Charlie", "Woody", "Alexis", "Fred"]
scores = [90, 88, 75, 64]
rankings = student_ranking(scores, names)
print(rankings)  # Output: ["1. Charlie: 90", "2. Woody: 88", "3. Alexis: 75", "4. Fred: 64"]
```