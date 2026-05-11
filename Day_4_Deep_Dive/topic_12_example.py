# topic_12_example.py
# Grouping, Aggregating, and Applying functions to data.

import pandas as pd

# Creating a Sales DataFrame
sales_data = {
    "Region": ["North", "South", "North", "East", "South", "East"],
    "Product": ["Laptops", "Phones", "Phones", "Laptops", "Laptops", "Phones"],
    "Revenue": [10000, 5000, 7000, 12000, 8000, 6000]
}
df = pd.DataFrame(sales_data)

print("--- Original Sales DataFrame ---")
print(df)

print("\n--- 1. Grouping and Aggregating (Sum) ---")
# Group by Region, look at Revenue, and Sum it up
regional_revenue = df.groupby("Region")["Revenue"].sum()
print("Total Revenue by Region:\n", regional_revenue)

print("\n--- 2. Grouping and Aggregating (Mean/Average) ---")
# Group by Product, look at Revenue, and find the Average
average_product_revenue = df.groupby("Product")["Revenue"].mean()
print("Average Revenue per Product:\n", average_product_revenue)

print("\n--- 3. Multiple Aggregations using agg() ---")
# We want the total sum, the average, and the count all at the same time!
multi_agg = df.groupby("Region")["Revenue"].agg(["sum", "mean", "count"])
print("Detailed Revenue Stats per Region:\n", multi_agg)

print("\n--- 4. The apply() Method ---")
# apply() runs a built-in function on every item in a column automatically
# Let's find the length (number of letters) of every Region name using the built-in 'len' function
df["Region_Name_Length"] = df["Region"].apply(len)

print("DataFrame after applying 'len' to the Region column:\n", df)

print("\n--- 5. Describing Grouped Data ---")
# You can also use describe() on a groupby object for a massive summary of each group!
print("Full mathematical description grouped by Product:\n", df.groupby("Product")["Revenue"].describe())
