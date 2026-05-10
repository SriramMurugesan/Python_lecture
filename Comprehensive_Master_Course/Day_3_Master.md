# 📘 Day 3: Data Structures & File Handling (6 Hours)

## 🕒 Topic 7: Lists (2 Hours)
### 🎯 Learning Outcome
Store, process, and manipulate collections of data using lists.

### 🌍 Real Problem
Managing a dynamic shopping cart on an e-commerce site. Items need to be appended when a user clicks "Add to Cart", removed if they change their mind, and sorted by price.

### 🧠 Concept Explanation
* **Creation:** Defined using square brackets `[1, 2, "apple"]`.
* **Indexing/Slicing:** Works identically to strings.
* **Methods:** `.append()` (add to end), `.insert()` (add at index), `.remove()` (delete by value), `.pop()` (delete by index), `.sort()`.
* **Integration:** Using `for` loops to iterate over lists.

### 💻 Live Code Example
```python
cart = ["apple", "banana"]
cart.append("orange")
cart.remove("banana")
for item in cart:
    print(f"To buy: {item}")
```

### 🐞 Debugging Requirement
**Broken Code:**
```python
nums = [10, 20, 30]
print(nums[3])
```
**Task:** Why does this throw an error when there are clearly 3 items?
**Errors Explained:** `IndexError`. Python lists are 0-indexed. The elements are at 0, 1, and 2. Index 3 is out of bounds.

### ⚠️ Common Mistakes
* **Mistake:** Modifying a list (like removing items) while actively looping over it.
* **Why it occurs:** As items shift indices upon removal, the loop skips the next element.

### 📝 Practice Requirements
**Easy (3):**
1. Create a list of 5 fruits and print the 3rd one.
2. Add a new fruit to the end of the list.
3. Sort a list of random numbers.
**Medium (3):**
1. Find the largest and smallest number in a list without using built-in `max/min`.
2. Remove all duplicates from a list using a loop.
3. Reverse a list in place.
**Challenging (2):**
1. Write a program to find the second largest number in a list.
2. Flatten a 2D list (e.g., `[[1,2], [3,4]]` to `[1,2,3,4]`).

---

## 🕒 Topic 8: Dictionaries & Tuples (2 Hours)
### 🎯 Learning Outcome
Work with structured, relational data mapping (dicts) and immutable sequences (tuples).

### 🌍 Real Problem
Storing an employee directory. A list is bad because you have to loop through thousands of names to find an ID. A dictionary allows instant O(1) lookups using an Employee ID as the key.

### 🧠 Concept Explanation
* **Tuples:** Defined with `()`. Immutable lists. Good for fixed data like GPS coordinates.
* **Dictionaries:** Defined with `{}`. Key-Value pairs. Keys must be unique.
* **Operations:** `.keys()`, `.values()`, `.items()`. Using `.get()` to avoid crashes.

### 💻 Live Code Example
```python
coords = (10.5, 20.2) # Tuple

student = {"name": "John", "age": 20}
student["grade"] = "A" # Adding a new key
for key, val in student.items():
    print(f"{key}: {val}")
```

### 🐞 Debugging Requirement
**Broken Code:**
```python
data = {"name": "Alice"}
print(data["age"])
```
**Task:** The script crashes entirely. Fix it gracefully.
**Errors Explained:** `KeyError`. The key 'age' does not exist. The fix is to use `data.get("age", "Unknown")` which returns a default value instead of crashing.

### ⚠️ Common Mistakes
* **Mistake:** Using a list as a dictionary key (`{[1, 2]: "value"}`).
* **Why it occurs:** Dictionary keys must be hashable and immutable (strings, integers, tuples). Lists can change, so they are banned as keys.

### 📝 Practice Requirements
**Easy (3):**
1. Create a dictionary with 3 key-value pairs representing a car.
2. Add a new key-value pair to the dictionary.
3. Create a tuple with 3 elements and print the second one.
**Medium (3):**
1. Iterate over a dictionary and print keys and values neatly.
2. Merge two dictionaries together.
3. Unpack a tuple into three distinct variables.
**Challenging (2):**
1. Write a program to count the frequency of each character in a string using a dictionary.
2. Sort a list of dictionaries based on a specific key inside them (e.g., sorting by age).

---

## 🕒 Topic 9: File Handling Basics (2 Hours)
### 🎯 Learning Outcome
Handle external data, read text, and persist information using file operations.

### 🌍 Real Problem
Variables exist in RAM. When a script finishes, RAM is cleared. If you write an app that tracks daily expenses, you must save that data to the hard drive (a file) so it survives reboots.

### 🧠 Concept Explanation
* **`open()` function:** Connects Python to a file on the OS.
* **File Modes:** `r` (read), `w` (write - overwrites), `a` (append - adds to bottom).
* **Context Manager (`with`):** Automatically closes the file, preventing memory leaks and OS locks.

### 💻 Live Code Example
```python
with open("log.txt", "a") as file:
    file.write("System started.\n")

with open("log.txt", "r") as file:
    print(file.read())
```

### 🐞 Debugging Requirement
**Broken Code:**
```python
f = open("data.txt", "r")
f.write("Hello")
f.close()
```
**Task:** Why doesn't the word "Hello" save to the file?
**Errors Explained:** `UnsupportedOperation`. The file was opened in read mode (`'r'`), which explicitly locks out writing permissions. Change it to `'w'` or `'a'`.

### ⚠️ Common Mistakes
* **Mistake:** Forgetting to close the file using `f.close()`.
* **Why it occurs:** If a script crashes before `.close()` is called, the file remains locked. Using the `with` keyword solves this permanently.

### 📝 Practice Requirements
**Easy (3):**
1. Write "Hello World" to a text file.
2. Read the contents of that exact text file and print them.
3. Append your name to the bottom of the same file.
**Medium (3):**
1. Read a file line by line and store each line as an item in a Python list.
2. Write a script that counts the total number of lines in a text file.
3. Copy the contents of one file to a completely new file.
**Challenging (2):**
1. Read a text file, count the occurrences of each word, and print the top 3 most common words.
2. Read a simple CSV file manually using Python file handling and `.split(',')`.
