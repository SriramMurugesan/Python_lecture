# topic_10_example.py
# Introduction to Pandas, Series, DataFrames, and basic exploration.

import pandas as pd

print("--- 1. Creating a Series (1D Data) ---")
# A Series is just a single column of data
ages = pd.Series([25, 30, 22, 40])
print("Ages Series:\n", ages)

print("\n--- 2. Creating a DataFrame (2D Table) ---")
# A DataFrame is a full table. We can build it using a Python Dictionary!
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [25, 30, 22, 40, 28],
    "City": ["New York", "Paris", "London", "Tokyo", "Paris"]
}

# Convert the dictionary into a Pandas DataFrame
df = pd.DataFrame(data)
print("\nFull DataFrame:\n", df)

print("\n--- 3. Simulating Loading Data ---")
# Usually, you would do: df = pd.read_csv("data.csv")
# For this example, we will save our DataFrame to a CSV, then load it back!
df.to_csv("my_data.csv", index=False)
print("Saved data to 'my_data.csv' successfully!")

# Loading it back from the file into a brand new variable
loaded_df = pd.read_csv("my_data.csv")
print("Successfully loaded 'my_data.csv' into a new DataFrame!")

print("\n--- 4. Basic Data Exploration ---")
print("First 2 rows using head(2):\n", loaded_df.head(2))
print("\nLast 2 rows using tail(2):\n", loaded_df.tail(2))

print("\nShape of the DataFrame (Rows, Columns):", loaded_df.shape)

print("\nStatistical Description (Math Summary):\n", loaded_df.describe())

print("\nDataFrame Info:")
# info() prints directly to the screen by default
loaded_df.info()
