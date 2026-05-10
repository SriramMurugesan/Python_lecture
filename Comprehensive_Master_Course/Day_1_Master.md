# 📘 Day 1: Foundations & Setup (6 Hours)

## 🕒 Topic 1: Introduction to Python & Git Workflow (2 Hours)
### 🎯 Learning Outcome
Understand Python’s purpose, features, real-world usage, and master basic Git version control workflow (`init`, `add`, `commit`, `push`, `clone`).

### 🌍 Real Problem
Imagine a team of 5 developers building an application. Without version control, they overwrite each other's work. Without Python, writing the backend would take weeks instead of days. We need a readable language and a safe way to track code changes.

### 🧠 Concept Explanation
* **What is Python?** A high-level, interpreted language focusing on readability.
* **Features:** Dynamically typed, massive library ecosystem, cross-platform.
* **Applications:** Web Dev, AI/Machine Learning, Data Science, Automation.
* **Git Workflow:** `git init` (starts tracking), `git add .` (stages changes), `git commit -m` (saves snapshot), `git push` (uploads), `git clone` (downloads).

### 💻 Live Code Example
```bash
git init
git add .
git commit -m "Initial commit of Python project"
```
```python
print("Welcome to the Python Development Team!")
```

### 🐞 Debugging Requirement
**Broken Code:**
```bash
git commit "Added new feature"
```
**Task:** Ask students why this Git command fails.
**Errors Explained:** Git requires the `-m` flag to identify the string as a message. Otherwise, it thinks the string is a file path.

### ⚠️ Common Mistakes
* **Mistake:** Forgetting to run `git add .` before `git commit`.
* **Why it occurs:** Beginners assume `commit` automatically saves everything. Git separates staging from committing.

### 📝 Practice Requirements
**Easy (3):**
1. Create a GitHub account.
2. Initialize a local Git repository in a new folder.
3. Write a Python script that prints three real-world applications of Python.
**Medium (3):**
1. Create a `.txt` file, add it to Git, and commit with a message.
2. Modify the file, check `git status`, and commit the changes.
3. Clone an open-source Python repository from GitHub.
**Challenging (2):**
1. Create a new repository on GitHub and push your local commits.
2. Write a `.gitignore` file that ignores a specific folder, then verify Git ignores it.

---

## 🕒 Topic 2: Python Installation & Setup (2 Hours)
### 🎯 Learning Outcome
Set up the Python environment, execute programs, and adopt a problem-solving mindset.

### 🌍 Real Problem
Writing code in Notepad is incredibly inefficient and error-prone. Developers need smart tools (IDEs) to highlight syntax and catch errors early.

### 🧠 Concept Explanation
* **Installation:** Downloading Python, adding it to PATH.
* **IDEs:** VS Code (for scripts/apps) vs Jupyter Notebook (for data science blocks).
* **Problem Solving:** Break down -> Pseudocode -> Write Code.

### 💻 Live Code Example
```python
# script.py
def solve_problem(steps):
    print(f"Executing step: {steps}")
solve_problem("1. Understand 2. Pseudocode 3. Code")
```

### 🐞 Debugging Requirement
**Broken Code:**
```bash
# In terminal
python script
```
**Task:** Ask students why the terminal throws an error.
**Errors Explained:** The interpreter needs the exact file extension (`.py`) to locate and execute the file.

### ⚠️ Common Mistakes
* **Mistake:** Forgetting to check "Add Python to PATH" on Windows during installation.
* **Why it occurs:** Users skip through installation wizards. Without PATH, the terminal doesn't know what the word `python` means.

### 📝 Practice Requirements
**Easy (3):**
1. Install Python and verify the version in the terminal.
2. Install VS Code.
3. Install Jupyter Notebook via pip.
**Medium (3):**
1. Write a script that prints your name and run it via the terminal.
2. Open Jupyter, write a print statement in a cell, and execute it.
3. Write structured pseudocode for the process of making coffee.
**Challenging (2):**
1. Set up an isolated Python virtual environment (`venv`).
2. Install an external package (like `requests`) into that environment.

---

## 🕒 Topic 3: Variables, Data Types & Operators (2 Hours)
### 🎯 Learning Outcome
Write basic Python programs using variables, core data types, and mathematical/logical operators.

### 🌍 Real Problem
A banking app needs to store a user's balance, name, and account status in memory to process a transaction. 

### 🧠 Concept Explanation
* **Variables:** Named boxes in memory.
* **Data Types:** `int` (whole numbers), `float` (decimals), `bool` (True/False), `str` (text).
* **Operators:** Arithmetic (`+`, `-`, `*`, `/`, `//`, `%`), Logical (`and`, `or`, `not`).
* **Type Casting:** Converting one type to another using `int()`, `str()`.

### 💻 Live Code Example
```python
age = 25
balance = 100.50
is_active = True
print(age + 5)
print(balance > 50 and is_active)
```

### 🐞 Debugging Requirement
**Broken Code:**
```python
total = "10" + 5
print(total)
```
**Task:** Ask students to debug the crash.
**Errors Explained:** `TypeError`. Python refuses to implicitly add text to numbers. You must cast it: `int("10") + 5`.

### ⚠️ Common Mistakes
* **Mistake:** Naming variables with spaces (`user age = 25`).
* **Why it occurs:** Beginners treat code like English essays. Variables must use underscores (`user_age = 25`).

### 📝 Practice Requirements
**Easy (3):**
1. Assign your age to a variable and print it.
2. Create and add two float variables.
3. Convert a boolean `True` to an integer.
**Medium (3):**
1. Calculate the area of a rectangle given length and width variables.
2. Write a program to swap the values of two variables.
3. Convert the string `"150"` to a float and add `50.5`.
**Challenging (2):**
1. Calculate compound interest based on hardcoded principal, rate, and time.
2. Check if a number is even without using the `%` (modulo) operator (use division logic).
