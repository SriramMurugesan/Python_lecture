# topic_21_example.py
# Using Support Vector Machine (SVM) for Classification
# What is Support Vector Machine (SVM)?
# Support Vector Machine (SVM) is a supervised machine learning algorithm used for classification and regression tasks. It works by finding the optimal hyperplane that separates the data points into different classes.
# why do we use SVM for classification?
# SVM is used for classification tasks because it is a robust algorithm that can handle large datasets and high-dimensional data. It is also less prone to overfitting than other algorithms.
# difference between SVM and Random Forest Classification:
# SVM is a supervised machine learning algorithm used for classification and regression tasks. It works by finding the optimal hyperplane that separates the data points into different classes. Random Forest Classification is a supervised machine learning algorithm used for classification tasks. It works by creating multiple decision trees during training and combining their predictions to make a final prediction.

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

print("--- 1. Preparing the Data ---")
# Mock dataset: predicting if an engine part is Defective (1) or Normal (0)
# based on its Temperature and Vibration levels.
data = {
    "Temperature": [70, 72, 71, 95, 100, 98, 65, 68, 105, 110],
    "Vibration": [1.2, 1.3, 1.1, 4.5, 5.0, 4.8, 1.0, 1.4, 5.5, 6.0],
    "Defective": [0, 0, 0, 1, 1, 1, 0, 0, 1, 1]
}
df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df[['Temperature', 'Vibration']]
y = df['Defective']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("Data split into training and testing sets.")

print("\n--- 2. Training the SVM Model ---")
# Create the SVM model. We'll use a simple linear kernel.
model = SVC(kernel='linear')

# Train the model
model.fit(X_train, y_train)
print("SVM Model trained successfully!")

print("\n--- 3. Making Predictions & Evaluating ---")
# Predict on the test set
predictions = model.predict(X_test)
print(f"Predictions: {predictions}")
print(f"Actuals:     {y_test.values}")

# Calculate accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

print("\nDetailed Classification Report:")
print(classification_report(y_test, predictions))
