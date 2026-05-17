# Topic 21: Support Vector Machine (SVM)

## What is SVM?
Support Vector Machine (SVM) is a powerful supervised Machine Learning algorithm primarily used for classification problems (though it can be used for regression as well). 

## How does it work?
The goal of SVM is to find the best "line" or "hyperplane" that divides your dataset into classes. 
Imagine plotting your data points on a graph. SVM tries to draw a boundary that not only separates the different classes but does so with the **maximum margin** (the largest possible gap) between the boundary and the closest data points from each class. 
These closest data points are called the **Support Vectors**.

## Advantages
- Very effective in high dimensional spaces (where you have many features).
- Memory efficient because it only uses a subset of training points (the support vectors) to build the decision boundary.
- Versatile through the use of different "Kernel functions" to separate data that is not linearly separable.

## Using SVM in Scikit-Learn
You can import `SVC` (Support Vector Classification) from the `sklearn.svm` module.
