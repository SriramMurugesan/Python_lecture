# Topic 15c: Exploratory Data Analysis (EDA) - Correlation Matrix

## What is a Correlation Matrix?
In Data Analysis, correlation measures the statistical relationship between two variables. A correlation matrix is a table showing correlation coefficients between sets of variables.
- A correlation of `1.0` means a perfect positive relationship.
- A correlation of `-1.0` means a perfect negative relationship.
- A correlation of `0.0` means no relationship.

## Why use it?
When exploring datasets (Exploratory Data Analysis - EDA), identifying highly correlated features can help in feature selection for machine learning models, or understanding which metrics move together (e.g., studying hours and exam scores).

## Generating a Correlation Matrix using Pandas
Pandas DataFrames have a built-in `.corr()` method that automatically calculates the correlation between all numeric columns.

```python
import pandas as pd

# Assume df is a pandas DataFrame with numeric columns
correlation_matrix = df.corr()
print(correlation_matrix)
```

## Visualizing with Seaborn
To make the correlation matrix easier to read, data scientists often visualize it using a heatmap from the `seaborn` library.
