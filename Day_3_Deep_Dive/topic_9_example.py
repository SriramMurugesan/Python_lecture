# topic_9_example.py
# Examples of Writing, Appending, and Reading files using the 'with' block.

print("--- 1. Writing to a File ---")
# Using "w" mode completely overwrites the file or creates a new one
with open("my_data.txt", "w") as file:
    file.write("This is line 1.\n") # \n creates a new line
    file.write("This is line 2.\n")
    print("Successfully created and wrote text to 'my_data.txt'!")

print("\n--- 2. Appending to a File ---")
# Using "a" mode adds to the end safely without erasing the old text
with open("my_data.txt", "a") as file:
    file.write("This is line 3 (Appended later!).\n")
    print("Successfully appended a new line to 'my_data.txt'!")

print("\n--- 3. Reading from a File ---")
# Using "r" mode is strictly for reading
with open("my_data.txt", "r") as file:
    # Read the entire file contents into a single text variable
    content = file.read()
    print("Here is what the file contains:")
    print("-------------------------------")
    print(content)
    print("-------------------------------")

print("\n--- 4. Reading Line by Line (Into a List) ---")
with open("my_data.txt", "r") as file:
    # readlines() returns a Python list where each item is a line
    lines_list = file.readlines()
    print("File read directly into a list format:")
    print(lines_list)
