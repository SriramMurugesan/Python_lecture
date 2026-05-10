# ==========================================
# 📘 Day 2: Control Flow & Text Processing
# ==========================================

# ---------------------------------------------------------
# 🕒 Topic 4: String Operations
# ---------------------------------------------------------
print("--- Topic 4: Live Code ---")
email = "admin@company.com"
username = email[:email.index("@")]
print(f"Welcome, {username.capitalize()}!")

print("\n--- Topic 4: Debugging Requirement ---")
# Broken Code:
# name = "python"
# name[0] = "P"
print("Fix: Strings are immutable. Reassign using methods -> name = name.capitalize()")
name = "python"
name = name.capitalize()
print(f"Fixed Name: {name}")

# ---------------------------------------------------------
# 🕒 Topic 5: Input/Output Functions
# ---------------------------------------------------------
print("\n--- Topic 5: Live Code ---")
# Uncomment for live input demo:
# name_input = input("Enter name: ")
# salary_input = float(input("Enter salary: "))
name_input = "Alice"
salary_input = 85000.75
print("User", name_input, sep=" -> ")
print(f"Formatted salary: ${salary_input:,.2f}")

print("\n--- Topic 5: Debugging Requirement ---")
# Broken Code:
# age = input("Age: ")
# print("In 5 years, you will be:", age + 5)
print("Fix: input() returns a string. Cast it -> int(input('Age: '))")

# ---------------------------------------------------------
# 🕒 Topic 6: Loops in Python
# ---------------------------------------------------------
print("\n--- Topic 6: Live Code ---")
for i in range(1, 4):
    print(f"Attempt {i}...")

text = "pYthOn"
for char in text:
    if char.isupper():
        print(f"Uppercase found: {char}")

print("\n--- Topic 6: Debugging Requirement ---")
# Broken Code (Infinite loop):
# count = 5
# while count > 0:
#     print(count)
print("Fix: Decrement the counter inside the loop -> count -= 1")
count = 5
while count > 0:
    print(count)
    count -= 1 # The Fix
