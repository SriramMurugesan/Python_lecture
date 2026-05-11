# The Exhaustive Interview Question Bank (Day-by-Day)

This document contains every possible interview question, covering theory, syntax, edge cases, debugging, and real-world architectural decisions based on the 7-day masterclass syllabus.

---

## Day 1: Python Foundations, Setup & Variables (Topics 1, 2, 3)

### Python Theory & Setup
1. **What is Python?** How does an Interpreted language differ from a Compiled language (like C++)?
2. **Dynamic vs. Static Typing:** Python is dynamically typed. What does this mean, and what are the pros and cons of this in a large enterprise application?
3. **Environment Variables:** Why is checking the "Add to PATH" box critical when installing Python on Windows? What happens if you don't?
4. **Git Workflow:** Explain the exact difference between `git init`, `git add .`, and `git commit`. 
5. **Version Control:** What is the difference between your local Git repository and a remote repository (like GitHub)? What does `git push` do?
6. **IDEs:** Why do Data Scientists prefer Jupyter Notebooks, while Software Engineers prefer VS Code?

### Variables & Memory
7. **Memory Management:** Explain conceptually how Python stores a variable in memory.
8. **Naming Conventions:** Why is `user_age = 25` valid, but `1st_user = 25` and `user age = 25` throw Syntax Errors?
9. **Data Types:** What is the strict difference between an `int` and a `float`? 
10. **Booleans:** What are the only two possible values for a Boolean? Give a real-world example of when you would use one.

### Operators & Type Casting
11. **Arithmetic:** What is the difference between standard division `/` and floor division `//`?
12. **Modulo:** What does the modulo operator `%` return? How can you use `%` to check if a number is even or odd?
13. **Type Casting (Success):** What happens exactly when you run `int("50") + 10`?
14. **Type Casting (Failure):** What happens if you run `int("Apple")`? What specific error does Python throw?
15. **Logical Operators:** Explain how `and`, `or`, and `not` work when combining multiple conditions.

---

## Day 2: Strings, Input/Output & Loops (Topics 4, 5, 6)

### String Operations
16. **Immutability:** Strings in Python are immutable. If you run `text = "Hello"`, then `text.upper()`, why does `print(text)` still print "Hello" in lowercase?
17. **Indexing:** Python uses zero-based indexing. How do you grab the very last character of a string without knowing its exact length?
18. **Slicing:** Explain the syntax `[start:stop:step]`. What does `text[::-1]` do?
19. **Membership:** How do the `in` and `not in` operators work on strings?
20. **Methods (find vs index):** Both `find()` and `index()` search for substrings. What happens in each method if the substring does NOT exist?
21. **Methods (Formatting):** What does `.strip()` do, and why is it crucial when cleaning user input?
22. **Methods (Splitting/Joining):** Explain how `.split(",")` and `", ".join(list)` are complete opposites of each other.
23. **f-strings:** Why are f-strings (`f"Hello {name}"`) considered vastly superior to older string concatenation (`"Hello " + name`)?

### Input / Output
24. **Input Type:** What data type does the `input()` function *always* return natively, regardless of what the user types?
25. **Print Arguments:** By default, `print()` adds a new line at the end. How do you force `print()` to keep the next output on the exact same line?
26. **Print Separators:** How do you change the default space separator between multiple printed items to a custom character (like `|`)?

### Loops
27. **For vs While:** Conceptually, when MUST you use a `while` loop instead of a `for` loop?
28. **Range Function:** Explain what `range(1, 10, 2)` generates. Does it include the number 10?
29. **Infinite Loops:** What causes an infinite loop in a `while` statement, and how do you prevent it?
30. **Loop Control (Break):** What exactly does the `break` keyword do to the execution flow of a loop?
31. **Loop Control (Continue):** How does `continue` differ from `break`?
32. **Nested Loops:** If an outer loop runs 5 times, and an inner loop runs 4 times, how many times total does the inner code execute?

---

## Day 3: Data Structures & File Handling (Topics 7, 8, 9)

### Lists
33. **Definition:** What is a List, and why do we use them instead of creating 100 individual variables?
34. **Mutability:** Lists are mutable. What does this mean you can do to a List that you cannot do to a String?
35. **Adding Data:** What is the difference between `.append("Apple")` and `.insert(0, "Apple")`? Which one is computationally slower on a massive list?
36. **Removing Data:** What is the difference between `.remove("Apple")` and `.pop(0)`?
37. **Sorting:** Does the `.sort()` method return a brand new sorted list, or does it permanently alter the original list?

