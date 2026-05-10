# 📘 Day 5: Advanced Data & Error Handling (6 Hours)

## 🕒 Topic 13: Data Manipulation (2 Hours)
### 🎯 Learning Outcome
Prepare and clean datasets for analytical and Machine Learning workflows by merging tables and handling nulls.

### 🌍 Real Problem
In real businesses, data is never stored in one place. Customer details are in Table A, and their Purchase History is in Table B. Furthermore, some users left fields blank (missing data). We must join the tables and deal with the blanks before analyzing.

### 🧠 Concept Explanation
* **Concatenation (`pd.concat`):** Stacking data blocks vertically (more rows) or horizontally (more columns).
* **Merging (`pd.merge`):** Joining on a common ID (Inner, Outer, Left, Right). Equivalent to SQL JOIN.
* **Missing Values (NaN):** Checking (`isna()`), Dropping (`dropna()`), or Filling (`fillna()`).

### 💻 Live Code Example
```python
import pandas as pd
import numpy as np
df1 = pd.DataFrame({'ID': [1,2], 'Val': [10, np.nan]})
df2 = pd.DataFrame({'ID': [2,3], 'Score': [90, 80]})

merged = pd.merge(df1, df2, on='ID', how='outer')
cleaned = merged.fillna(0)
print(cleaned)
```

### 🐞 Debugging Requirement
**Broken Code:**
```python
df = pd.DataFrame({'A': [1, None, 3]})
df.dropna()
print(df)
```
**Task:** Why are the missing values still printed?
**Errors Explained:** Pandas operations are not in-place by default to protect data. You must overwrite the variable: `df = df.dropna()` or explicitly state `df.dropna(inplace=True)`.

### ⚠️ Common Mistakes
* **Mistake:** Dropping all NaNs blindly using `dropna()`.
* **Why it occurs:** Beginners want a clean dataset quickly, but dropping any row with a single NaN might result in destroying 80% of perfectly good data in other columns.

### 📝 Practice Requirements
**Easy (3):**
1. Concatenate two small DataFrames vertically.
2. Check for the sum of missing values in a DataFrame.
3. Drop all rows containing missing values and save the result.
**Medium (3):**
1. Perform an inner merge on two DataFrames sharing a common ID.
2. Perform a left merge.
3. Fill missing values intelligently using the mean average of the column.
**Challenging (2):**
1. Perform a complex merge resolving duplicate column names using the `suffixes` argument.
2. Interpolate missing time-series data using Pandas `.interpolate()`.

---

## 🕒 Topic 14: Understanding Errors (2 Hours)
### 🎯 Learning Outcome
Identify, differentiate, and correct Syntax versus Runtime errors while adopting a debugging mindset.

### 🌍 Real Problem
You write a 500-line script. When you run it, the terminal spits out a massive wall of angry red text. Without a debugging mindset, you will stare at the screen blankly. You need to know how to trace the problem.

### 🧠 Concept Explanation
* **Syntax Errors:** Bad grammar (missing colon, unclosed bracket). The code physically cannot start running.
* **Runtime Errors:** Perfect grammar, but an illegal mathematical or logic operation occurs while the code is actively running (e.g., dividing by zero).
* **Tracebacks:** Read the error message from the *bottom up*. The last line tells you exactly what went wrong.
* **Print Debugging:** Placing `print()` statements to track variable states just before a crash.

### 💻 Live Code Example
```python
def divide_amounts(a, b):
    print(f"[DEBUG] Attempting to divide {a} by {b}")
    return a / b
```

### 🐞 Debugging Requirement
**Broken Code:**
```python
for i in range(5)
    print(i)
```
**Task:** Identify the error type.
**Errors Explained:** `SyntaxError`. A colon `:` is required at the end of the `for` statement definition. Python's parser fails immediately.

### ⚠️ Common Mistakes
* **Mistake:** Changing random parts of the code hoping it fixes the error.
* **Why it occurs:** Panic. Developers must isolate the exact line causing the issue rather than guessing.

### 📝 Practice Requirements
**Easy (3):**
1. Fix a provided script with a missing parenthesis error.
2. Fix a provided script with an indentation error (`IndentationError`).
3. Read a complex stack trace and write down the exact file and line number of failure.
**Medium (3):**
1. Debug a function that accidentally returns `None` instead of appending to a list.
2. Use `print()` statements to trace variable changes inside a complex loop to find a logic bug.
3. Fix a `NameError` caused by local versus global variable scope.
**Challenging (2):**
1. Set up breakpoints in VS Code and step through a recursive function visually.
2. Identify and fix a silent logical error (e.g., using integer division `//` when standard division `/` was expected for financial math).

---

## 🕒 Topic 15: Exceptions in Python (2 Hours)
### 🎯 Learning Outcome
Write robust, crash-proof programs that gracefully handle runtime errors.

### 🌍 Real Problem
You ask the user to input their age. The user types "Twenty". Python tries to run `int("Twenty")`, violently crashes, and closes the entire application.

### 🧠 Concept Explanation
* **Exceptions:** When a runtime error occurs, Python "throws" an exception object.
* **`try / except`:** The safety net. Code inside `try` runs; if it throws an error, the `except` block catches it preventing a crash.
* **Built-in Exceptions:** `ValueError`, `TypeError`, `ZeroDivisionError`, `KeyError`.
* **Raising Exceptions:** Using `raise ValueError("Message")` to manually trigger an error when a business rule is violated.

### 💻 Live Code Example
```python
try:
    age = int(input("Enter age: "))
except ValueError:
    print("Invalid input! Please enter numbers only.")

def withdraw(amount):
    if amount < 0:
        raise ValueError("Cannot withdraw a negative amount!")
```

### 🐞 Debugging Requirement
**Broken Code:**
```python
try:
    x = 10 / 0
except ValueError:
    print("Error caught!")
```
**Task:** The script crashes anyway. Why?
**Errors Explained:** The math creates a `ZeroDivisionError`, but the `except` block is explicitly only looking for a `ValueError`. The unhandled error crashes the program.

### ⚠️ Common Mistakes
* **Mistake:** Using a "bare" `except:` clause with no specific error type.
* **Why it occurs:** It's lazy. But a bare `except` catches *everything*, including `KeyboardInterrupt` (when a user presses Ctrl+C to force quit), trapping the user in the program.

### 📝 Practice Requirements
**Easy (3):**
1. Write a block to safely catch a `ZeroDivisionError`.
2. Safely catch a `ValueError` during a string-to-integer conversion.
3. Raise a generic `Exception` manually with a custom message.
**Medium (3):**
1. Catch an `IndexError` gracefully when accessing a list out of bounds.
2. Write a function that raises an error if the user's input is a negative number.
3. Safely catch a `KeyError` in dictionary access.
**Challenging (2):**
1. Implement a retry mechanism using a `while` loop that keeps asking for input until a valid integer is provided without crashing.
2. Catch multiple distinct exceptions in a single `try` block and respond differently to each.
