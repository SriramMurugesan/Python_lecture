# ==========================================
# 📘 Day 1: Foundations & Setup
# ==========================================

# ---------------------------------------------------------
# 🕒 Topic 1: Introduction to Python & Git Workflow
# ---------------------------------------------------------
print("--- Topic 1: Live Code ---")
print("Welcome to the Python Development Team!")

print("\n--- Topic 1: Debugging Requirement ---")
print("Broken Code (Bash): git commit 'Added new feature'")
print("Fix: git commit -m 'Added new feature'")

# ---------------------------------------------------------
# 🕒 Topic 2: Python Installation & Setup
# ---------------------------------------------------------
print("\n--- Topic 2: Live Code ---")
def solve_problem(steps):
    print(f"Executing step: {steps}")
solve_problem("1. Understand 2. Pseudocode 3. Code")

print("\n--- Topic 2: Debugging Requirement ---")
print("Broken Code (Bash): python script")
print("Fix: python script.py")

# ---------------------------------------------------------
# 🕒 Topic 3: Variables, Data Types & Operators
# ---------------------------------------------------------
print("\n--- Topic 3: Live Code ---")
age = 25
balance = 100.50
is_active = True
print(f"Age + 5 = {age + 5}")
print(f"Is balance > 50 and active? {balance > 50 and is_active}")

print("\n--- Topic 3: Debugging Requirement ---")
# Broken Code:
# total = "10" + 5
# print(total)
print("Fix: Explicitly cast the string to an integer -> int('10') + 5")
total = int("10") + 5
print(f"Fixed Total: {total}")
