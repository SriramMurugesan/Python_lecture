import pandas as pd
import numpy as np
import os

# Set random seed for reproducibility
np.random.seed(42)

num_records = 500

print("Generating synthetic sales dataset for Day 7 Capstone...")

# Generate synthetic features
dates = pd.date_range(start='2024-01-01', periods=num_records, freq='D')
regions = np.random.choice(['North', 'South', 'East', 'West'], num_records)
ads_spend = np.random.uniform(500, 5000, num_records)
customer_age = np.random.randint(18, 65, num_records)

# Simulate relationship: Sales = Base + (Coefficient * Ads_Spend) + random noise
# Customer_Age has no real effect, acting as a dummy variable
noise = np.random.normal(0, 800, num_records)
sales = 1000 + (3.2 * ads_spend) + noise

df = pd.DataFrame({
    'Transaction_ID': range(1, num_records + 1),
    'Date': dates,
    'Region': regions,
    'Customer_Age': customer_age,
    'Ads_Spend': np.round(ads_spend, 2),
    'Sales': np.round(sales, 2)
})

# Introduce Missing Values to test data cleaning skills (Day 4/5 concepts)
# Remove some ages
missing_age_indices = np.random.choice(df.index, 25, replace=False)
df.loc[missing_age_indices, 'Customer_Age'] = np.nan

# Remove some sales (Target variable!)
missing_sales_indices = np.random.choice(df.index, 10, replace=False)
df.loc[missing_sales_indices, 'Sales'] = np.nan

# Save to CSV
output_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(output_dir, 'capstone_sales_data.csv')

df.to_csv(output_file, index=False)
print(f"✅ Successfully generated {output_file} with {num_records} records.")
print("Instructors: Run this script anytime to generate a fresh dataset for the final project.")
