# topic_5_example.py
# Examples of getting user input and formatting output.

print("--- The print() Function Features ---")
# Printing multiple items together
print("Word 1", "Word 2", "Word 3")

# Changing the separator (instead of a space, use a custom symbol)
print("Apple", "Banana", "Cherry", sep=" | ")

# Changing the ending (preventing a new line so the next print connects)
print("This is on ", end="")
print("the same line.")

print("\n--- Getting User Input ---")
# Getting basic text input
user_name = input("Please enter your name: ")
print(f"Hello, {user_name}! Welcome to Day 2.")

# Getting numeric input
print("\nWe need your birth year to do some math.")
# We wrap input() inside int() to convert the text to a math number immediately
birth_year_text = input("What year were you born? ")
birth_year = int(birth_year_text)

# Now we can safely do math with the variable
current_year = 2026
age = current_year - birth_year

print(f"Based on my math, you are turning {age} years old this year.")
