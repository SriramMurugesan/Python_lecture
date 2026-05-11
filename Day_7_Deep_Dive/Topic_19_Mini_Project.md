# Topic 19: Mini Project (Full ML Workflow)

## The Grand Finale
Over the last 6 days, you have learned variables, loops, data manipulation with Pandas, and machine learning with Scikit-Learn. Now, we put it all together into a real, professional Machine Learning Pipeline.

## The Professional ML Workflow
Every single Data Scientist and AI Engineer follows these exact 5 steps when building a project:

1. **Data Loading**: Getting the raw data into Python (usually from a CSV via Pandas).
2. **Data Cleaning**: The most important step. Finding missing values (`NaN`) and filling them with logical replacements (like the average/mean) so the ML model doesn't crash.
3. **Exploratory Data Analysis (EDA)**: Looking at `.describe()` and the Correlation Matrix `.corr()` to prove scientifically that our variables actually relate to each other.
4. **Model Training**: Splitting the clean data into Train and Test sets, defining Features (`X`) and Targets (`y`), and fitting a `LinearRegression` model.
5. **Evaluation and Reporting**: Calculating the error (MAE), reporting the accuracy, and using the finished model to make a brand new prediction for the future!

## Your Project: The Student Performance Analyzer
In the accompanying Python file, you will step through this exact workflow to build an AI that predicts a student's final exam score based on how many hours they studied and what their past grades were.
