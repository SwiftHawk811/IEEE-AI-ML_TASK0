# IEEE-AI-ML_TASK0

This repository contains the completed solutions for **Task 0 (Python Fundamentals, Data Analysis & Git)** of the IEEE AI/ML track. All data handling, numeric computations, and visualizations were implemented independently.

**Author:** Angad Saha

---

## 📁 Repository Structure

```text
task-0/
├── data/
│   ├── student_performance.csv             # Raw input dataset
│   └── processed_student_performance.csv   # Cleaned & processed dataset (Pandas output)
├── plots/
│   ├── final_scores.png                    # Student names vs final scores bar chart
│   ├── study_vs_score.png                  # Hours studied vs final score scatter plot
│   ├── score_distribution.png              # Distribution of final scores histogram
│   └── attendance_vs_deterioration.png     # Custom plot analyzing an extra data trend
├── q1.py                                   # List Analyzer (Manual stats algorithm)
├── q2.py                                   # Lists, Functions, and .copy() operations
├── q3.py                                   # Prime Numbers using for-else loops
├── q4.py                                   # NumPy Basics & Vectorized operations
├── q5.py                                   # Pandas Data Analysis & CSV processing
├── q6.py                                   # Data Visualization with Matplotlib
└── README.md
```

---

## 🛠️ Prerequisites & Installation

To run the pipeline or execute separate task files locally, make sure you have Python 3 and the required numerical computing packages installed. Use [pip](https://pypa.io) to install them:

```bash
pip install numpy pandas matplotlib
```

---

## 📜 Script Reference & Usage

### 🔹 `q1.py` — List Analyzer
* **Description:** Accepts user-input integers as '1 2 3 4 5' to find basic metrics (Min, Max, Sum, Evens, Odds, Reversed) without the use of built-in math shortcuts like `max()`, `min()`, or `sort()`.
* **Execution:** `python q1.py`

### 🔹 `q2.py` — List Copying & Methods
* **Description:** Creating a function evaluating mutable array behavior using `.copy()`. It removes all negative numbers, adds one 0, and returns a sorted, modified array without altering the source array. Takes input of form "int int int ... int"
* **Execution:** `python q2.py`

### 🔹 `q3.py` — Prime Number Finder (For-Else Syntax)
* **Description:** Prompts for a integer $N$ and filters out all primes in the inclusive range $[2, N]$ via standard tests. For-else algorithm is known but not used explicitly for optimizing solution.
* **Execution:** `python q3.py`

### 🔹 `q4.py` — NumPy Basics
* **Description:** Explores multidimensional structures and vector operations on array-extracted columns (shapes, data types, standard deviations, and indexing filters matching values over threshold marks) without loop reliance.
* **Execution:** `python q4.py`

### 🔹 `q5.py` — Pandas Data Analysis
* **Description:** Reads tabular data from `student_performance.csv`, runs query profiles (null audits, top scorer discovery, logical subsetting by attendance rules), updates standard metrics with computed columns, and structures the changes to output `processed_student_performance.csv`.
* **Execution:** `python q5.py`

### 🔹 `q6.py` — Matplotlib Data Visualization
* **Description:** Consumes the pipeline modifications generated inside `q5.py` to draft clear data figures. Saves individual visual plots to the `plots/` folder (`final_scores.png`, `study_vs_score.png`, `score_distribution.png`, and a custom-crafted pattern analysis trend).
* **Execution:** `python q6.py`