### Dictionaries & Tuples
38. **Key-Value Architecture:** How does a Dictionary structure its data? Why is looking up data by a "Key" extremely fast?
39. **Dictionary Rules:** Can a Dictionary have duplicate Keys? What happens if you try to assign a new value to an already existing Key?
40. **Dictionary Methods:** What is the difference between `.keys()`, `.values()`, and `.items()`? Which one is most useful for a `for` loop?
41. **Tuples vs Lists:** What is the SINGLE massive difference between a Tuple and a List?
42. **Use Cases:** Why would a Senior Developer strictly mandate using a Tuple to store Geographic Coordinates (Latitude/Longitude) instead of a List?

### File Handling
43. **Persistence:** Why is file handling necessary? What happens to standard variables when a Python script finishes running?
44. **File Modes:** Explain the exact differences between `"r"`, `"w"`, and `"a"` modes. 
45. **Destructive Modes:** What happens if you open an existing, highly important file in `"w"` mode?
46. **Reading:** What is the difference between `read()` (returns a single string) and `readlines()` (returns a list)?
47. **The `with` Block:** Why is `with open("file.txt", "w") as file:` considered the absolute industry standard? What critical action does it automate?

---

## Day 4: Pandas Fundamentals (Topics 10, 11, 12)

### Introduction & DataFrames
48. **Pandas Purpose:** What is Pandas, and why is it preferred over Excel for Data Science?
49. **Architecture:** What is the structural difference between a Pandas `Series` and a Pandas `DataFrame`?
50. **Loading Data:** What method instantly converts a CSV file on your hard drive into a Pandas DataFrame?
51. **Exploration Tools:** Explain what `.head()`, `.tail()`, `.info()`, and `.describe()` tell you about a new dataset.
52. **Properties:** Why does `.shape` not use parentheses? What exactly does it return?

### Deep Dive: Selecting, Filtering & Cleaning
53. **Selecting Columns:** Why does `df["Age"]` return a Series, but `df[["Name", "Age"]]` returns a DataFrame?
54. **Selecting Rows:** What is the strict difference between `.iloc[]` (Index Location) and `.loc[]` (Location)?
55. **Filtering:** Walk through the logic of how `df[df["Salary"] > 50000]` actually filters the table behind the scenes.
56. **NaN Handling:** What is `NaN`? Why do Machine Learning models crash if they encounter it?
57. **Cleaning Strategy:** When cleaning data, under what specific business circumstances would you use `.dropna()` versus `.fillna()`?
58. **Duplicates:** What does `.drop_duplicates()` do, and why is it essential for accurate mathematical reporting?

### Grouping & Aggregating
59. **GroupBy Concept:** What does `df.groupby("Department")` do structurally to a DataFrame? How is this related to an Excel Pivot Table?
60. **Aggregations:** Name 4 common aggregation methods (e.g., `sum()`, `mean()`).
61. **Multiple Aggregations:** How do you calculate the sum AND the mean at the exact same time using the `.agg()` method?
62. **The Apply Method:** What is the `.apply()` method? How does it replace the need for writing slow, manual `for` loops?

---

## Day 5: Pandas Manipulation, Errors & Exceptions (Topics 13, 14, 15)

### Advanced Data Manipulation
63. **Combining Data:** What is the fundamental difference between `pd.concat()` and `pd.merge()`?
64. **Merging Concept:** `pd.merge()` requires an `on="column_name"` parameter. Why? How is this identical to a SQL JOIN or a VLOOKUP?
65. **Advanced Imputation (Filling blanks):** Why is filling missing test scores with the `.mean()` of the class considered a vastly superior Machine Learning strategy compared to just filling them with `0`?

### Understanding Errors
66. **Syntax Errors:** What is a Syntax Error? Will a Python script execute *any* lines of code if there is a Syntax Error on line 50?
67. **Runtime Errors:** What is a Runtime Error? If the code has perfect grammar, why does it crash?
68. **Tracebacks:** What is a Traceback? When reading a massive red error block in the terminal, where is the most important information located?
69. **Debugging Strategy:** Explain "The Print Strategy". How do you use `print()` statements to locate the exact line where a silent crash is happening?

