# topic_15b_example.py
# Using the re module for pattern matching and string manipulation

import re

print("--- 1. Searching for a Pattern ---")
text = "The quick brown fox jumps over 42 hurdles."

# Search for the word 'fox'
match = re.search(r"fox", text)
if match:
    print(f"Found '{match.group()}' at index {match.start()} to {match.end()}.")
else:
    print("Pattern not found.")

print("\n--- 2. Finding All Matches ---")
# Find all digits in the text
digits = re.findall(r"\d", text)
print(f"All digits found: {digits}")
# To find a number (multiple digits)
number = re.findall(r"\d+", text)
print(f"Full numbers found: {number}")

print("\n--- 3. Replacing Text ---")
# Replace all spaces with a dash
replaced_text = re.sub(r"\s", "-", text)
print(f"Replaced string: {replaced_text}")

print("\n--- 4. Validating Formats (e.g. Email) ---")
email = "student@example.com"
# Simple regex to check if it looks like an email
pattern = r"^\w+@\w+\.\w+$"
if re.search(pattern, email):
    print(f"'{email}' is a valid email format.")
else:
    print(f"'{email}' is invalid.")
