# Topic 15: Exceptions in Python

## What are Exceptions?
An Exception is Python's advanced way of dealing with a Runtime Error. Instead of letting the entire program crash and burn, you can "catch" the error safely and tell Python exactly what to do instead.

## The Try / Except Block
You can wrap highly dangerous code (like opening a file, or taking random user input) inside an indented `try` block. If the code crashes, Python immediately jumps to the indented `except` block instead of destroying the program.

```python
try:
    # Try to do something dangerous
    number = 10 / 0
except:
    # If it crashes, run this safely!
    print("Oops! Something went wrong.")
```

## Built-in Exceptions
It is best practice to catch *specific* errors, rather than a general "Oops". 
- `ValueError`: Raised when an operation receives the right type of data, but an inappropriate value (like trying to convert the text word "Apple" into an integer).
- `ZeroDivisionError`: Raised when mathematically dividing by zero.
- `TypeError`: Raised when mixing incompatible types (like adding text and a number).
- `KeyError`: Raised when you try to access a key in a Dictionary that doesn't exist.

## Raising Exceptions
You can intentionally crash your own program if the user does something you don't allow. You do this using the `raise` keyword.
- Why? It acts as a strict security guard, preventing bad data (like negative ages) from moving deeper into your secure code.
