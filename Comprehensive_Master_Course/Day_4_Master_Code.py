# ==========================================
# 📘 Day 4: Data Science Foundations - Pandas
# ==========================================
import pandas as pd

# ---------------------------------------------------------
# 🕒 Topic 10: Introduction to Pandas
# ---------------------------------------------------------
print("--- Topic 10: Live Code ---")
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
print(df.head())

print("\n--- Topic 10: Debugging Requirement ---")
# Broken Code:
# df = pd.DataFrame([1, 2, 3], ["A", "B", "C"])
# print(df.head)
print("Fix: Call the method with parentheses -> df.head()")

# ---------------------------------------------------------
# 🕒 Topic 11: Series & DataFrames Deep Dive
# ---------------------------------------------------------
print("\n--- Topic 11: Live Code ---")
# Expanding dummy data for demo
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [17, 25, 30], 'UnnecessaryCol': [1,2,3]})

adults = df[df['Age'] >= 18]
specific_user = df.loc[0, 'Name']
cleaned_df = df.drop(columns=['UnnecessaryCol'])
print("Adults filtered:")
print(adults)

print("\n--- Topic 11: Debugging Requirement ---")
# Broken Code:
# df['Age'] == 25
print("Fix: Actually apply the boolean mask -> df = df[df['Age'] == 25]")

# ---------------------------------------------------------
# 🕒 Topic 12: Grouping & Aggregating
# ---------------------------------------------------------
print("\n--- Topic 12: Live Code ---")
df_group = pd.DataFrame({'Dept': ['IT', 'HR', 'IT'], 'Salary': [60, 50, 70]})
avg_salary = df_group.groupby('Dept')['Salary'].mean()
print(avg_salary)
print("\nDescribe Output:")
print(df_group.describe())

print("\n--- Topic 12: Debugging Requirement ---")
# Broken Code:
# grouped = df_group.groupby('Dept')
# print(grouped)
print("Fix: Apply an aggregate function like .sum() or .mean() to the groupby object.")
