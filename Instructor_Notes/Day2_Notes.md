# 👨‍🏫 Instructor Lecture Notes: Day 2

## Topic 4: String Operations (2 Hrs)
**1. What is a String?**
- Strings are immutable arrays (sequences) of characters. Once created, they cannot be changed in place.
**2. Indexing & Slicing:**
- Python is 0-indexed. The first character is `[0]`.
- Negative indexing exists! `[-1]` is the very last character.
- **Slicing Syntax:** `[start : stop : step]`. *Crucial note:* The `stop` index is exclusive.
- *Live Code:* `word = "Python"`. `word[0:3]` returns `"Pyt"`. `word[::-1]` reverses the string.
**3. String Methods:**
- Methods are built-in functions specific to strings.
- Show: `.upper()`, `.lower()`, `.replace("old", "new")`, `.split(",")` (turns a string into a list), `.strip()` (removes whitespace).
**4. Formatting:**
- Explain **f-strings** (formatted string literals). They are the modern, clean way to inject variables into text.
- *Live Code:* `name = "John"; print(f"Hello {name}")`.

## Topic 5: Input/Output Functions (2 Hrs)
**1. `input()` Function:**
- How to pause the program and wait for the user.
- **CRITICAL:** `input()` ALWAYS returns a string. If you want a number, you must cast it immediately: `age = int(input("Age: "))`.
**2. Advanced `print()`:**
- Teach the `sep` (separator) and `end` arguments.
- *Live Code:* `print("Apple", "Banana", sep=" | ")`
- *Live Code:* `print("Loading...", end="")` (prevents the newline character).
**3. Formatting Specifiers:**
- How to make numbers look pretty (e.g., money).
- *Live Code:* `price = 12.3456; print(f"Price: ${price:.2f}")` -> `$12.35`.

## Topic 6: Loops in Python (2 Hrs)
**1. `for` Loops:**
- Used when you know exactly how many times you want to iterate, or when iterating over a collection (like a string or list).
- *Live Code:* `for i in range(5): print(i)` (Explain that `range(5)` goes 0 to 4).
- Iterating over a string: `for letter in "Python": print(letter)`.
**2. `while` Loops:**
- Used when you want to loop *until a condition becomes false*.
- *Analogy:* "Keep pumping gas WHILE the tank is not full."
- Warn them about infinite loops! Always ensure the condition will eventually update.
**3. Loop Control:**
- `break`: Smashes out of the loop completely.
- `continue`: Skips the rest of the current iteration and goes to the next one.
**4. Nested Loops:**
- A loop inside a loop. Used for grids, matrices, or 2D patterns.
- *Live Code:* Create a 3x3 grid of stars using a nested `for` loop.
