# topic_4_example.py
# A massive deep dive into all string operations and methods!

text = "Python Programming is fun!"

print("--- Membership Operators ---")
print("Is 'Python' in our text?", "Python" in text)
print("Is 'Java' in our text?", "Java" in text)
print("Is 'Java' NOT in our text?", "Java" not in text)

print("\n--- Finding and Counting ---")
print("Length of string:", len(text))
print("Count of 'm':", text.count("m"))
print("Find 'Program':", text.find("Program"))
print("Index of 'Program':", text.index("Program"))

print("\n--- Changing Case ---")
message = "hElLo WoRlD"
print("Original:", message)
print("Upper:", message.upper())
print("Lower:", message.lower())
print("Capitalize:", message.capitalize())
print("Title:", message.title())
print("Swapcase:", message.swapcase())

print("\n--- Checking Content (True/False) ---")
word1 = "Python3"
word2 = "12345"
word3 = "hello"
print(f"Does '{text}' start with 'Python'?", text.startswith("Python"))
print(f"Is '{word1}' alphanumeric (letters/numbers)?", word1.isalnum())
print(f"Is '{word1}' only letters?", word1.isalpha())
print(f"Is '{word2}' only numbers?", word2.isdigit())
print(f"Is '{word3}' completely lowercase?", word3.islower())

print("\n--- Modifying and Formatting ---")
dirty_text = "   too many spaces   "
print("Cleaned text:", dirty_text.strip())
print("Replaced text:", text.replace("fun", "awesome"))

number_str = "42"
print("Padded with zeros (zfill):", number_str.zfill(5))

print("\n--- Splitting and Joining ---")
csv_data = "apple,banana,orange"
# Split breaks it into a list
fruits_list = csv_data.split(",")
print("Split into a list:", fruits_list)

# Join glues it back together with a different separator
joined_text = " | ".join(fruits_list)
print("Joined back together:", joined_text)

print("\n--- f-strings ---")
name = "Alice"
score = 95
print(f"Player {name} achieved a score of {score}.")
