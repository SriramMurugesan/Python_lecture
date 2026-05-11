# topic_19_example.py
# FINAL MINI PROJECT: Student Performance Analyzer (The Full AI Pipeline)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

print("=== STEP 1: Data Loading ===")
# Raw, slightly messy data from a school district
raw_data = {
    "Hours_Studied": [2, 3, 5, 1, 8, 4, 6, 9, 3, 7],
    "Previous_Score": [65, 70, 80, 50, 95, 75, 85, 98, None, 90], # One student is missing their previous score!
    "Final_Score": [68, 73, 85, 52, 98, 78, 88, 99, 74, 94]
}
df = pd.DataFrame(raw_data)
print("Raw Data Loaded successfully. Total Students:", len(df))

print("\n=== STEP 2: Data Cleaning ===")
# Machine Learning will crash if it sees 'None' (NaN).
# We must fill the missing 'Previous_Score' with the class average.
average_previous = df["Previous_Score"].mean()
df["Previous_Score"] = df["Previous_Score"].fillna(average_previous)
print("Missing values filled with the average score:", average_previous)

print("\n=== STEP 3: Exploratory Data Analysis (EDA) ===")
# Let's prove scientifically that Hours_Studied actually relates to Final_Score
print("Correlation Matrix:")
print(df.corr())
print("Notice the massive positive correlation between Hours_Studied and Final_Score!")

print("\n=== STEP 4: Model Training ===")
# Define Inputs (X) - We use TWO features now!
X = df[["Hours_Studied", "Previous_Score"]]
# Define Output (y)
y = df["Final_Score"]

# Split the data (80% for studying, 20% for taking the test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the AI brain
ai_model = LinearRegression()
ai_model.fit(X_train, y_train)
print("AI Model successfully trained on the historical data!")

print("\n=== STEP 5: Evaluation and Reporting ===")
# Force the AI to take a test on the hidden 20% data
predictions = ai_model.predict(X_test)

# Calculate how far off the AI's guesses were
error = mean_absolute_error(y_test, predictions)
print(f"Model Error Margin (MAE): {error:.2f} points off on average.")

print("\n=== BONUS: PREDICTING THE FUTURE ===")
# A brand new student walks in. They studied for 5 hours and their previous score was 75.
# Let's ask the AI to predict their final exam score!
new_student = pd.DataFrame({"Hours_Studied": [5], "Previous_Score": [75]})
future_prediction = ai_model.predict(new_student)

print(f"Based on historical data, the AI predicts this new student will score: {future_prediction[0]:.2f} on the Final!")
