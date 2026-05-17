# Topic 20: Random Forest Algorithm

## What is a Random Forest?
Random Forest is a popular and powerful supervised Machine Learning algorithm used for both classification and regression tasks. As the name suggests, it creates a "forest" of many individual Decision Trees and combines their predictions.

## How does it work?
Instead of relying on a single decision tree (which might overfit and memorize the data), Random Forest builds multiple trees. 
- Each tree looks at a random subset of the data and a random subset of features.
- To make a prediction, each individual tree "votes" on the outcome.
- The forest takes the majority vote (for classification) or the average (for regression).

This concept of combining multiple weak models to create a strong one is called **Ensemble Learning**.

## Advantages
- Highly accurate and robust.
- Reduces the risk of overfitting compared to a single decision tree.
- Can handle missing values and maintain accuracy.

## Using Random Forest in Scikit-Learn
You can import the `RandomForestClassifier` or `RandomForestRegressor` from `sklearn.ensemble`.
