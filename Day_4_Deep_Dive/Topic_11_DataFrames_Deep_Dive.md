# Topic 11: DataFrames Deep Dive (2-Hour Lab)

In the real world, data is never clean. The IBM certification heavily tests your ability to take a raw, messy CSV and transform it into a mathematically sound DataFrame ready for Machine Learning. In this 2-hour lab, we will filter, clean, and standardize our student data.

---

## Part 1: Advanced Filtering (Boolean Indexing)

You rarely want to analyze an entire dataset at once. You usually want a subset: "Show me all students who failed Math."

### The Power of Boolean Arrays
When you type `df['Score'] > 80`, Pandas doesn't give you the scores. It gives you a `Series` of True/False values (a Boolean Array). 
To actually see the data, you must wrap that condition inside the DataFrame brackets: 
`df[df['Score'] > 80]`

### Multiple Conditions
IBM exams love testing multiple conditions. 
- Use `&` for AND (both must be true).
- Use `|` for OR (either can be true).
**CRITICAL RULE:** When using multiple conditions, you MUST wrap each condition in parentheses!
Example: `df[(df['Score'] > 80) & (df['Subject'] == 'Math')]`

---

## Part 2: The Art of Data Cleaning

Missing data is the enemy of Machine Learning. If you feed a `NaN` (Not a Number) into a predictive model, it will crash. 

### Identifying the Missing Data
Use `df.isnull().sum()` to get a quick count of how many missing values exist in each column.

### Strategy 1: Dropping Data (`dropna`)
If a row is missing critical information, sometimes the best strategy is to delete the row entirely.
- `df.dropna()` deletes any row that contains at least one `NaN`.
- *Warning:* If your dataset is small, you might accidentally delete 50% of your data! IBM often tests if you know when *not* to use this.

### Strategy 2: Imputing Data (`fillna`)
Instead of deleting data, we fill the gap with a logical replacement.
- For numerical data (like 'Score'), we often fill missing values with the `mean` or `median` of the column.
- `df['Score'].fillna(df['Score'].mean(), inplace=True)`

---

## Part 3: Transformation and Standardization

### Type Casting (`astype`)
Sometimes numbers are imported as strings (e.g., `"85"` instead of `85`). You cannot do math on strings. 
You must cast the column: `df['Score'] = df['Score'].astype(float)`

### String Manipulation (`.str` accessor)
Human entry causes messy text. "Alice Smith", " alice smith ", and "ALICE SMITH" are treated as three completely different people by a computer.
We use the `.str` accessor to standardize text columns across the entire DataFrame at once.
- `.str.strip()` removes accidental spaces at the beginning or end.
- `.str.title()` capitalizes the first letter of each word.
