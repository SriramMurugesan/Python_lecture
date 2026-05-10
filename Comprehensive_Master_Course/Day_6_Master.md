# 📘 Day 6: Advanced Control Flow & Statistics (6 Hours)
*(Note: ML section instruction — Focus on intuition, avoid heavy math).*

## 🕒 Topic 16: Try/Except/Finally + Custom Exceptions (3 Hours)
### 🎯 Learning Outcome
Implement defensive programming paradigms and custom error handling architectures.

### 🌍 Real Problem
Your script connects to a secure database, runs a query, and then closes the connection. If the query throws an error midway, the script jumps to the `except` block, and the connection is *never* closed, leaving a security vulnerability.

### 🧠 Concept Explanation
* **Multiple Except Blocks:** Handling different types of failures with specific responses.
* **`finally` Block:** Guaranteed execution. It runs regardless of whether the `try` succeeded or failed. Critical for cleanup operations (closing files, releasing network ports).
* **Custom Exception Classes:** Inheriting from Python's base `Exception` to create incredibly specific, business-logic errors (e.g., `InsufficientFundsError`).

### 💻 Live Code Example
```python
class InsufficientFundsError(Exception):
    pass

def transfer(bal, amt):
    if amt > bal:
        raise InsufficientFundsError("Not enough money.")
    return bal - amt

try:
    transfer(100, 200)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
finally:
    print("Database connection successfully closed.")
```

### 🐞 Debugging Requirement
**Broken Code:**
```python
try:
    f = open("file.txt", "r")
    print(1 / 0)
except ValueError:
    print("Math error")
    f.close()
```
**Task:** Identify the memory leak.
**Errors Explained:** `ZeroDivisionError` occurs, bypassing the `ValueError` block. The program crashes, and `f.close()` is never reached. `f.close()` must be inside a `finally` block or handled via a `with` statement.

### ⚠️ Common Mistakes
* **Mistake:** Putting too much non-risky code inside the `try` block.
* **Why it occurs:** Laziness. Only the exact lines that could fail should be wrapped in `try` to prevent masking unrelated bugs.

### 📝 Practice Requirements
**Easy (3):**
1. Write a `try/except/finally` block where the `finally` block prints "Cleanup complete".
2. Catch `TypeError` and `ValueError` in two separate explicit `except` blocks.
3. Define an empty custom exception class named `NetworkTimeoutError`.
**Medium (3):**
1. Use an `else` block in conjunction with `try/except`.
2. Raise your custom exception with a highly specific, formatted error message.
3. Ensure a dummy file variable is securely closed in a `finally` block.
**Challenging (2):**
1. Create an API request simulator that randomly fails, raises a custom `NetworkError`, and implements an exponential backoff retry loop.
2. Build a custom `ValidationException` that actually stores the specific string field that failed validation as an attribute inside the exception object.

---

## 🕒 Topic 17: Regression & Correlation Concepts (3 Hours)
### 🎯 Learning Outcome
Understand the statistical foundations and relationships underpinning regression-based Machine Learning.

### 🌍 Real Problem
The marketing team spends millions on Facebook Ads and TV Ads. They want to know: *Does spending more on TV actually correlate to higher product sales?* 

### 🧠 Concept Explanation *(Intuition-Focus)*
* **Correlation (-1 to 1):** 
  * `1` = Perfect positive (Ads go up, Sales go up).
  * `-1` = Perfect negative (Price goes up, Sales go down).
  * `0` = Completely random, no relationship.
* **Correlation Matrix:** A grid showing how every variable interacts with every other variable.
* **Causation vs Correlation:** Just because Ice Cream sales and Shark Attacks are highly correlated does not mean ice cream attracts sharks. (Hidden variable: Summer).
* **Regression Theory:** Drawing the "Line of Best Fit" through a scatter plot of data. It calculates the line that minimizes the total distance (residuals) to all the dots.

### 💻 Live Code Example
```python
import pandas as pd
df = pd.DataFrame({'Ads': [100, 200, 300], 'Sales': [150, 250, 350]})
corr = df.corr()
print("Correlation Matrix:\n", corr)
```

### 🐞 Debugging Requirement
**Broken Code:**
```python
df = pd.DataFrame({'Region': ["North", "South"], 'Sales': [100, 200]})
print(df.corr())
```
**Task:** Why doesn't the matrix compute properly?
**Errors Explained:** Correlation mathematically requires numeric data. Trying to compute correlation on string categories (`"North"`) will fail or silently drop the column.

### ⚠️ Common Mistakes
* **Mistake:** Assuming a high correlation automatically means one variable is controlling the other.
* **Why it occurs:** Human psychology looks for patterns and assumes direct causation, ignoring outside confounding variables.

### 📝 Practice Requirements
**Easy (3):**
1. Compute the correlation between two simple numeric lists in Pandas.
2. Identify positive versus negative correlation conceptually from real-world examples.
3. Generate a full correlation matrix on a dummy dataset.
**Medium (3):**
1. Filter out correlations below 0.5 in a Pandas matrix to isolate strong relationships.
2. Plot a scatter plot of two highly correlated variables (using matplotlib or seaborn if available).
3. Identify and document a scenario where correlation exists but causation does absolutely not.
**Challenging (2):**
1. Handle missing values appropriately before computing a correlation matrix.
2. Convert a categorical column to numeric (Dummy variables / One-Hot Encoding) so it can be included in a correlation matrix.
