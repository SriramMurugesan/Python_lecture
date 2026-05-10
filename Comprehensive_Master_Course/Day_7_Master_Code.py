# ==========================================
# 📘 Day 7: Machine Learning & Capstone
# ==========================================
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import os

# ---------------------------------------------------------
# 🕒 Topic 18: Linear Regression (Hands-On)
# ---------------------------------------------------------
print("--- Topic 18: Live Code ---")
X = np.array([[1], [2], [3], [4]]) 
y = np.array([2, 4, 6, 8])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

preds = model.predict(X_test)
print(f"R2 Score: {r2_score(y_test, preds)}")

print("\n--- Topic 18: Debugging Requirement ---")
# Broken Code:
# X_flat = [1, 2, 3, 4]
# y_flat = [2, 4, 6, 8]
# model.fit(X_flat, y_flat)
print("Fix: scikit-learn strictly expects 2D structure for Features X. A flat 1D list causes a ValueError.")

# ---------------------------------------------------------
# 🕒 Topic 19: Capstone Mini Project
# ---------------------------------------------------------
print("\n--- Topic 19: Live Code (Pipeline) ---")
try:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, '../Student_Materials/capstone_sales_data.csv')
    df = pd.read_csv(data_path)
    
    # Clean
    df = df.dropna(subset=['Sales']) 
    
    # Features & Target
    X = df[['Ads_Spend']]
    y = df['Sales']
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    # Model
    cap_model = LinearRegression().fit(X_train, y_train)
    
    # Report
    print(f"Capstone R2 Score: {cap_model.score(X_test, y_test):.4f}")
except FileNotFoundError:
    print("Run `generate_capstone_data.py` inside Student_Materials first to generate the CSV!")

print("\n--- Topic 19: Debugging Requirement ---")
print("Broken Workflow: Target variable ('Sales') is included inside the Feature set (X).")
print("Fix: Data Leakage! The target must ALWAYS be dropped from X, or the model achieves a fake 1.0 R2 score.")
