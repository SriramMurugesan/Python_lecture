# 📘 Day 4: Data Science Foundations - Pandas (6 Hours)
*(Note: Pandas strict requirement — Use real datasets and perform loading, cleaning, filtering, grouping, merging).*

## 🕒 Topic 10: Introduction to Pandas (2 Hours)
### 🎯 Learning Outcome
Import the library, understand the core structures (Series vs DataFrame), and load tabular data.

### 🌍 Real Problem
Excel is great, but it violently crashes if you try to open a 5-million-row CSV file. Python's Pandas library handles millions of rows easily because it processes data programmatically in memory.

### 🧠 Concept Explanation
* **Pandas:** Built on NumPy for extreme speed.
* **Series:** A 1-Dimensional array (essentially a single column) with an index.
* **DataFrame:** A 2-Dimensional table (rows and columns). A collection of Series.
* **Loading Data:** `pd.read_csv()` to import external real datasets.

### 💻 Live Code Example
```python
import pandas as pd
# Creating from scratch
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
print(df.head())
# Real world:
# df = pd.read_csv("real_sales_data.csv")
```

### 🐞 Debugging Requirement
**Broken Code:**
```python
import pandas as pd
df = pd.DataFrame([1, 2, 3], ["A", "B", "C"])
print(df.head)
```
**Task:** Why doesn't the table print properly?
**Errors Explained:** `.head` is a method, not a property. Without the parentheses `()`, Python prints the memory address of the function instead of executing it.

### ⚠️ Common Mistakes
* **Mistake:** Forgetting to run `import pandas as pd` at the top of the file.
* **Why it occurs:** Believing Pandas is built into Python natively. It is a third-party library.

### 📝 Practice Requirements
**Easy (3):**
1. Import pandas successfully.
2. Create a Pandas Series from a standard Python list.
3. Create a DataFrame from a dictionary.
**Medium (3):**
1. Load a real CSV file into a DataFrame.
2. Print the first 5 rows and the last 5 rows of the DataFrame.
3. Check the `.shape` and `.columns` of the DataFrame.
**Challenging (2):**
1. Create a DataFrame from a complex list of nested dictionaries.
2. Write a modified DataFrame back to a new CSV file without writing the index column.

---

## 🕒 Topic 11: Series & DataFrames Deep Dive (2 Hours)
### 🎯 Learning Outcome
Transform datasets by indexing, conditionally filtering, and cleaning columns.

### 🌍 Real Problem
A database dump contains thousands of users. You only want to email users who are over 18, live in "NY", and have an active subscription. You need to slice and filter the DataFrame efficiently.

### 🧠 Concept Explanation
* **Indexing:** `df['ColumnName']` grabs a Series.
* **`loc` vs `iloc`:** `iloc` uses integer positions (row 0). `loc` uses label names.
* **Conditional Filtering:** Creating boolean masks (`df['Age'] > 18`) and applying them.
* **Cleaning:** `df.drop(columns=['BadCol'])`.

### 💻 Live Code Example
```python
adults = df[df['Age'] >= 18]
specific_user = df.loc[0, 'Name']
cleaned_df = df.drop(columns=['UnnecessaryCol'])
```

### 🐞 Debugging Requirement
**Broken Code:**
```python
df = pd.DataFrame({'A': [1,2], 'B': [3,4]})
df['A'] == 1
```
**Task:** The DataFrame does not change. Why?
**Errors Explained:** The condition `df['A'] == 1` merely generates a boolean True/False Series in memory and discards it. To actually filter the data, you must pass the mask back into the brackets: `df = df[ df['A'] == 1 ]`.

### ⚠️ Common Mistakes
* **Mistake:** Encountering `SettingWithCopyWarning`.
* **Why it occurs:** Trying to modify a slice of a dataframe without explicitly using `.copy()`, making Pandas unsure if you want to modify the original table or just the slice.

### 📝 Practice Requirements
**Easy (3):**
1. Select a single column from a DataFrame and print it.
2. Select three columns simultaneously.
3. Use `iloc` to extract the very first row.
**Medium (3):**
1. Filter a DataFrame based on a single condition (e.g., Age > 30).
2. Filter a DataFrame using multiple complex conditions (using `&` or `|`).
3. Drop a specific row completely by its index.
**Challenging (2):**
1. Update the values of a column conditionally (e.g., increase salary by 10% IF department is IT).
2. Fix a `SettingWithCopyWarning` by properly isolating a DataFrame subset.

---

## 🕒 Topic 12: Grouping & Aggregating (2 Hours)
### 🎯 Learning Outcome
Analyze patterns in massive datasets using advanced grouping and statistical aggregations.

### 🌍 Real Problem
You have a table of 10,000 sales transactions across 4 regions. You need to present the average revenue, total items sold, and maximum sale price grouped by Region to the CEO.

### 🧠 Concept Explanation
* **Split-Apply-Combine:** The core logic of `.groupby()`.
* **`groupby()`:** Groups identical data into buckets.
* **`agg()`:** Applies statistical functions (mean, sum, max) to those buckets.
* **`describe()`:** Instantly generates statistical profiles of numeric columns.

### 💻 Live Code Example
```python
import pandas as pd
df = pd.DataFrame({'Dept': ['IT', 'HR', 'IT'], 'Salary': [60, 50, 70]})
avg_salary = df.groupby('Dept')['Salary'].mean()
print(avg_salary)
print(df.describe())
```

### 🐞 Debugging Requirement
**Broken Code:**
```python
grouped = df.groupby('Dept')
print(grouped)
```
**Task:** Why doesn't this print the table grouped by department?
**Errors Explained:** The `groupby` object is lazy. It creates the buckets in memory but does nothing until you apply an aggregate function like `.sum()` or `.mean()`.

### ⚠️ Common Mistakes
* **Mistake:** Grouping without specifying a target column.
* **Why it occurs:** `df.groupby('Dept').mean()` attempts to calculate the mean for EVERY other column in the dataset, which crashes if some columns contain strings.

### 📝 Practice Requirements
**Easy (3):**
1. Use `describe()` on a numerical DataFrame.
2. Group data by a categorical column and count the number of rows in each group.
3. Find the maximum value in each group.
**Medium (3):**
1. Group by two columns simultaneously and find the sum.
2. Use `.agg()` to apply multiple distinct functions (mean, sum) to a group at once.
3. Use `.apply()` to apply a custom mathematical function to a column.
**Challenging (2):**
1. Group data by date and calculate a 7-day rolling average.
2. Create a complex Pivot Table summarizing sales categorized by region and product line.
