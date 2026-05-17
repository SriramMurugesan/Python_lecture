# topic_20_example.py
# Random Forest Classification
#what is Random Forest Classification?
# Random Forest Classification is a supervised machine learning algorithm used for classification tasks. It works by creating multiple decision trees during training and combining their predictions to make a final prediction.
#why do we use Random Forest Classification?
# Random Forest Classification is used for classification tasks because it is a robust algorithm that can handle large datasets and high-dimensional data. It is also less prone to overfitting than other algorithms.
# difference between linear regression and random forest classification:
# Linear Regression is a supervised machine learning algorithm used for regression tasks. It works by creating a linear relationship between the independent variables and the dependent variable. Random Forest Classification is a supervised machine learning algorithm used for classification tasks. It works by creating multiple decision trees during training and combining their predictions to make a final prediction.

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

print("--- 1. Preparing the Data ---")
# We'll use a mock dataset predicting if a user buys a product based on Age and Estimated Salary
data = {
    "Age": [22, 25, 47, 52, 46, 56, 31, 28, 35, 42],
    "EstimatedSalary": [20000, 30000, 150000, 180000, 160000, 175000, 50000, 45000, 80000, 120000],
    "Purchased": [0, 0, 1, 1, 1, 1, 0, 0, 0, 1] # 0 = No, 1 = Yes
}
df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df[['Age', 'EstimatedSalary']]
y = df['Purchased']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("Data split into training and testing sets.")

print("\n--- 2. Training the Random Forest Model ---")
# Create the Random Forest model with 10 decision trees
model = RandomForestClassifier(n_estimators=10, random_state=42)

# Train the model
model.fit(X_train, y_train)
print("Model trained successfully!")

print("\n--- 3. Making Predictions & Evaluating ---")
# Predict on the test set
predictions = model.predict(X_test)
print(f"Predictions: {predictions}")
print(f"Actuals:     {y_test.values}")

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
