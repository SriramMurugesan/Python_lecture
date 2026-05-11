# topic_14_example.py
# Examples of Syntax and Runtime errors. 
# NOTE: The errors are commented out with hashtags so this script doesn't crash!

print("--- Understanding Errors ---")
print("Programming is 10% writing code and 90% fixing errors.")

# 1. Syntax Error Example (Grammar mistake)
# If you remove the hashtag below, the whole script refuses to run at all.
# print("Hello World)  <-- MISSING ENDING QUOTE!

# 2. Runtime Error: ZeroDivisionError
# The grammar is fine, but math rules are broken.
# crash_number = 10 / 0  <-- YOU CANNOT DIVIDE BY ZERO!

# 3. Runtime Error: NameError
# Using a variable that you never actually created.
# print(mystery_variable)  <-- Python doesn't know what this is!

# 4. Runtime Error: TypeError
# Trying to mix text and numbers without casting them properly.
# total = "50" + 10  <-- Python cannot mathematically add text and a number!

print("\n--- Debugging with Print Statements ---")
print("Step 1 started...")
x = 10
print("Step 1 finished successfully! x is", x)

print("Step 2 started...")
y = 5
print("Step 2 finished successfully! y is", y)

# If the code magically crashed right here, the print statements above 
# would prove to us without a shadow of a doubt that Step 1 and 2 worked perfectly!
