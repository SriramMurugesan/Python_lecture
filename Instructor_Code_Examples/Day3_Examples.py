# ==========================================
# DAY 3: DATA STRUCTURES & FILES
# ==========================================

# --- Topic 7: Lists ---
print("--- Topic 7: Lists ---")
fruits = ["Apple", "Banana", "Cherry"]
print(f"Original List: {fruits}")

fruits.append("Orange")
print(f"After Append: {fruits}")

fruits.remove("Banana")
print(f"After Remove: {fruits}")

fruits.sort()
print(f"Sorted: {fruits}\n")

# --- Topic 8: Dictionaries & Tuples ---
print("--- Topic 8: Dicts & Tuples ---")
coordinates = (10.5, 20.8) # Tuple (Immutable)
print(f"Tuple: {coordinates}")

student = {"name": "John", "age": 20, "grade": "A"}
print(f"Dictionary: {student}")
print(f"Accessing Name: {student['name']}")
print(f"Safe Access (get): {student.get('phone', 'No Phone Found')}\n")

print("Iterating over Dictionary:")
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")

# --- Topic 9: File Handling ---
print("\n--- Topic 9: File Handling ---")
file_name = "demo_log.txt"

# Writing to a file using 'with' context manager
with open(file_name, "w") as file:
    file.write("System started.\n")
    file.write("User logged in.\n")

# Reading from a file
with open(file_name, "r") as file:
    content = file.read()
    print(f"File Contents of {file_name}:\n{content}")
