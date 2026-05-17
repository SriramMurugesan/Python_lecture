# topic_15c_example.py
# Calculating and displaying a Correlation Matrix

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = {
    "Hours_Studied": [2, 3, 5, 7, 9],
    "Test_Score": [55, 60, 75, 85, 95],
    "Hours_Playing_Games": [5, 4, 2, 1, 0]
}
df = pd.DataFrame(data)
# print(df)

# print("\n--- 2. Calculating the Correlation Matrix ---")
# # .corr() computes Pearson correlation by default
corr_matrix = df.corr()
print(corr_matrix)
 






# Set up the matplotlib figure
plt.figure(figsize=(6, 4))
# Draw the heatmap
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()
