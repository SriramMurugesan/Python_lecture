# topic_15_example.py
# Using Try/Except to prevent crashes, and Raising custom errors.

print("--- 1. The Try / Except Block ---")

print("Attempting dangerous math...")
try:
    # This will immediately cause a ZeroDivisionError
    result = 10 / 0
    print("This line will NEVER print because the line above crashed.")
except:
    print("Caught an error! We prevented the whole program from crashing.")

print("\n--- 2. Catching Specific Errors ---")
text_number = "Apple"

try:
    # Trying to turn the word "Apple" into a math number
    converted = int(text_number)
except ValueError:
    print("ValueError Caught: You cannot convert the word 'Apple' into an integer!")
except ZeroDivisionError:
    print("This won't print because it wasn't a division error.")

print("\n--- 3. Raising Your Own Exceptions ---")
# Sometimes you WANT to crash the program if the user breaks a strict rule
age = -5

print(f"Checking if age {age} is valid...")

# If you uncomment the lines below, the program will act as a security guard and intentionally crash!
# if age < 0:
#     raise ValueError("CRITICAL ERROR: Age cannot be a negative number!")

print("If the age was valid, the program continues running normally.")
