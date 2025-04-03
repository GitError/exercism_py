# Exercism Python Solutions

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-blue)
![Exercises](https://img.shields.io/badge/Exercises-40%2B-brightgreen)
![Build](https://img.shields.io/badge/Build-Passing-brightgreen)
![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen)

This repository contains my solutions to Python exercises from [Exercism](https://exercism.org/), a platform for practicing and improving coding skills through interactive exercises.

---

## 📚 About

The exercises in this repository demonstrate various Python programming concepts and problem-solving techniques. They are designed to help:

- Master Python programming fundamentals and advanced concepts.
- Learn best practices, coding standards, and idiomatic Python.
- Develop algorithmic thinking and problem-solving skills.
- Prepare for technical interviews and real-world programming challenges.

All solutions follow [PEP 8](https://peps.python.org/pep-0008/) style guidelines and include appropriate documentation.

---

## 🗂️ Repository Structure

Each exercise is contained in its own directory with a consistent structure:

```
exercise_name/
├── exercise_name.py      # Solution implementation
├── exercise_name_test.py # Test cases
└── README.md             # Exercise description and requirements
```

---

## 🧩 Exercise Categories

### Fundamentals
- **[lasagna/](./lasagna/)**: Functions for calculating preparation times (basic function concepts).
- **[conditionals/](./conditionals/)**: Implementing control statements.
- **[arcade_game/](./arcade_game/)**: Classic game rule implementation.
- **[leap/](./leap/)**: Leap year determination algorithm.
- **[exchange/](./exchange/)**: Currency exchange calculation.
- **[hello_world/](./hello_world/)**: Basic "Hello, World!" program.

### String Operations
- **[strings/](./strings/)**: Basic string manipulation techniques.
- **[pig_latin/](./pig_latin/)**: Text translation according to specific rules.
- **[bob/](./bob/)**: Response generation based on input patterns.
- **[reverse_string/](./reverse_string/)**: Reversing strings efficiently.
- **[matching_brackets/](./matching_brackets/)**: Verifying balanced brackets, braces, and parentheses.
- **[crypto_square/](./crypto_square/)**: Encoding text using the square code cipher.
- **[rna_transcription/](./rna_transcription/)**: Transcribing DNA strands into RNA.
- **[atbash_cipher/](./atbash_cipher/)**: Encoding and decoding text using the Atbash cipher.

### Data Structures
- **[lists/](./lists/)**: Basic list operations and transformations.
- **[sublist/](./sublist/)**: Compare relationships between lists.
- **[all_your_base/](./all_your_base/)**: Base conversion algorithms.
- **[loops/](./loops/)**: Iterative operations and student score calculations.
- **[binary_search/](./binary_search/)**: Efficient searching in sorted lists.
- **[list_ops/](./list_ops/)**: Implementing basic list operations like map, filter, and fold.

### Mathematics
- **[grains/](./grains/)**: Exponential growth calculation.
- **[perfect_numbers/](./perfect_numbers/)**: Number classification.
- **[armstrong_numbers/](./armstrong_numbers/)**: Validating Armstrong numbers.
- **[collatz_conjecture/](./collatz_conjecture/)**: Implementation of a mathematical sequence.
- **[raindrops/](./raindrops/)**: Advanced FizzBuzz-style problem.
- **[triangle/](./triangle/)**: Geometric shape validation.
- **[prime_factors/](./prime_factors/)**: Prime factorization of numbers.
- **[largest_series_product/](./largest_series_product/)**: Finding the largest product in a series of digits.

### Games & Simulations
- **[black_jack/](./black_jack/)**: Card game rules implementation.
- **[darts/](./darts/)**: Scoring system for a target game.
- **[tic_tac_toe/](./tic_tac_toe/)**: Implementation of a classic game.

### Electronics
- **[resistor_color/](./resistor_color/)**: Basic resistor color codes.
- **[resistor_color_duo/](./resistor_color_duo/)**: Two-band resistor values.
- **[resistor_color_trio/](./resistor_color_trio/)**: Three-band resistor values.
- **[resistor_color_expert/](./resistor_color_expert/)**: Full resistor value and tolerance calculation.

### Miscellaneous
- **[tuples/](./tuples/)**: Organizing treasure hunt data using tuples.
- **[anagram/](./anagram/)**: Finding anagrams from a list of candidates.
- **[scrabble_score/](./scrabble_score/)**: Calculating Scrabble word scores.
- **[diamond/](./diamond/)**: Generating a diamond shape based on a given letter.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher.
- pip (Python package installer).
- pytest (for running tests).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/exercism-python-solutions.git
   cd exercism-python-solutions
   ```

2. Set up a virtual environment (recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install pytest
   ```

---

## 📝 Running Solutions

You can run any solution directly:
```bash
python exercise_name/exercise_name.py
```

### Running Tests

To verify a solution against the test cases:
```bash
# Run tests for a specific exercise
pytest exercise_name/exercise_name_test.py

# Run all tests
pytest
```

---

## 📝 Learning Points

Each solution demonstrates one or more of the following Python concepts:

- Clean, readable code following Python idioms.
- Effective use of data structures and algorithms.
- Proper error handling and input validation.
- Efficient solutions with appropriate time/space complexity.
- Functional programming techniques.
- Object-oriented design principles.

---

## 🔍 Advanced Topics Covered

- List comprehensions and generator expressions.
- Functional programming with `map()`, `filter()`, and lambda functions.
- Dictionary and set operations for efficient lookups.
- Regular expressions for pattern matching.
- Recursion and memoization for optimization.
- Type hints for improved code clarity.

---

## 📚 Additional Resources

### Python Documentation
- [Python Official Documentation](https://docs.python.org/3/)
- [Python Standard Library](https://docs.python.org/3/library/index.html)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)

### Recommended Books
- "Python Crash Course" by Eric Matthes.
- "Fluent Python" by Luciano Ramalho.
- "Effective Python: 90 Specific Ways to Write Better Python" by Brett Slatkin.

### Online Learning
- [Real Python](https://realpython.com/)
- [Python Morsels](https://pythonmorsels.com/)
- [Talk Python To Me](https://talkpython.fm/) (Podcast).
- [Python Bytes](https://pythonbytes.fm/) (Podcast).

### Practice Platforms
- [Exercism Python Track](https://exercism.org/tracks/python)
- [LeetCode](https://leetcode.com/problemset/all/?difficulty=Easy&page=1&topicSlugs=python)
- [HackerRank Python Domain](https://www.hackerrank.com/domains/python)
- [Codewars](https://www.codewars.com/?language=python)
