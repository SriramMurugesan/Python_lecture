# ==========================================
# DAY 1: FOUNDATIONS & SETUP
# ==========================================

# --- Topic 1 & 2: Introduction and Setup ---
print("--- Topic 1 & 2 ---")
print("Hello, Python Developer!")
print("Welcome to Day 1 of Python Training.\n")

# --- Topic 3: Variables, Data Types & Operators ---
print("--- Topic 3: Variables & Data Types ---")
age = 25              # Integer
price = 19.99         # Float
is_active = True      # Boolean
name = "Alice"        # String

print(f"Name: {name}, Age: {age}, Price: {price}, Active: {is_active}")
print(f"Type of age: {type(age)}\n")

print("--- Operators ---")
print(f"10 + 3 = {10 + 3}")
print(f"10 / 3 = {10 / 3}")
print(f"10 // 3 = {10 // 3} (Integer Division)")
print(f"10 % 3 = {10 % 3} (Modulo/Remainder)\n")

print("--- Type Casting ---")
# string_num = "10" + 5  # This causes a TypeError!
string_num = "10"
print(f"String '10' + 5 = {int(string_num) + 5}")
