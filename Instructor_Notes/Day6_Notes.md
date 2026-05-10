# 👨‍🏫 Instructor Lecture Notes: Day 6

## Topic 16: Try/Except/Finally + Custom Exceptions (3 Hrs)
**1. The `try / except` Block:**
- Put "risky" code inside the `try` block. If an error is thrown, the `except` block catches it like a safety net, allowing the program to continue running.
- **Multiple Except Blocks:** Show how to handle different errors differently.
  ```python
  try:
      num = int(input("Enter number: "))
      print(10 / num)
  except ValueError:
      print("That's not a number!")
  except ZeroDivisionError:
      print("Can't divide by zero!")
  ```
**2. The `finally` Block:**
- Code in the `finally` block executes **no matter what**—whether an error occurred or not.
- *Use case:* Closing files, closing database connections, or releasing network sockets.
**3. Custom Exceptions:**
- Show how to create bespoke errors tailored to business logic by subclassing the base `Exception` class.
- *Live Code:* `class AgeRestrictionError(Exception): pass`.

## Topic 17: Regression & Correlation Concepts (3 Hrs)
*(Instructor Note: Keep math light. Focus on visual and logical intuition).*
**1. Relationships Between Variables:**
- Give real-world examples: Temperature vs Ice Cream Sales (Positive), Age of Car vs Price of Car (Negative).
**2. Correlation Matrix:**
- Correlation is a number between -1 and 1. 
  - `1` = Perfect positive correlation.
  - `-1` = Perfect negative correlation.
  - `0` = No correlation (scattered randomly).
- *Live Code:* `df.corr()`. Show how the diagonal is always 1.0 because a variable correlates perfectly with itself.
- **CRITICAL RULE:** Correlation does NOT imply causation. (e.g., Ice cream sales and shark attacks correlate because of Summer, not because ice cream attracts sharks).
**3. Regression Theory (Intuition):**
- If we know two variables are correlated, can we *predict* one using the other? Yes!
- Explain linear regression as drawing a "Line of Best Fit" through a scatter plot.
- The algorithm calculates the line that minimizes the "residuals" (the distance between the actual data points and the line). Equation: `y = mx + b`.
