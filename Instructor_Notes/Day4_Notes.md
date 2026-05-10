# 👨‍🏫 Instructor Lecture Notes: Day 4

## Topic 10: Introduction to Pandas (2 Hrs)
**1. What is Pandas?**
- Explain that Pandas is "Excel on steroids" built for Python. It is the industry standard for tabular data analysis.
- Based on NumPy (very fast, written in C).
**2. Series vs DataFrame:**
- **Series:** A single column of data with an index. (1-Dimensional).
- **DataFrame:** A table with rows and columns. Basically, a collection of Series glued together. (2-Dimensional).
**3. Loading Data:**
- Show how to import: `import pandas as pd`.
- *Live Code:* Create a DataFrame from a dictionary.
  ```python
  data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
  df = pd.DataFrame(data)
  ```
- Loading CSVs: Show `pd.read_csv("data.csv")`. Show `.head()` to preview the top 5 rows.

## Topic 11: Series & Data Frames Deep Dive (2 Hrs)
**1. Indexing & Selecting:**
- Grabbing a column: `df['Age']`.
- **`loc` vs `iloc`:**
  - `.iloc[]`: Integer Location. `df.iloc[0]` gets the very first row, regardless of its label.
  - `.loc[]`: Label Location. Looks for the actual name of the index row/column.
**2. Conditional Filtering:**
- Very important! Show how boolean masking works.
- *Live Code:* 
  - Step 1: `df['Age'] > 18` (Returns True/False for every row).
  - Step 2: `df[ df['Age'] > 18 ]` (Passes the True/False mask back into the dataframe to return only the True rows).
**3. Cleaning Data:**
- Dropping columns: `df.drop(columns=['Useless_Column'])`. Emphasize that operations in pandas do not modify the original dataframe unless you assign it (`df = df.drop...`) or use `inplace=True`.

## Topic 12: Grouping & Aggregating (2 Hrs)
**1. The Split-Apply-Combine Strategy:**
- Explain the logic: Grouping data *splits* it into buckets (e.g., buckets for each Department). We then *apply* a function (like mean salary) to each bucket, and *combine* it back into a new table.
**2. Groupby & Aggregate (`agg`):**
- *Live Code:* `df.groupby('Department')['Salary'].mean()`.
- Explain that the groupby object itself is lazy; nothing happens until you attach an aggregate function (`.sum()`, `.mean()`, `.count()`).
- Show `.agg(['mean', 'max'])` to apply multiple statistical functions at once.
**3. Describing Data:**
- Show `df.describe()`. It instantly calculates count, mean, standard dev, min, max, and quartiles for all numerical columns. It's the ultimate EDA (Exploratory Data Analysis) cheat code.
