# Topic 14: Understanding Errors

## Syntax vs. Runtime Errors
When programming, things will break. Understanding *why* it broke is the most important skill you can learn. There are two main types of errors:

1. **Syntax Errors**: Grammar mistakes. You forgot a quote `""`, a parenthesis `()`, or spelled a core Python keyword wrong.
   - **Result**: Python refuses to run the code at all. It crashes instantly before line 1 even executes.
2. **Runtime Errors**: The grammar is perfect, so Python starts running the code top-to-bottom. However, it hits an impossible situation and crashes during execution.
   - Example: Trying to divide a number by zero.
   - Example: Trying to open a file that doesn't exist on your computer.

## Reading the Traceback
When a program crashes, Python prints a **Traceback** (a block of red text) to the screen. 
- ALWAYS look at the very bottom line of the Traceback first. It tells you the exact Error Type (e.g., `ZeroDivisionError`, `NameError`).
- Then look slightly up to see the exact **Line Number** where the crash happened.

## Debugging Basics
Debugging is the process of hunting down bugs (errors).
- **The Print Strategy**: If your program crashes on Line 50, place `print("Made it to Line 20")` and `print("Made it to Line 40")` in your code. If "Line 20" prints but "Line 40" doesn't, you know exactly where the crash is happening!
