# topic_11_example.py
# Deep dive into selecting, filtering, and cleaning data.

import pandas as pd

# Creating a messy DataFrame with missing values (None) and duplicates
messy_data = {
    "Employee": ["John", "Sarah", "John", "Mike", "Anna"],
    "Department": ["Sales", "HR", "Sales", "IT", None],
    "Salary": [50000, 60000, 50000, None, 70000]
}
df = pd.DataFrame(messy_data)

print("--- Original Messy DataFrame ---")
print(df)

print("\n--- 1. Selecting Columns ---")
# Single bracket = Series
print("Selecting just the Employee column:\n", df["Employee"])

# Double brackets = DataFrame
print("\nSelecting Employee and Salary columns:\n", df[["Employee", "Salary"]])

print("\n--- 2. Selecting Rows (iloc) ---")
print("Grabbing the very first row (index 0):\n", df.iloc[0])

print("\n--- 3. Filtering Data ---")
# Let's find employees making more than 55000
# Notice that comparing math with NaN (missing data) safely ignores the missing data!
high_earners = df[df["Salary"] > 55000]
print("Employees making over 55000:\n", high_earners)

print("\n--- 4. Cleaning Data: Duplicates ---")
# John in Sales with 50000 is accidentally listed twice!
clean_df = df.drop_duplicates()
print("After dropping exact duplicates:\n", clean_df)

print("\n--- 5. Cleaning Data: Missing Values ---")
# We have a missing Department and a missing Salary
# Let's fill the missing Salary safely with 0
clean_df["Salary"] = clean_df["Salary"].fillna(0)
print("After filling missing Salaries with 0:\n", clean_df)

# Let's drop any row that STILL has a missing value (Anna's Department is missing)
final_df = clean_df.dropna()
print("After dropping rows with ANY missing values left:\n", final_df)

print("\n--- 6. Renaming Columns ---")
# Let's rename 'Employee' to 'Name'
final_df = final_df.rename(columns={"Employee": "Name"})
print("After renaming the Employee column:\n", final_df)