### Exceptions in Python
70. **Exception Handling Theory:** What is the purpose of the `try` / `except` block? How does it act as a safety net?
71. **Catching Specifics:** Why is it considered a terrible, dangerous practice to use a blank `except:` block that silently catches ALL errors?
72. **Common Built-in Errors:** Describe a scenario that would specifically trigger a `ValueError`. 
73. **Common Built-in Errors:** Describe a scenario that would specifically trigger a `TypeError`.
74. **Common Built-in Errors:** Describe a scenario that would specifically trigger a `KeyError`.
75. **Raising Errors:** What does the `raise` keyword do? Why would a programmer intentionally *want* to crash their own program?

---

## Day 6: Advanced Exceptions & Regression Concepts (Topics 16, 17)

### Advanced Exceptions
76. **Multiple Excepts:** Can you chain multiple `except` blocks together? How does Python decide which one to execute?
77. **The Finally Block:** What is the absolute, guaranteed rule of the `finally` block?
78. **Finally Use-Case:** Give a real-world enterprise example of when you MUST use a `finally` block (Hint: databases/files).
79. **Custom Error Classes:** How do you define a custom error? (Explain `class MyError(Exception): pass`). Why would a bank need an `InsufficientFundsError` instead of just a generic `ValueError`?

### Regression & Correlation Concepts
80. **Correlation Definition:** In statistics and Data Science, what exactly does Correlation measure?
81. **Positive vs Negative Correlation:** Give a real-world example of a Positive Correlation and a Negative Correlation.
82. **Correlation Matrix:** When you run `df.corr()`, the results are between `-1.0` and `1.0`. What does a score of `0.0` mean? What does `-0.95` mean?
83. **Correlation vs Causation:** Explain the phrase "Correlation does not imply Causation." Give a funny or real-world example.
84. **Regression Theory:** What is Regression attempting to do mathematically? (Explain the concept of drawing a "Line of Best Fit" through a scatter plot).
85. **Prediction Concept:** Once a Line of Best Fit is established by an AI, how does it predict the future? (Explain plugging an X value into the line to find the Y value).

---

## Day 7: Linear Regression Models & ML Workflow (Topics 18, 19)

### Linear Regression (Hands-On)
86. **Scikit-Learn Library:** What is `scikit-learn` (`sklearn`), and why is it the industry standard for Python Machine Learning?
87. **Features vs. Target:** Explain the standard ML convention of `X` (Features) and `y` (Target). Why is `X` capitalized and `y` lowercase?
88. **Train/Test Split Theory:** Why is it a fatal ML mistake to train a model on 100% of your data and then evaluate it on that exact same data?
89. **Model Fitting:** What is the computer physically doing under the hood when you run `model.fit(X_train, y_train)`?
90. **Model Predicting:** What is the computer doing when you run `model.predict(X_test)`? Why do we ONLY pass `X_test` into the predict function?
91. **Evaluation Metrics (MAE):** What does Mean Absolute Error (MAE) measure? If an AI predicts house prices and the MAE is 10,000, what does that number represent in English?

### The Mini Project (Full ML Pipeline)
92. **Pipeline Step 1 (Loading):** Why is Pandas always the very first step in a tabular ML pipeline?
93. **Pipeline Step 2 (Cleaning):** If you skip data cleaning and pass a DataFrame with `NaN` values directly into `LinearRegression().fit()`, what happens?
94. **Pipeline Step 3 (EDA):** What is Exploratory Data Analysis (EDA)? Why must we run `.corr()` before we decide which Features (`X`) to feed into our model?
95. **Pipeline Step 4 (Training):** Why do we set a `random_state=42` when running `train_test_split`? What happens if we don't?
96. **Pipeline Step 5 (Evaluation):** If your model's MAE is extremely high (meaning it's terribly inaccurate), what are 3 things you could do to the data to try and improve the model's accuracy?
97. **Feature Importance:** If you add a feature like "Eye Color" to predict "Test Scores", the correlation will be near 0.0. Will adding this useless feature make the ML model better, worse, or the same?
98. **Business Application:** Once `model.predict()` is proven to be accurate, how does a business actually use this script in the real world to make money or save time? (Explain the concept of feeding brand new, unseen data into the live model).
