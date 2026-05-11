# The Ultimate Consolidated Project: House Price Predictor AI
# This single script uses EVERYTHING learned from Day 1 to Day 7.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

print("=== PART 1: Python Basics & Data Structures ===")
# 1. Variables, Strings, and Lists
app_name = "Real Estate AI Predictor"
print(f"Welcome to the {app_name.upper()}!")

# Creating a list of dictionaries to hold raw property data
properties = [
    {"Square_Feet": 1500, "Bedrooms": 3, "Price": 300000},
    {"Square_Feet": 2000, "Bedrooms": 4, "Price": 400000},
    {"Square_Feet": 1200, "Bedrooms": 2, "Price": 250000},
    {"Square_Feet": 2500, "Bedrooms": 4, "Price": 500000},
    {"Square_Feet": 1800, "Bedrooms": 3, "Price": None}, # Missing data!
    {"Square_Feet": 2200, "Bedrooms": 4, "Price": 450000},
    {"Square_Feet": 1600, "Bedrooms": 3, "Price": 320000},
    {"Square_Feet": 2800, "Bedrooms": 5, "Price": 550000}
]

print("\n=== PART 2: Loops & File Handling ===")
# Let's save this raw data into a CSV file manually to practice file handling!
print("Saving raw property data to 'raw_houses.csv'...")

with open("raw_houses.csv", "w") as file:
    # Write the header row
    file.write("Square_Feet,Bedrooms,Price\n")
    
    # Loop through the list of dictionaries and write each row
    for prop in properties:
        # We must cast numbers to strings to write them to a text file
        sqft = str(prop["Square_Feet"])
        beds = str(prop["Bedrooms"])
        price = str(prop["Price"])
        file.write(f"{sqft},{beds},{price}\n")
        
print("File successfully created and saved!")

print("\n=== PART 3: Pandas & Error Handling ===")
# Now we load the CSV back into a Pandas DataFrame
df = pd.read_csv("raw_houses.csv")

print("Original Messy Data:")
print(df)

# Let's try to do something dangerous and catch the error safely
try:
    print("\nAttempting to find the average 'Pool_Size'...")
    # This column doesn't exist, so it will throw a KeyError!
    avg_pool = df["Pool_Size"].mean()
except KeyError:
    print("ERROR CAUGHT: 'Pool_Size' column does not exist! Proceeding safely...")

print("\n=== PART 4: Data Cleaning & Correlation ===")
# The ML model will completely crash if it sees NaN (missing prices). Let's fill it with the average price!
average_price = df["Price"].mean()
df["Price"] = df["Price"].fillna(average_price)
print("Missing prices cleanly filled with the average value:", average_price)

print("\nCorrelation Matrix (Proving size completely affects price):")
print(df.corr())

print("\n=== PART 5: Machine Learning (Linear Regression) ===")
# 1. Define Features (X) and Target (y)
X = df[["Square_Feet", "Bedrooms"]]
y = df["Price"]

# 2. Train / Test Split (Keeping 25% hidden for the final test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 3. Create and Train the Model
model = LinearRegression()
model.fit(X_train, y_train)
print("AI Model successfully trained on historical house data!")

# 4. Evaluate the Model
predictions = model.predict(X_test)
error = mean_absolute_error(y_test, predictions)
print(f"Model Accuracy Check: The AI is off by an average of ${error:,.2f} per house.")

print("\n=== PART 6: Predicting the Future! ===")
# A user wants to know how much a brand new 2,400 sqft, 4-bedroom house should cost
new_house = pd.DataFrame({"Square_Feet": [2400], "Bedrooms": [4]})
predicted_price = model.predict(new_house)

print(f"*** FINAL PREDICTION ***")
print(f"A 2,400 sqft house with 4 bedrooms should be priced at roughly: ${predicted_price[0]:,.2f}!")
