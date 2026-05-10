# ==========================================
# DAY 4: PANDAS FOUNDATIONS
# ==========================================
import pandas as pd

# --- Topic 10: Pandas Intro ---
print("--- Topic 10: Pandas Intro ---")
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'Department': ['HR', 'IT', 'IT', 'Finance'],
    'Salary': [50000, 75000, 80000, 60000]
}
df = pd.DataFrame(data)
print("DataFrame created from dictionary:")
print(df)
print("\n")

# --- Topic 11: Series & DF Deep Dive ---
print("--- Topic 11: Deep Dive ---")
print("Selecting one column (Series):")
print(df['Name'])

print("\nConditional Filtering (Age > 28):")
adults = df[df['Age'] > 28]
print(adults)

print("\nDropping a column:")
df_dropped = df.drop(columns=['Age'])
print(df_dropped)
print("\n")

# --- Topic 12: Grouping & Aggregating ---
print("--- Topic 12: Grouping ---")
print("Average Salary per Department:")
avg_salary = df.groupby('Department')['Salary'].mean()
print(avg_salary)

print("\nDescriptive Statistics (.describe()):")
print(df.describe())
