# The Ultimate 7-Day Python & ML Cheatsheet

This document contains the absolute most important takeaways from all 19 topics covered in the master course.

## 1. Python Foundations
- **Variables & Data Types**: Use descriptive names (`user_age = 25`). Know your types: `int`, `float`, `str`, `bool`.
- **String Operations**: Strings are just lists of text characters. 
  - Use `len()`, `.upper()`, `.replace()`, and `.split()`. 
  - Slicing: `text[start:stop:step]`.
  - Formatting: ALWAYS use f-strings (`f"Hello {name}"`).
- **Input/Output**: `print()` displays data. `input()` gets data from the user, but ALWAYS returns a string. Remember to cast it if you need math: `int(input())`.
- **Loops**: 
  - Use `for` loops when you know exactly how many times to run (e.g., iterating through a list or using `range()`).
  - Use `while` loops when waiting for a specific condition to change. Don't forget to mathematically update the condition or you'll get an infinite loop!

## 2. Data Structures & File Handling
- **Lists `[]`**: Ordered, changeable. Great for storing multiple items. Use `.append()` to add, `.pop()` to remove.
- **Dictionaries `{}`**: Key-Value pairs. Extremely fast for looking up data by its label (e.g., `student["name"]`).
- **Tuples `()`**: Just like lists, but completely **locked and unchangeable** (Immutable). Use them for safe, permanent data.
- **File Handling**: ALWAYS use the `with open("file.txt", "w") as file:` block. It automatically closes the file for you safely. Use `"r"` to read, `"w"` to overwrite, and `"a"` to append.

## 3. Data Analysis with Pandas
- **Pandas**: Python's automated version of Excel. `import pandas as pd`.
- **DataFrames**: A 2D table of rows and columns. Load them easily using `pd.read_csv()`.
- **Exploration**: Use `.head()`, `.info()`, and `.describe()` to understand your data mathematically immediately.
- **Cleaning Data**: Machine Learning hates blanks! Always clean your data using `.dropna()` (delete row entirely) or `.fillna()` (safely replace the blank with an average).
- **Grouping**: Use `.groupby("Category")` just like an Excel Pivot Table to summarize massive amounts of data.
- **Merging**: Use `pd.merge()` to connect two different tables using a shared column (exactly like VLOOKUP).

## 4. Defensive Programming (Errors)
- **Syntax Errors**: Grammar mistakes (missing commas, quotes). The code won't run at all.
- **Runtime Errors**: Math or logic mistakes (dividing by zero). The code crashes while running.
- **Try / Except**: Wrap dangerous code in a `try` block. If it crashes, it safely falls into the `except` block instead of destroying the program.
- **Finally**: The `finally` block runs 100% of the time, no matter what. Perfect for closing database connections so data isn't corrupted.

## 5. Machine Learning & Regression
- **Correlation**: Use `.corr()` to mathematically prove if two variables relate to each other (1.0 = perfect positive match, -1.0 = perfect negative match).
- **Scikit-Learn**: The ultimate industry-standard ML library (`import sklearn`).
- **The Workflow**:
  1. Define Features (`X` inputs) and Target (`y` output).
  2. Use `train_test_split` to hide 20% of your data so the model can take a blind test later.
  3. `.fit(X_train, y_train)`: The computer learns the mathematical pattern.
  4. `.predict(X_test)`: The computer guesses the answers for the hidden test.
  5. **Mean Absolute Error (MAE)**: Measures exactly how many points the computer's guess was off by on average.
