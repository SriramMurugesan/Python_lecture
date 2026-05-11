# Topic 16: Try/Except/Finally & Custom Exceptions

## Multiple Except Blocks
In the real world, a single block of code could crash for several different reasons. You can stack multiple `except` blocks together to handle each specific problem differently.
- Example: If a user types the word "Apple" instead of a number, that's a `ValueError`. If they try to divide by zero, that's a `ZeroDivisionError`. We can catch and handle both separately with their own unique error messages!

## The `finally` Block
The `finally` block is placed at the very bottom of a `try/except` chain. 
- **The Golden Rule**: The code inside `finally` will run 100% of the time, no matter what happens. Even if the program succeeds perfectly, or if it crashes horribly, `finally` will always execute.
- **Why use it?** It is mostly used for critical "cleanup" operations, like forcing a file to close or disconnecting from a database so you don't corrupt data.

## Custom Error Classes
Python has dozens of built-in errors, but sometimes you need to invent your own specific error for your strict business rules (e.g., `NegativeAgeError` or `InsufficientFundsError`).
To do this, we use the advanced `class` keyword to create our own custom Error that behaves exactly like a built-in Python Exception.
