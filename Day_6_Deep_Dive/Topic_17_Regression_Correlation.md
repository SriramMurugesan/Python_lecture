# Topic 17: Regression & Correlation Concepts

## What is Correlation?
Correlation is a statistical measurement that describes how two variables move in relation to each other.
- **Positive Correlation**: If one goes up, the other goes up. (Example: More hours studying usually means higher Test Scores).
- **Negative Correlation**: If one goes up, the other goes down. (Example: As the age of a car goes up, its price goes down).
- **No Correlation**: The variables have absolutely nothing to do with each other.

## The Correlation Matrix
In Pandas, you can instantly see how every single column in your table relates to every other column using the `.corr()` method.
- A score of **1.0** means a perfect positive match.
- A score of **-1.0** means a perfect negative match.
- A score near **0.0** means there is zero mathematical relationship.

## Regression Theory (The Foundation of Machine Learning)
Correlation tells us IF a relationship exists. **Regression** tells us exactly WHAT that relationship is mathematically, so we can predict the future.
- **Line of Best Fit**: Regression works by drawing a mathematical straight line right through the middle of a scatter plot of your data points.
- **Prediction**: Once the computer finds the perfect line, you can plug in a brand new "X" value (like a massive Advertising Budget), and the line will automatically predict the "Y" value (Expected Sales). This is the exact foundation of Machine Learning!
