# 👨‍🏫 Instructor Lecture Notes: Day 5

## Topic 13: Data Manipulation (2 Hrs)
**1. Concatenation vs Merging:**
- **Concatenation (`pd.concat`):** Stacking data blocks together. Either vertically (putting January's rows on top of February's rows) or horizontally (adding new columns side-by-side).
- **Merging (`pd.merge`):** Exactly like SQL Joins or Excel VLOOKUP. Connecting tables based on a common key (like `Employee_ID`).
- Explain Inner, Outer, Left, and Right merges conceptually.
**2. Handling Missing Values (NaN):**
- Real data is messy. `NaN` means "Not a Number" (null/blank).
- Checking for blanks: `df.isna().sum()`.
- **Strategy 1: Drop them.** `df.dropna()`. Good if you have millions of rows and only a few missing. Bad if you lose 50% of your data.
- **Strategy 2: Fill them.** `df.fillna(value)`. Show how to fill missing ages with the average age: `df['Age'].fillna(df['Age'].mean())`.

## Topic 14: Understanding Errors (2 Hrs)
**1. Syntax Errors vs Runtime Errors:**
- **Syntax Errors:** You broke the grammar rules of Python (missing colon, unclosed parenthesis). The code *never even starts running*.
- **Runtime Errors:** Grammar is fine, but an illegal operation happens during execution (e.g., trying to divide by zero, or accessing a file that doesn't exist).
**2. Debugging Basics:**
- Teach students **how to read a traceback**.
- Rule of thumb: Read the very *last line* first (it tells you the exact error type like `TypeError`). Then look for the filename and line number immediately above it.
- **Print Debugging:** Show how adding `print("Made it to step 2")` can help isolate where the code silently fails.

## Topic 15: Exceptions in Python (2 Hrs)
**1. What are Exceptions?**
- When a runtime error occurs, Python creates an "Exception Object" and throws it. If nothing catches it, the program crashes violently.
**2. Built-in Exceptions:**
- Familiarize them with: `ValueError` (right type, wrong value like `int("apple")`), `TypeError` (adding string to int), `IndexError` (list out of bounds), `KeyError` (dict key missing).
**3. Raising Exceptions:**
- Why would we want to trigger an error on purpose? To enforce rules!
- *Live Code:*
  ```python
  def withdraw(balance, amount):
      if amount > balance:
          raise ValueError("Insufficient funds!")
  ```
- Explain that raising an error is safer than returning a silent failure like `-1`, which another developer might not notice.
