# Topic 12: Grouping & Aggregating Data (2-Hour Lab)

Now that our data is clean, it's time to find insights. The IBM certification expects you to be able to answer business questions using the **Split-Apply-Combine** methodology. In this 2-hour lab, we will break down our dataset by Class and Subject to find the hidden patterns.

---

## Part 1: The `groupby` Engine (Split)

The `groupby()` function is the most powerful tool in Pandas for data analysis. It allows you to group rows that share the same value in a specific column.

### Single Grouping
If we want to know the average score per Subject, we split the data by 'Subject':
`df.groupby('Subject')`
*Note:* If you run just this, Pandas returns a `<DataFrameGroupBy object>`. It has split the data into invisible buckets, but it's waiting for you to tell it what math to perform!

### Applying the Math
To see the results, attach a mathematical function:
`df.groupby('Subject')['Score'].mean()`
This says: Group by Subject, look ONLY at the Score column, and calculate the average.

### Multi-Index Grouping
IBM exams frequently ask you to group by *multiple* columns. Pass them as a list!
`df.groupby(['Class', 'Subject'])['Score'].mean()`
This will show you the average Math score for 10A, the average Math score for 10B, etc.

---

## Part 2: Advanced Aggregation (`.agg`)

Sometimes you want more than just the mean. You might want the highest score, the lowest score, and the average score all at the same time.

### The `.agg()` Method
Instead of `.mean()`, we use `.agg()` and pass a list of the statistical functions we want.
`df.groupby('Subject')['Score'].agg(['mean', 'max', 'min'])`
This produces a beautiful summary table showing all three statistics side-by-side for each subject.

---

## Part 3: The `.apply()` Method (Custom Logic)

While Pandas has built-in math functions, sometimes you need to apply custom business logic.

### Creating a Custom Function
Let's say the school has a strict grading curve. We write a standard Python function:
```python
def assign_grade(score):
    if score >= 90: return 'A'
    elif score >= 80: return 'B'
    else: return 'C'
```

### Applying it to the DataFrame
We can force Pandas to run every single row of the 'Score' column through our custom function using `.apply()`:
`df['Letter_Grade'] = df['Score'].apply(assign_grade)`

### Lambda Functions (IBM Favorite)
For very simple logic, IBM expects you to use anonymous `lambda` functions inside `.apply()` to save space.
`df['Passed_With_Honors'] = df['Score'].apply(lambda x: True if x >= 90 else False)`
