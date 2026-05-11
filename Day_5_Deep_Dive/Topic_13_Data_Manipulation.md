# Topic 13: Data Manipulation in Pandas

## Why Manipulate Data?
In the real world, your data will almost never be in one perfect file. You might have customer names in one file, and their purchases in another. Data Manipulation is the process of combining and preparing these scattered datasets so they are clean and ready for Data Analysis or Machine Learning models.

## Merging Datasets (VLOOKUP / SQL JOIN)
`pd.merge()` allows you to combine two DataFrames together based on a common column (a shared key). This is exactly like doing a VLOOKUP in Excel.
- If Table A has "Employee_ID" and Table B has "Employee_ID", you can merge them together perfectly side-by-side!
- Syntax: `pd.merge(table_a, table_b, on="Employee_ID")`

## Concatenation (Stacking)
`pd.concat()` is used to stack entire DataFrames together.
- Stacking Vertically (Rows): If you have a file for "January Sales" and another for "February Sales", you can stack them straight on top of each other to make one giant master table.

## Handling Missing Values (For Machine Learning)
Before sending data to a Machine Learning model, you absolutely CANNOT have missing blanks (`NaN` or Not a Number). Machine Learning models only understand complete numbers.
- `dropna()`: Deletes the entire row. Use this if you have millions of rows of data and losing a few won't hurt your analysis.
- `fillna()`: Fills the blanks. A very common and advanced ML strategy is to fill a missing number with the **Average (Mean)** of that specific column. This ensures the fake data doesn't skew or ruin your mathematical analysis!
