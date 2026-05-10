# 👨‍🏫 Instructor Lecture Notes: Day 1

## Topic 1: Introduction to Python (2 Hrs)
**1. What is Python?**
- Explain that Python is a high-level, interpreted programming language created in 1991. 
- *Analogy to use:* Explain "interpreted" like a real-time language translator who translates sentence-by-sentence, whereas "compiled" (like C++) translates the whole book before you can read it.
**2. Key Features:**
- **Readability:** Looks almost like plain English.
- **Dynamically Typed:** You don't have to declare variable types (e.g., no need for `int x = 5`).
- **Huge Ecosystem:** Libraries for everything from web to AI.
**3. Real-World Applications:**
- Data Science/ML (Pandas, TensorFlow), Web Development (Django, Flask), Automation, and Finance.

## Topic 2: Python Installation & Setup (2 Hrs)
**1. Installation Basics:**
- Show the python.org website. **CRITICAL:** Remind Windows users to check the "Add Python to PATH" box during installation.
- Explain what PATH is (how the terminal knows where Python lives).
**2. IDEs (Integrated Development Environments):**
- Explain the difference between a standard text editor and an IDE.
- *VS Code:* Best for building full applications, scripts, and general-purpose coding.
- *Jupyter Notebook:* Best for data science. Explain the "cell-by-cell" execution model which allows for quick data visualization.
**3. Running Scripts:**
- Create a file named `hello.py`. Write `print("Hello World")`.
- Open the terminal, navigate to the folder, and execute `python hello.py`. Explain how the terminal communicates with the Python interpreter.

## Topic 3: Variables, Data Types & Operators (2 Hrs)
**1. Variables:**
- *Analogy to use:* A variable is a named storage box in the computer's memory.
- Naming rules: No spaces, cannot start with a number, case-sensitive.
**2. Core Data Types:**
- `int` (Integer): Whole numbers (`age = 25`)
- `float` (Float): Decimal numbers (`price = 19.99`)
- `bool` (Boolean): True or False (`is_active = True`)
- `str` (String): Text enclosed in quotes (`name = "Alice"`)
- *Show the `type()` function* to let students check variable types dynamically.
**3. Operators:**
- **Arithmetic:** `+`, `-`, `*`, `/` (normal division), `//` (integer division - removes decimals), `%` (modulo - returns the remainder).
- *Live Example:* Ask the class what `10 % 3` is. Explain it's 1 because 3 goes into 10 three times with 1 left over.
- **Relational/Logical:** `==`, `>`, `<`, `and`, `or`, `not`.
**4. Type Casting:**
- Explain why `"10" + 5` causes an error. Python doesn't know if you want `"105"` or `15`.
- *Live Code:* Show `int("10") + 5` and `str(10) + "5"`.
