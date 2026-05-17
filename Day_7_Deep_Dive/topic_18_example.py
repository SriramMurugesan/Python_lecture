# topic_18_example.py
# Building, training, and evaluating our very first Machine Learning Model!

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Dataset: Does spending more money on Ads increase Sales?
data = {
    "Ad_Budget": [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000],
    "Sales": [150, 300, 450, 600, 750, 900, 1050, 1200]
}
df = pd.DataFrame(data)

# X (Features/Inputs) - Must be a 2D DataFrame (double brackets!)
X = df[["Ad_Budget"]]
# y (Target/Output) - Just a single Series
y = df["Sales"]

# We hold back 25% of the data for testing. random_state ensures we get the same split every time we run the file.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

print("Training data length (80%):", len(X_train))
print("Testing data length (20%):", len(X_test))

# Create the blank "brain"
model = LinearRegression()

# Tell the brain to study the training data and find the mathematical pattern
model.fit(X_train, y_train)
print("Model successfully trained!")

 # Give the model the hidden test inputs and ask it to guess the Sales!
predictions = model.predict(X_test)
print("The Model Guessed:", predictions)
print("The Actual Truth :", y_test.values)

# How far off was the model on average?
error = mean_absolute_error(y_test, predictions)
print(f"Mean Absolute Error (MAE): {error}")
print("If MAE is 0.0, the model is literally predicting the future perfectly!")

new_budget = pd.DataFrame({"Ad_Budget": [5500]})
new_predictions = model.predict(new_budget)
print("The Model Guessed for sales in 5500 budget:", new_predictions)