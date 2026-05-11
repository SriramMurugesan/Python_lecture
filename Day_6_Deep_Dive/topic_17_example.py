# topic_17_example.py
# Understanding Correlation Matrices and Regression foundations in Pandas.

import pandas as pd

print("--- 1. Creating an Analytical Dataset ---")
# Let's create a dataset showing the relationship between Advertising Spend,
# the Price of the product, and the final Sales numbers.
business_data = {
    "Ad_Spend": [1000, 2000, 3000, 4000, 5000],
    "Price": [50, 50, 48, 48, 45], # The product price is dropping slightly
    "Sales": [150, 300, 450, 600, 750]
}

df = pd.DataFrame(business_data)
print("Business Dataset:\n", df)

print("\n--- 2. The Correlation Matrix ---")
# .corr() mathematically calculates relationships between -1.0 and 1.0 for the whole table
correlation_matrix = df.corr()
print("Correlation Matrix:\n", correlation_matrix)

print("\n--- 3. Analyzing the Results ---")
print("Notice how 'Ad_Spend' and 'Sales' have a perfect 1.0 score.")
print("This proves a 100% Positive Correlation: More Ads = More Sales!")

print("\nNotice how 'Price' and 'Sales' have a negative score (around -0.9).")
print("This proves a Negative Correlation: Lower Price = More Sales!")

print("\n--- 4. Regression Theory (Prediction Concept) ---")
# If we were to apply a Machine Learning Regression Model to this exact data,
# the computer would do the math and realize that every $1,000 in Ad_Spend generates exactly 150 Sales.
# The ML Model would then confidently predict that $6,000 in Ad_Spend would generate 900 Sales!
# We will actually build this model using Python in the upcoming final days!
