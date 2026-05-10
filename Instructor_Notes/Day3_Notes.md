# 👨‍🏫 Instructor Lecture Notes: Day 3

## Topic 7: Lists (2 Hrs)
**1. What is a List?**
- A dynamic, mutable array that can hold mixed data types `[1, "Apple", True]`.
- *Analogy:* A train with connected cargo cars. You can add cars, remove cars, and change what's inside them.
**2. Creation, Indexing, & Slicing:**
- Works exactly identically to strings. Emphasize that learning slicing in strings pays off here.
- *Live Code:* `fruits = ["Apple", "Banana", "Cherry"]`. Show `fruits[1]`.
**3. Core Methods:**
- `.append(item)`: Adds to the very end.
- `.insert(index, item)`: Sneaks an item into a specific spot.
- `.remove(item)`: Removes the first occurrence of a value.
- `.pop(index)`: Removes and returns an item at an index (defaults to the last item).
- `.sort()`: Sorts the list in place.

## Topic 8: Dictionaries & Tuples (2 Hrs)
**1. Tuples:**
- Defined with parentheses `(1, 2, 3)`. 
- **Key difference from lists:** They are IMMUTABLE. You cannot append, remove, or change elements.
- *Why use them?* Memory efficiency, fixed coordinates (like GPS latitude/longitude), and returning multiple values from functions.
**2. Dictionaries:**
- Key-Value pairs. Defined with curly braces `{"key": "value"}`.
- *Analogy:* A real dictionary! The word is the "key", the definition is the "value". Keys must be unique and immutable (strings/integers).
- Fast O(1) lookups.
**3. Dictionary Operations:**
- Accessing: `student["name"]`.
- Using `.get()`: Teach them to use `student.get("age", "Not Found")` to avoid program-crashing `KeyErrors`.
- Iterating: `for key, value in student.items():`

## Topic 9: File Handling Basics (2 Hrs)
**1. The `open()` Function & File Modes:**
- Explain how data in variables vanishes when RAM clears (program stops). Files persist on the hard drive.
- **Modes:** 
  - `r` (Read): Errors if file doesn't exist.
  - `w` (Write): Overwrites the entire file. Creates if it doesn't exist.
  - `a` (Append): Adds to the bottom of the file.
**2. Working with Text Files:**
- Show traditional way: `f = open("data.txt", "w"); f.write("Hi"); f.close()`. Explain that forgetting `.close()` locks the file in the OS.
**3. The `with` Context Manager:**
- The modern, safe way to handle files.
- *Live Code:*
  ```python
  with open("log.txt", "a") as file:
      file.write("User logged in.\n")
  ```
- Explain that the `with` block automatically closes the file the moment the indentation ends, even if the program crashes inside the block!
