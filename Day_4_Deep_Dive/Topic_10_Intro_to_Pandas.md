# Topic 10: Introduction to Pandas

## What is Pandas?
Pandas is a powerful, external Python library used for Data Analysis. If Python is the engine of a car, Pandas is like having the ultimate, automated version of Excel built directly into your programming environment.

## Importing Pandas
Because Pandas is an external library, we must install it (using `pip install pandas` in the terminal) and import it into our script before we can use it.
- `import pandas as pd` (We use 'pd' as a shortcut so we don't have to type 'pandas' over and over again).

## Series vs. DataFrame
Pandas has two main data structures you must understand:
1. **Series**: A single column of data. Think of it as a 1-Dimensional list with labels (indexes) next to each item.
2. **DataFrame**: A 2-Dimensional table of data, made up of multiple Series glued together. This is your standard spreadsheet with rows and columns.

## Loading Data
The most common way to load data into Pandas is from a CSV (Comma Separated Values) file.
- `pd.read_csv("filename.csv")`: Reads a CSV file from your computer and converts it directly into a Pandas DataFrame table.

## Basic Data Exploration
Once your data is loaded, you need to understand what it looks like before you analyze it. Pandas provides built-in methods for this:
- `head()`: Shows the first 5 rows of the table.
- `tail()`: Shows the last 5 rows of the table.
- `info()`: Gives a summary of the columns, data types, and shows if any data is missing.
- `describe()`: Automatically calculates math statistics (average, minimum, maximum) for all number columns.
- `shape`: A property (not a method, so no parentheses!) that tells you the total dimensions: (Rows, Columns).
