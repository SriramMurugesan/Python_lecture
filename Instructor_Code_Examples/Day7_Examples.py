# ==========================================
# DAY 7: MACHINE LEARNING & CAPSTONE
# ==========================================
import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# --- Topic 18: Linear Regression Hands-On ---
print("--- Topic 18: Linear Regression ---")

# 1. Dummy Data preparation
X = np.array([[10], [20], [30], [40], [50]])  # Features (Must be 2D array)
y = np.array([15, 25, 35, 45, 55])            # Target (1D array)

# 2. Split data (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. Initialize and Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Predict
predictions = model.predict(X_test)
print(f"Actual Test Values: {y_test}")
print(f"Predicted Values: {predictions}")
print(f"R2 Score: {r2_score(y_test, predictions)}\n")

# --- Topic 19: Capstone Mini Project Walkthrough ---
print("--- Topic 19: Capstone Pipeline Demo ---")
try:
    # Attempt to load the synthetic data generated earlier
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, '../Student_Materials/capstone_sales_data.csv')
    
    df = pd.read_csv(data_path)
    print("1. Data Loaded Successfully.")
    
    # Clean data
    df = df.dropna(subset=['Sales']) # Drop rows where target is missing
    df['Customer_Age'] = df['Customer_Age'].fillna(df['Customer_Age'].mean())
    print("2. Data Cleaned.")
    
    # Select features
    X = df[['Ads_Spend']]
    y = df['Sales']
    
    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Fit model
    capstone_model = LinearRegression().fit(X_train, y_train)
    print("3. Model Trained on Capstone Data.")
    
    # Evaluate
    preds = capstone_model.predict(X_test)
    print(f"4. Evaluation -> R2 Score: {r2_score(y_test, preds):.4f}")
    
    # Insight
    print(f"5. Business Insight -> For every $1 in Ads, Sales increase by ${capstone_model.coef_[0]:.2f}")

except FileNotFoundError:
    print("Capstone dataset not found. Please run the generate_capstone_data.py script in the Student_Materials folder first!")
