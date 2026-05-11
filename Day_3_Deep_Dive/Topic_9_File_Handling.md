# Topic 9: File Handling Basics

## Why do we need File Handling?
When your Python program finishes running, all the variables, lists, and data inside it are destroyed. If you want to save data permanently (like saving high scores, logs, or user details), you must save it to an external file on your hard drive.

## The `open()` Function
To work with a file, you first need to open it.
- `file = open("filename.txt", "mode")`

### The 3 Main File Modes
- `"r"` (Read): Opens a file just for reading. (The program will crash if the file does not exist).
- `"w"` (Write): Opens a file for writing. **WARNING**: This completely overwrites and destroys any existing text in the file! If the file doesn't exist, Python will create it.
- `"a"` (Append): Opens a file to safely add new text to the very end. It does not erase the old text.

## Best Practice: The `with` Block
When you open a file, you absolutely MUST close it when you are done using `file.close()`. If you forget, the file might get corrupted or stay locked by your operating system. 
To completely prevent this mistake, Python programmers use the `with` block. It automatically and safely closes the file for you as soon as the indented block of code is finished!

```python
with open("data.txt", "w") as file:
    file.write("Hello World!")
# The file is safely and automatically closed right here!
```

## Reading Methods
- `read()`: Reads the entire file as one giant string of text.
- `readline()`: Reads a single line at a time.
- `readlines()`: Reads all lines and puts them into a Python List, where each item is a line of text.
