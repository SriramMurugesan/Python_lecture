# 📘 Day 2: Control Flow & Text Processing (6 Hours)

## 🕒 Topic 4: String Operations (2 Hours)
### 🎯 Learning Outcome
Manipulate, slice, and format text data efficiently.

### 🌍 Real Problem
You have a database of thousands of raw email addresses (e.g., `user.name@domain.com`). You need to write a script that automatically extracts just the username to personalize a welcome message.

### 🧠 Concept Explanation
* **Indexing:** Strings are arrays of characters. `[0]` is the first, `[-1]` is the last.
* **Slicing:** `[start : stop : step]`. The stop index is exclusive.
* **Methods:** `.upper()`, `.replace()`, `.split()`.
* **Formatting:** `f-strings` inject variables seamlessly into text.

### 💻 Live Code Example
```python
email = "admin@company.com"
username = email[:email.index("@")]
print(f"Welcome, {username.capitalize()}!")
```

### 🐞 Debugging Requirement
**Broken Code:**
```python
name = "python"
name[0] = "P"
```
**Task:** Why doesn't this capitalize the word?
**Errors Explained:** `TypeError`. Strings are *immutable* in Python; you cannot change characters in place. Use `name = name.capitalize()`.

### ⚠️ Common Mistakes
* **Mistake:** Off-by-one errors in slicing (e.g., stopping one character too early).
* **Why it occurs:** Forgetting that Python slicing is exclusive on the right side (`[0:3]` gets indexes 0, 1, 2).

### 📝 Practice Requirements
**Easy (3):**
1. Print the first and last character of a string.
2. Convert a lowercase string to uppercase.
3. Replace the word "bad" with "good" in a sentence.
**Medium (3):**
1. Reverse a string using slicing.
2. Extract the domain (after the @) from an email URL.
3. Count the occurrences of the letter 'a' in a paragraph.
**Challenging (2):**
1. Write a script to check if a string is a palindrome.
2. Mask the first 12 digits of a 16-digit credit card number (e.g., `****-****-****-1234`).

---

## 🕒 Topic 5: Input/Output Functions (2 Hours)
### 🎯 Learning Outcome
Build interactive programs using `input()` and advanced `print()` formatting.

### 🌍 Real Problem
You are building a customized checkout terminal for a coffee shop. The barista needs to type in the order amount, and the screen needs to output the total with tax formatted strictly to two decimal places.

### 🧠 Concept Explanation
* **`input()`:** Pauses the program to get user text. **Always returns a string.**
* **`print()`:** Outputting to terminal. Advanced arguments include `sep` (separator) and `end` (ending character).
* **Formatting Specifiers:** Using `:.2f` to force floats to look like currency.

### 💻 Live Code Example
```python
name = input("Enter name: ")
salary = float(input("Enter salary: "))
print("User", name, sep=" -> ")
print(f"Formatted salary: ${salary:,.2f}")
```

### 🐞 Debugging Requirement
**Broken Code:**
```python
age = input("Age: ")
print("In 5 years, you will be:", age + 5)
```
**Task:** Why does this crash when the user types a number?
**Errors Explained:** `TypeError`. Even if the user types `20`, `input()` sees it as `"20"`. You must cast it: `int(input())`.

### ⚠️ Common Mistakes
* **Mistake:** Printing with the `+` operator and crashing on integers (`print("Age: " + 25)`).
* **Why it occurs:** `+` tries to concatenate mathematically instead of joining text. Using commas or f-strings is safer.

### 📝 Practice Requirements
**Easy (3):**
1. Ask for a name and print a personalized greeting.
2. Take two numbers as input, add them, and print the result.
3. Print three distinct words separated by hyphens using the `sep` argument.
**Medium (3):**
1. Build a calculator that takes two numbers and prints their sum, difference, and product.
2. Take a long float input and format it to exactly 3 decimal places.
3. Ask the user for their birth year and calculate their current age.
**Challenging (2):**
1. Build an interactive restaurant tip calculator.
2. Create a receipt printer that automatically aligns item names to the left and prices to the right.

---

## 🕒 Topic 6: Loops in Python (2 Hours)
### 🎯 Learning Outcome
Solve repetitive logic problems using `for` and `while` loops, and understand nested loops.

### 🌍 Real Problem
A marketing team needs to send 1,000 customized reminder emails. Writing 1,000 individual `send_email()` functions is impossible. We need a loop to automate the repetition.

### 🧠 Concept Explanation
* **`for` loops:** Used when you know the exact number of iterations (e.g., looping through a sequence or `range()`).
* **`while` loops:** Used when you want to loop *until a condition becomes false*.
* **Control:** `break` stops the loop immediately. `continue` skips to the next iteration.
* **Integration:** Combining strings, conditions, and loops.

### 💻 Live Code Example
```python
for i in range(1, 4):
    print(f"Attempt {i}...")

text = "pYthOn"
for char in text:
    if char.isupper():
        print(f"Uppercase found: {char}")
```

### 🐞 Debugging Requirement
**Broken Code:**
```python
count = 5
while count > 0:
    print(count)
```
**Task:** Why does this script freeze the computer?
**Errors Explained:** Infinite loop. The condition `count > 0` is always true because `count` is never decreased. Must add `count -= 1`.

### ⚠️ Common Mistakes
* **Mistake:** Using `while` when a `for` loop is much safer.
* **Why it occurs:** Beginners forget to increment their counter variables in `while` loops. `for` loops handle the incrementing automatically.

### 📝 Practice Requirements
**Easy (3):**
1. Print numbers 1 to 10 using a `for` loop.
2. Print even numbers from 2 to 20 using a `while` loop.
3. Loop through a string and print each character on a new line.
**Medium (3):**
1. Calculate the factorial of a user-input number using a loop.
2. Print the multiplication table of a given number.
3. Loop through a string; use `break` to stop completely if the letter 'x' is found.
**Challenging (2):**
1. Print a right-angled triangle pattern of stars using nested loops.
2. Build a guess-the-number game with a `while` loop, giving the user a maximum of 3 attempts.
