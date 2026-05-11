# Topic 12: Grouping & Aggregating

## What is Grouping?
Grouping data in Pandas is the exact equivalent of creating a Pivot Table in Excel. It allows you to group identical categories together and calculate math on them instantly (like finding the total sales per region, or average age per city).

## The groupby() Method
The `groupby(column_name)` method splits your entire table into distinct, isolated groups based on a specific column.
- Example: `df.groupby("Department")` will group all the Sales people together, all the IT people together, etc.

## Aggregation Functions
Once you group your data, you must tell Pandas what math to do with the groups. These math actions are called aggregations:
- `sum()`: Adds all the numbers up.
- `mean()`: Calculates the average.
- `count()`: Counts how many rows exist in that specific group.
- `max()` / `min()`: Finds the highest or lowest value in that group.

Example: `df.groupby("Department")["Salary"].mean()` calculates the average salary per department.

## Multiple Aggregations with agg()
If you want to calculate the sum AND the average at the exact same time, you use the `.agg()` method and pass it a list of strings representing the math you want.
- Example: `df.groupby("Department")["Salary"].agg(["sum", "mean"])`

## The apply() Method
The `apply()` method allows you to run a built-in Python function across an entire column instantly, without writing a loop. 
For example, using `apply(len)` on a text column will instantly calculate the character length of every single row in that column.

## Describing Data (Grouped)
Just like you can `describe()` a whole DataFrame, you can `describe()` a grouped object to get a massive, instant mathematical summary of every single group individually!
