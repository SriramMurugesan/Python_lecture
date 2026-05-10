"""
Python Training - Debugging Tasks
Instructions for Students: 
Uncomment the section for the topic you are learning. 
Run the script, read the error traceback carefully, and fix the code!
"""

# ==========================================
# DAY 1
# ==========================================

# --- Topic 3: Variables & Data Types ---
# total = "10" + 5
# print("The total is:", total)

# ==========================================
# DAY 2
# ==========================================

# --- Topic 4: String Operations ---
# name = "python"
# name[0] = "P"
# print(name)

# --- Topic 5: Input/Output ---
# age = input("Enter your age: ")
# print("In 5 years, you will be:", age + 5)

# --- Topic 6: Loops ---
# count = 5
# while count > 0:
#     print("Counting down:", count)
# print("Done!")

# ==========================================
# DAY 3
# ==========================================

# --- Topic 7: Lists ---
# nums = [10, 20, 30]
# print("The fourth number is:", nums[3])

# --- Topic 8: Dictionaries ---
# data = {"name": "Alice", "city": "New York"}
# print("Age is:", data["age"])

# --- Topic 9: File Handling ---
# f = open("data.txt", "r")
# f.write("Hello, World!")
# f.close()

# ==========================================
# DAY 4
# ==========================================

# --- Topic 10: Pandas Intro ---
# import pandas as pd
# df = pd.DataFrame([1, 2, 3], ["A", "B", "C"])
# print(df.head)

# --- Topic 11: Series & DataFrames ---
# import pandas as pd
# df = pd.DataFrame({'A': [1,2,1], 'B': [3,4,5]})
# df['A'] == 1
# print("Filtered Data:\n", df)

# --- Topic 12: Grouping ---
# import pandas as pd
# df = pd.DataFrame({'Dept': ['IT', 'HR', 'IT'], 'Salary': [60, 50, 70]})
# grouped = df.groupby('Dept')
# print("Average Salary by Dept:\n", grouped)

# ==========================================
# DAY 5
# ==========================================

# --- Topic 13: Data Manipulation ---
# import pandas as pd
# df = pd.DataFrame({'A': [1, None, 3], 'B': [4, 5, 6]})
# df.dropna()
# print("Cleaned DataFrame:\n", df)

# --- Topic 14: Understanding Errors ---
# for i in range(5)
#     print("Loop iteration:", i)

# --- Topic 15: Exceptions ---
# try:
#     x = 10 / 0
# except ValueError:
#     print("Handled the error gracefully!")

# ==========================================
# DAY 6
# ==========================================

# --- Topic 16: Try/Except/Finally ---
# try:
#     f = open("log.txt", "w")
#     f.write("Starting...\n")
#     1 / 0
# except ValueError:
#     print("A math error occurred.")
#     f.close()

# --- Topic 17: Correlation ---
# import pandas as pd
# df = pd.DataFrame({'Category': ["High", "Low", "Medium"], 'Value': [100, 20, 50]})
# print("Correlation:\n", df.corr())

# ==========================================
# DAY 7
# ==========================================

# --- Topic 18: Linear Regression ---
# from sklearn.linear_model import LinearRegression
# X = [1, 2, 3, 4]
# y = [2, 4, 6, 8]
# model = LinearRegression()
# model.fit(X, y)
# print("Model trained!")

# --- Topic 19: Capstone Logical Bug ---
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# df = pd.DataFrame({'Ads_Spend': [100, 200, 300], 'Sales': [150, 250, 350]})
# X = df[['Ads_Spend', 'Sales']] # Features
# y = df['Sales']                # Target
# model = LinearRegression().fit(X, y)
# print("R2 Score (Suspiciously perfect):", model.score(X, y))
