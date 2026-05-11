# Topic 18: Linear Regression (Hands-On)

## What is Scikit-Learn?
In the same way that Pandas is the ultimate tool for handling data tables, `scikit-learn` (imported in code as `sklearn`) is the absolute standard Python library for Machine Learning. It contains hundreds of pre-built ML mathematical models so you don't have to write the complex math yourself!

## The Machine Learning Workflow
To train a machine learning model properly, you must follow specific steps:

### 1. Separate Features (X) and Target (y)
- **Features (X)**: The inputs. The data the model uses to make a guess (e.g., Advertising Budget). By standard convention in the industry, `X` is always capitalized.
- **Target (y)**: The output. What you are trying to predict (e.g., Final Sales). `y` is always lowercase.

### 2. Train / Test Split
If you give the model 100% of your data to study, and then test it on that exact same data, it will cheat because it already memorized the answers! 
- We use the `train_test_split` tool to hide 20% of the data. The model studies the 80% (Training Data), and takes a test on the hidden 20% (Testing Data).

### 3. Fit and Predict
- `fit(X_train, y_train)`: This is where the actual Machine Learning happens. The computer analyzes the training data, does millions of math calculations, and finds the perfect Line of Best Fit.
- `predict(X_test)`: The model is given the hidden test inputs and forced to guess the answers!

### 4. Evaluation Metrics
How do we know if the model is smart or stupid?
- **Mean Absolute Error (MAE)**: On average, how far off was the model's guess from the actual truth? If the MAE is 5, it means the model's predictions are usually off by exactly 5 points.
