# topic_15d_example.py
# Basic Churn Analysis using Pandas
# what is churn analysis, why do we do this?
# churn analysis is the process of analyzing customer behavior and identifying customers who are likely to stop using our product or service.
# why do we do this?
# customer retention, increasing revenue, reducing costs, improving customer satisfaction

import pandas as pd

print("--- 1. Loading Customer Data ---")
# Creating a mock dataset of customers
data = {
    "CustomerID": [101, 102, 103, 104, 105, 106],
    "Tenure_Months": [24, 2, 18, 1, 36, 4],
    "Monthly_Charge": [60.5, 80.0, 55.0, 95.0, 45.0, 85.0],
    "Contract_Type": ["Two Year", "Month-to-month", "One Year", "Month-to-month", "Two Year", "Month-to-month"],
    "Churn": ["No", "Yes", "No", "Yes", "No", "Yes"]
}
df = pd.DataFrame(data)
print(df)

print("\n--- 2. Calculating Overall Churn Rate ---")
# Count how many customers have Churn == 'Yes'
total_customers = len(df)
churned_customers = len(df[df['Churn'] == 'Yes'])
churn_rate = (churned_customers / total_customers) * 100
print(f"Overall Churn Rate: {churn_rate:.2f}%")

print("\n--- 3. Analyzing Churn Drivers (EDA) ---")
print("Average Tenure grouped by Churn:")
# Are churned customers newer or older?
avg_tenure = df.groupby('Churn')['Tenure_Months'].mean()
print(avg_tenure)

print("\nAverage Monthly Charge grouped by Churn:")
# Do churned customers pay more on average?
avg_charge = df.groupby('Churn')['Monthly_Charge'].mean()
print(avg_charge)

print("\nChurn by Contract Type:")
# Which contract type has the highest churn?
contract_churn = df.groupby(['Contract_Type', 'Churn']).size().unstack(fill_value=0)
print(contract_churn)

# what is the outcome we can conclude from this analysis?
# outcome is that month to month customers are more likely to churn than two year or one year customers and also the customers who are paying more are more likely to churn.
# what should we do to improve the churn rate?
# we should try to convert month to month customers to one year or two year contracts.
# we should try to reduce the monthly charge for customers who are paying more.