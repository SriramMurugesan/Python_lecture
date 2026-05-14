# Topic 10: Introduction to Pandas (2-Hour Deep Dive)

Welcome to Day 4! If Python is the engine of Data Science, Pandas is the steering wheel. This 2-hour session is tightly aligned with the **IBM Data Science Professional Certificate**, focusing on the exact fundamentals you need to pass their technical assessments. 

We will be using a realistic `student_marks.csv` file to simulate a real-world analytics task.

---

## Part 1: The Core Architecture of Pandas

### Series vs. DataFrames
Pandas is built on two primary data structures. You must understand the difference to pass certification exams.
- **Series:** A one-dimensional array. Think of it as a single column of data. It has an index (row labels) and a set of values.
- **DataFrame:** A two-dimensional table. Think of it as an Excel spreadsheet. It is literally just a collection of `Series` glued together, sharing the same index.

### Importing Data
The gateway to all data analysis in Python is `pd.read_csv()`. 
In the real world, datasets aren't always perfect. Sometimes you'll need to specify parameters like `sep=';'` if the file isn't comma-separated, or `encoding='utf-8'` if there are weird characters. For our student dataset, a standard import will work.

---

## Part 2: High-Level Exploration 

Before you ever try to clean or model data, you *must* explore it. IBM tests heavily on your ability to quickly understand a dataset's structure and constraints.

### The Inspection Tools
Once you load a DataFrame (e.g., `df`), you should immediately run these four commands:
1. **`df.head()` / `df.tail()`:** Views the first or last 5 rows. Look for obvious formatting issues.
2. **`df.shape`:** Returns a tuple `(rows, columns)`. Are there as many rows as you expected?
3. **`df.info()`:** The most important method! It tells you how many non-null values exist in each column, the data type of each column (`int64`, `float64`, `object`), and the memory usage. 
4. **`df.describe()`:** Generates descriptive statistics (mean, min, max, standard deviation) for all numerical columns instantly.

### Understanding `dtypes` (Data Types)
In Pandas, strings are called `object`. Integers are `int64`, and decimals are `float64`. If you see a column that *should* be numbers (like 'Score') but it shows up as `object` in `df.info()`, it means there's a hidden string or bad character in that column ruining the math.

---

## Part 3: Subsetting and Selection (The Tricky Part)

Extracting specific rows and columns is where most beginners fail. You must master the difference between `.loc` and `.iloc`.

### Label-Based vs. Index-Based Selection
- **`.iloc[]` (Integer Location):** This is purely based on the physical position. `df.iloc[0, 1]` gets the item in the 1st row, 2nd column. It acts exactly like standard Python list slicing.
- **`.loc[]` (Location):** This is label-based. You look up data using the actual names of the rows and columns. `df.loc[0, 'Name']` gets the 'Name' of the student at index label 0.

*Certification Tip:* If you sort a DataFrame and the index gets shuffled (e.g., 5, 2, 9), `iloc[0]` still gets the very first row physically visible, while `loc[0]` searches for the specific row labeled '0', wherever it ended up!
