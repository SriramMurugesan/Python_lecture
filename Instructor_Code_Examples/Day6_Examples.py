# ==========================================
# DAY 6: ADVANCED EXCEPTIONS & STATS
# ==========================================
import pandas as pd

# --- Topic 16: Try/Except/Finally & Custom ---
print("--- Topic 16: Try/Except/Finally ---")

class InsufficientFundsError(Exception):
    """Custom exception class for banking"""
    pass

try:
    print("Opening transaction log...")
    raise InsufficientFundsError("User tried to overdraw $500.")
except InsufficientFundsError as e:
    print(f"Exception Handled: {e}")
except Exception as e:
    print("Catch-all for other errors.")
finally:
    print("Finally block executes: Closing transaction log...\n")

# --- Topic 17: Regression Concepts ---
print("--- Topic 17: Correlation Concepts ---")
# Creating a dummy dataset to show correlation
df = pd.DataFrame({
    'Ads_Spend': [100, 200, 300, 400, 500],
    'Sales': [150, 250, 340, 460, 550],  # Goes up as Ads_Spend goes up
    'Age': [45, 22, 31, 55, 29]          # Random, no correlation
})

print("Dataset:")
print(df)

print("\nCorrelation Matrix:")
print(df.corr())
print("\nNotice how Ads_Spend and Sales have a correlation close to 1.0 (Positive Correlation).")
print("Age has a correlation close to 0.0 (No Correlation).")
