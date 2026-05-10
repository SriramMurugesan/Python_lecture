# ==========================================
# 📘 Day 3: Data Structures & File Handling
# ==========================================

# ---------------------------------------------------------
# 🕒 Topic 7: Lists
# ---------------------------------------------------------
print("--- Topic 7: Live Code ---")
cart = ["apple", "banana"]
cart.append("orange")
cart.remove("banana")
for item in cart:
    print(f"To buy: {item}")

print("\n--- Topic 7: Debugging Requirement ---")
# Broken Code:
# nums = [10, 20, 30]
# print(nums[3])
print("Fix: Python is 0-indexed. Maximum index for a 3-item list is 2.")

# ---------------------------------------------------------
# 🕒 Topic 8: Dictionaries & Tuples
# ---------------------------------------------------------
print("\n--- Topic 8: Live Code ---")
coords = (10.5, 20.2) # Tuple

student = {"name": "John", "age": 20}
student["grade"] = "A" # Adding a new key
for key, val in student.items():
    print(f"{key}: {val}")

print("\n--- Topic 8: Debugging Requirement ---")
# Broken Code:
# data = {"name": "Alice"}
# print(data["age"])
print("Fix: Use .get() to prevent KeyErrors -> data.get('age', 'Unknown')")
data = {"name": "Alice"}
print(data.get("age", "Unknown"))

# ---------------------------------------------------------
# 🕒 Topic 9: File Handling Basics
# ---------------------------------------------------------
print("\n--- Topic 9: Live Code ---")
file_name = "log.txt"
with open(file_name, "a") as file:
    file.write("System started.\n")

with open(file_name, "r") as file:
    print(file.read())

print("\n--- Topic 9: Debugging Requirement ---")
# Broken Code:
# f = open("data.txt", "r")
# f.write("Hello")
# f.close()
print("Fix: Change mode from 'r' (read) to 'w' or 'a' to allow writing.")
