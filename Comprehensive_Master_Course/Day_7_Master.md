# 📘 Day 7: Machine Learning & Capstone (6 Hours)
*(Note: ML section instruction — Focus on intuition, show workflow clearly).*

## 🕒 Topic 18: Linear Regression (Hands-On) (3 Hours)
### 🎯 Learning Outcome
Build, train, evaluate, and interpret a real linear regression Machine Learning model.

### 🌍 Real Problem
You have historical data on houses (Square footage vs. Sale Price). A client wants to list their house today. You need a mathematical model that accurately predicts their optimal sale price based on the historical trend.

### 🧠 Concept Explanation *(Workflow Focus)*
* **Scikit-learn (`sklearn`):** The industry standard ML library.
* **Train / Test Split:** We must hide 20% of the data from the model during training. If we test it on the exact same data it learned from, it's just memorization, not intelligence.
* **Fitting (`model.fit`):** The algorithm crunching the numbers to find the line of best fit.
* **Predicting (`model.predict`):** Asking the model to guess outcomes on the hidden test data.
* **Evaluation:** 
  * **MSE (Mean Squared Error):** Average error distance. Lower is better.
  * **R2 Score:** Accuracy percentage (0 to 1). 0.90 is fantastic.

### 💻 Live Code Example
```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import numpy as np

# 1. Prepare Data (Features X must be 2D)
X = np.array([[1], [2], [3], [4]]) 
y = np.array([2, 4, 6, 8])

# 2. Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# 3. Train
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Predict & Evaluate
preds = model.predict(X_test)
print(f"R2 Score: {r2_score(y_test, preds)}")
```

### 🐞 Debugging Requirement
**Broken Code:**
```python
X = [1, 2, 3, 4]
y = [2, 4, 6, 8]
model = LinearRegression()
model.fit(X, y)
```
**Task:** Explain the `ValueError`.
**Errors Explained:** `scikit-learn` strictly expects a 2-Dimensional structure for Features `X` (like a DataFrame or nested list `[[1], [2]]`). A flat 1D list causes a crash.

### ⚠️ Common Mistakes
* **Mistake:** Evaluating the model's accuracy on the exact same `X_train` data it was trained on.
* **Why it occurs:** Misunderstanding the purpose of the split. Testing on training data yields artificially high accuracy.

### 📝 Practice Requirements
**Easy (3):**
1. Import `LinearRegression` and initialize the model object.
2. Perform a standard 80/20 train/test split on dummy data.
3. Make a single prediction using a pre-trained model.
**Medium (3):**
1. Reshape a flat 1D list into a 2D array using NumPy to satisfy sklearn.
2. Calculate the R-squared score between actual and predicted test values.
3. Print the model's computed coefficient and intercept.
**Challenging (2):**
1. Perform multiple linear regression (using two or more feature columns simultaneously).
2. Compare the MSE of two different models built using different feature sets to see which performs better.

---

## 🕒 Topic 19: Capstone Mini Project (3 Hours)
### 🎯 Learning Outcome
Apply the full end-to-end data science pipeline: Data loading, cleaning, EDA, regression modeling, evaluation, and reporting.

### 🌍 Real Problem
Act as a Junior Data Scientist. The company handed you a messy, raw CSV file of regional sales data. You must clean it, figure out what drives sales, and build a predictive model to forecast next quarter's revenue.

### 🧠 Concept Explanation *(Pipeline Integration)*
This project integrates everything learned over the 7 days:
1. **File Handling / Pandas:** Load the CSV.
2. **Data Manipulation:** Fix NaNs, drop bad columns.
3. **Control Flow / Exceptions:** Handle string formatting errors.
4. **EDA:** Run correlation matrix, grouping.
5. **Machine Learning:** Split, Train, Predict, Evaluate.

### 💻 Live Code Workflow 
*(Instructor Note: Guide students through this flow using the generated dataset).*
```python
# 1. Load
df = pd.read_csv("capstone_sales_data.csv")
# 2. Clean
df = df.dropna(subset=['Sales']) 
# 3. Features & Target
X = df[['Ads_Spend']]
y = df['Sales']
# 4. Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 5. Model
model = LinearRegression().fit(X_train, y_train)
# 6. Report
print(f"R2 Score: {model.score(X_test, y_test)}")
```

### 🐞 Debugging Requirement
**Broken Workflow:**
The model is trained, and the R2 score comes out to exactly `1.0` (100% perfect prediction). 
**Task:** Why should the Data Scientist panic?
**Errors Explained:** Data Leakage. The target variable (`Sales`) was accidentally included in the Feature set (`X`). The model simply learned that "Sales equals Sales". The target must ALWAYS be dropped from `X`.

### ⚠️ Common Mistakes
* **Mistake:** Skipping Exploratory Data Analysis (EDA).
* **Why it occurs:** Rushing straight to ML. If you don't run `.corr()` first, you might train a model on totally unrelated garbage variables (like `Customer_Age` predicting `Sales`).

### 📝 Practice Requirements
**Easy (3):**
1. Load the final CSV dataset and run `.info()`.
2. Identify the target variable.
3. Drop missing values safely.
**Medium (3):**
1. Run a correlation matrix to identify the most important predictive feature.
2. Run the `train_test_split` with a randomized state.
3. Write a custom function to clean specific string formatting inside the DataFrame if necessary.
**Challenging (2):**
1. Execute the entire pipeline end-to-end without a single error.
2. Write a brief executive summary using Python `f-strings` to present the final model metrics cleanly to non-technical stakeholders.
