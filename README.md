# PS 17: Class Marks Analyzer

A simple Python program that reads marks for a class, validates the input, and computes summary statistics using NumPy.

---

## Overview

This project was built for a 1st-semester Python assignment. It accepts space-separated marks typed into the console, validates each score, converts the scores into a NumPy array, and calculates:

- **Mean**: Arithmetic average of the class marks.
- **Median**: Middle score of the dataset.
- **Highest & Lowest**: Maximum and minimum marks scored.
- **Standard Deviation**: Population standard deviation (`np.std`, `ddof=0`).
- **Pass & Fail Counts**: Number of students scoring at or above 40 (passing mark).
- **Pass Percentage**: Ratio of passed students to total students.
- **Above Average**: Number of students scoring strictly above the class mean.

---

## Requirements

- Python 3.8+
- [NumPy](https://numpy.org/)

---

## Setup & Running

1. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install numpy
   ```

3. **Run the program:**
   ```bash
   python marks_analyzer.py
   ```

---

## How It Works

The solution is contained in `marks_analyzer.py`:

- **`get_marks()`**: Prompts the user with `Marks: `, splits the input string by whitespace, and validates each value:
  - Ensures every entry is a valid number using `try/except ValueError`.
  - Confirms every number is between `0` and `100` (`if not (0 <= mark <= 100)`).
  - Handles empty input gracefully.
  - Returns a NumPy array of valid numbers.
- **`analyze_marks(marks)`**: Performs all calculations using NumPy functions (`np.mean`, `np.median`, `np.max`, `np.min`, `np.std`, `np.sum`).
- **`print_results(...)`**: Prints the calculated values in a neat, easy-to-read console layout.
- **`main()`**: Coordinates input validation, analysis, and display.

---

## Test Cases & Examples

### Test Case 1: Normal Input
```text
Marks: 40 50 60 70 80
Mean: 60.00 | Median: 60.00
Max: 80 | Min: 40 | Std Dev: 14.14
Passed: 5 of 5 | Failed: 0 | Pass percentage: 100.00%
Above average: 2 students
```

### Test Case 2: Boundary / Minimum Input (Single Student)
```text
Marks: 75
Mean: 75.00 | Median: 75.00
Max: 75 | Min: 75 | Std Dev: 0.00
Passed: 1 of 1 | Failed: 0 | Pass percentage: 100.00%
Above average: 0 students
```

### Test Case 3: Invalid Input Handling
- **Non-numeric entry:**
  ```text
  Marks: 50 abc 70
  Invalid marks 'abc'. Enter numbers only.
  ```
- **Out-of-range entry:**
  ```text
  Marks: 50 105 70
  Marks must be between 0 and 100.
  ```

### Test Case 4: Different Valid Scenario
```text
Marks: 25 50 75 100
Mean: 62.50 | Median: 62.50
Max: 100 | Min: 25 | Std Dev: 27.95
Passed: 3 of 4 | Failed: 1 | Pass percentage: 75.00%
Above average: 2 students
```

