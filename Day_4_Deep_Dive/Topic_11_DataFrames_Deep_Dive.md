# Topic 11: Series & Data Frames Deep Dive

## Selecting Columns
To extract a single column (which returns a Series) from a DataFrame, you pass the exact column name in square brackets:
- `df["Age"]`
To extract multiple columns (which returns a smaller DataFrame), you must pass a List of column names (using double square brackets):
- `df[["Name", "Age"]]`

## Indexing and Selecting Rows
Pandas uses special methods to grab specific rows out of the massive table:
- `iloc[]`: Index Location. Grabs rows based purely on their numerical position (zero-based).
  - Example: `df.iloc[0]` grabs the very first row. `df.iloc[0:5]` grabs the first five rows.
- `loc[]`: Location. Grabs rows based on specific labels or conditions.

## Filtering Data
You can filter a DataFrame to only show rows that meet a specific condition (exactly like adding a Filter in Excel).
- Step 1: Create a condition: `df["Age"] > 25` (This returns True/False for every row).
- Step 2: Pass the condition back into the DataFrame: `df[df["Age"] > 25]` (This returns the actual filtered table rows).

## Cleaning Data
Real-world data is extremely messy. It has missing blanks (called NaN in Pandas) and duplicate entries.
- `dropna()`: Completely deletes any row that has a missing value.
- `fillna(value)`: Safely replaces missing values with a specific value (like 0 or "Unknown").
- `drop_duplicates()`: Removes exact duplicate rows from the table so data is not counted twice.
- `rename(columns={"old_name": "new_name"})`: Safely changes the names of your columns.
