# ==========================================
# 📘 Day 6: Advanced Control Flow & Statistics
# ==========================================
import pandas as pd

# ---------------------------------------------------------
# 🕒 Topic 16: Try/Except/Finally + Custom Exceptions
# ---------------------------------------------------------
print("--- Topic 16: Live Code ---")
class InsufficientFundsError(Exception):
    pass

def transfer(bal, amt):
    if amt > bal:
        raise InsufficientFundsError("Not enough money.")
    return bal - amt

try:
    transfer(100, 200)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
finally:
    print("Database connection successfully closed.")

print("\n--- Topic 16: Debugging Requirement ---")
# Broken Code:
# try:
#     f = open("file.txt", "r")
#     print(1 / 0)
# except ValueError:
#     print("Math error")
#     f.close()
print("Fix: 1/0 creates ZeroDivisionError, bypassing ValueError. f.close() is skipped. Put it in `finally:`.")

# ---------------------------------------------------------
# 🕒 Topic 17: Regression & Correlation Concepts
# ---------------------------------------------------------
print("\n--- Topic 17: Live Code ---")
df = pd.DataFrame({'Ads': [100, 200, 300], 'Sales': [150, 250, 350]})
corr = df.corr()
print("Correlation Matrix:\n", corr)

print("\n--- Topic 17: Debugging Requirement ---")
# Broken Code:
# df_str = pd.DataFrame({'Region': ["North", "South"], 'Sales': [100, 200]})
# print(df_str.corr())
print("Fix: Correlation requires numeric data. String categories like 'North' will fail or be dropped.")
