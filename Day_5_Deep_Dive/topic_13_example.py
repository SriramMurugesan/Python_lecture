# topic_13_example.py
# Merging, Concatenating, and preparing data for Machine Learning.

import pandas as pd

print("--- 1. Concatenation (Stacking Data) ---")
# Imagine downloading a new CSV file every single month
january_sales = pd.DataFrame({"Item": ["Apple", "Banana"], "Sales": [100, 150]})
february_sales = pd.DataFrame({"Item": ["Cherry", "Date"], "Sales": [200, 50]})

# Stacking them directly on top of each other into one master table
# ignore_index=True resets the row numbers on the far left so they go 0, 1, 2, 3 perfectly
master_sales = pd.concat([january_sales, february_sales], ignore_index=True)
print("Master Sales Table (Concatenated):\n", master_sales)

# print("\n--- 2. Merging (VLOOKUP / JOIN) ---")
# # We have employee names in one table...
employees = pd.DataFrame({
    "Emp_ID": [1, 2, 3],
    "Name": ["John", "Sarah", "Mike"]
})

# # ...and their salaries in a completely different table!
salaries = pd.DataFrame({
    "Emp_ID": [1, 2, 3],
    "Salary": [60000, 80000, 75000]
})

# # We merge them together horizontally using the shared "Emp_ID" column
full_employee_data = pd.merge(employees, salaries, on="Emp_ID")
print("Merged Employee Table:\n", full_employee_data)

# print("\n--- 3. Handling Missing Values for Machine Learning ---")
data_with_blanks = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Test_Score": [85, None, 92, None] # Bob and David completely missed the test!
})
print("Original Data with Blanks (NaN):\n", data_with_blanks)

# # Machine Learning models hate NaN. Let's fill the missing scores safely!
# # First, calculate the average (mean) of the Test_Score column
class_average = data_with_blanks["Test_Score"].mean()
print(f"The class average is: {class_average}")

# # Now, target the exact column and fill the NaNs with that average
data_with_blanks["Test_Score"] = data_with_blanks["Test_Score"].fillna(class_average)
print("\nCleaned Data ready for Machine Learning:\n", data_with_blanks)
