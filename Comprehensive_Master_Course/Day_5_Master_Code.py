# ==========================================
# 📘 Day 5: Advanced Data & Error Handling
# ==========================================
import pandas as pd
import numpy as np

# ---------------------------------------------------------
# 🕒 Topic 13: Data Manipulation
# ---------------------------------------------------------
print("--- Topic 13: Live Code ---")
df1 = pd.DataFrame({'ID': [1,2], 'Val': [10, np.nan]})
df2 = pd.DataFrame({'ID': [2,3], 'Score': [90, 80]})

merged = pd.merge(df1, df2, on='ID', how='outer')
cleaned = merged.fillna(0)
print(cleaned)

print("\n--- Topic 13: Debugging Requirement ---")
# Broken Code:
# df_err = pd.DataFrame({'A': [1, None, 3]})
# df_err.dropna()
# print(df_err)
print("Fix: Pandas operations are not in-place by default. Do -> df = df.dropna()")

# ---------------------------------------------------------
# 🕒 Topic 14: Understanding Errors
# ---------------------------------------------------------
print("\n--- Topic 14: Live Code ---")
def divide_amounts(a, b):
    print(f"[DEBUG] Attempting to divide {a} by {b}")
    return a / b
# print(divide_amounts(10, 0)) # Will throw ZeroDivisionError

print("\n--- Topic 14: Debugging Requirement ---")
# Broken Code:
# for i in range(5)
#     print(i)
print("Fix: Missing colon causing SyntaxError. Add `:` -> for i in range(5):")

# ---------------------------------------------------------
# 🕒 Topic 15: Exceptions in Python
# ---------------------------------------------------------
print("\n--- Topic 15: Live Code ---")
try:
    # age = int(input("Enter age: "))
    age = int("Twenty") # Simulating bad input
except ValueError:
    print("Invalid input! Please enter numbers only.")

def withdraw(amount):
    if amount < 0:
        raise ValueError("Cannot withdraw a negative amount!")

print("\n--- Topic 15: Debugging Requirement ---")
# Broken Code:
# try:
#     x = 10 / 0
# except ValueError:
#     print("Error caught!")
print("Fix: ZeroDivisionError bypasses the ValueError block. Use correct Exception class.")
