# ==========================================
# DAY 5: ADVANCED DATA & ERRORS
# ==========================================
import pandas as pd

# --- Topic 13: Data Manipulation ---
print("--- Topic 13: Data Manipulation ---")
df1 = pd.DataFrame({'ID': [1, 2], 'Name': ['Alice', 'Bob']})
df2 = pd.DataFrame({'ID': [2, 3], 'Score': [90, 85]})

print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

print("\nOuter Merge (joining tables):")
merged = pd.merge(df1, df2, on='ID', how='outer')
print(merged)

print("\nHandling Missing Values (NaN):")
# Fill NaN with a default value
cleaned = merged.fillna({"Name": "Unknown", "Score": 0})
print(cleaned)
print("\n")

# --- Topic 14: Understanding Errors ---
print("--- Topic 14: Errors (Instructor Note: Uncomment in class) ---")
# Syntax Error: Missing colon 
# for i in range(5)
#     print(i)

# Runtime Error: Division by zero 
# print(10 / 0)

# --- Topic 15: Exceptions ---
print("--- Topic 15: Exceptions ---")
try:
    print("Trying to divide by zero...")
    result = 10 / 0
except ZeroDivisionError:
    print("Caught a ZeroDivisionError! Program continues safely.")

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds!")
    return balance - amount

print("\nTesting Custom Raise:")
try:
    withdraw(100, 500)
except ValueError as e:
    print(f"Error caught: {e}")
