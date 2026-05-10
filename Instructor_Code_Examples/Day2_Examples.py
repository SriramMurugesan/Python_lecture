# ==========================================
# DAY 2: CONTROL FLOW & TEXT PROCESSING
# ==========================================

# --- Topic 4: String Operations ---
print("--- Topic 4: Strings ---")
text = "Python Programming"
print(f"Original: {text}")
print(f"First char [0]: {text[0]}")
print(f"Slice [0:6]: {text[0:6]}")
print(f"Reverse [::-1]: {text[::-1]}")
print(f"Uppercase: {text.upper()}")
print(f"Replace: {text.replace('Python', 'Java')}\n")

# --- Topic 5: Input & Output ---
print("--- Topic 5: I/O ---")
# Note for Instructor: Uncomment the input lines during live class to show interactiveness.
# user_name = input("Enter your name: ")
# salary = float(input("Enter your salary: "))
user_name = "Alice" # Hardcoded for script demonstration
salary = 75000.50

print("Apple", "Banana", "Cherry", sep=" | ")
print(f"Formatted Salary: ${salary:,.2f}\n")

# --- Topic 6: Loops ---
print("--- Topic 6: Loops ---")
print("For Loop (range 1 to 4):")
for i in range(1, 4):
    print(f"Attempt {i}...")

print("\nWhile Loop:")
count = 3
while count > 0:
    print(count)
    count -= 1
print("Go!")
