# 👨‍🏫 Instructor Lecture Notes: Day 7

## Topic 18: Linear Regression (Hands-On) (3 Hrs)
**1. Scikit-Learn (`sklearn`):**
- Introduce `scikit-learn` as the standard ML library in Python. It provides consistent, easy-to-use interfaces for hundreds of algorithms.
**2. Data Splitting (`train_test_split`):**
- *Concept:* If a student sees the exam questions before the test, getting 100% doesn't mean they are smart—it means they memorized it. ML models are the same.
- We must split our data into "Training" (to let the model learn) and "Testing" (to evaluate it on unseen data). Usually 80/20.
**3. Fitting and Predicting:**
- **Step 1:** Isolate Features (`X`, usually 2D DataFrame) and Target (`y`, usually 1D Series).
- **Step 2:** Initialize the model: `model = LinearRegression()`.
- **Step 3:** Fit the model: `model.fit(X_train, y_train)`. (The math happens here).
- **Step 4:** Predict: `predictions = model.predict(X_test)`.
**4. Evaluation Metrics:**
- **MSE (Mean Squared Error):** On average, how far off were our predictions? Lower is better.
- **R2 Score:** The percentage of variance explained by the model (0 to 1). 0.90 means the model is highly accurate. 

## Topic 19: Mini Project (3 Hrs)
**1. Execution of the Pipeline:**
- This is the grand finale. Students will take the `capstone_sales_data.csv` and apply everything from the past 7 days.
- **Walkthrough Steps for the Instructor to guide:**
  1. **Load:** Read the CSV using pandas.
  2. **Inspect & Clean:** Use `.isna().sum()`. Guide them to drop or fill the missing `Customer_Age` and `Sales` values.
  3. **EDA (Exploratory Data Analysis):** Run `.describe()` and `.corr()`. Ask the students: *"Which variable affects Sales the most?"* (They should see `Ads_Spend` is highly correlated).
  4. **Prepare:** Set `X = df[['Ads_Spend']]` and `y = df['Sales']`.
  5. **Split:** Run `train_test_split`.
  6. **Train:** Fit the `LinearRegression` model.
  7. **Evaluate:** Print the R2 score and MSE.
**2. Final Wrap-Up:**
- Show them `model.coef_` (the multiplier). Explain that this number literally tells the business: *"For every $1 spent on Ads, we generate $X in Sales."*
- Congratulate the students on going from basic variables to building a predictive Machine Learning model in just 7 days!
