# topic_8_example.py
# Working with Dictionaries and Tuples

print("--- Dictionaries ---")
# Creating a dictionary with key-value pairs
student = {
    "name": "Alice",
    "age": 22,
    "course": "Python"
}
print("Full Dictionary:", student)

# Accessing values using their keys instead of indexes
print("Student's Name:", student["name"])
print("Student's Age:", student["age"])

# Adding a brand new key-value pair
student["grade"] = "A"
print("After adding a new grade key:", student)

# Updating an existing value
student["age"] = 23
print("After updating age to 23:", student)

print("\n--- Dictionary Methods ---")
print("All Keys:", student.keys())
print("All Values:", student.values())
print("All Items (Pairs):", student.items())

# Removing an item
removed_value = student.pop("course")
print("After removing 'course':", student)
print("The value that was removed:", removed_value)

print("\n--- Tuples ---")
# Creating a tuple (immutable/unchangeable data)
dimensions = (1920, 1080)
print("Screen Dimensions:", dimensions)

# Accessing tuple items works exactly like a list
print("Width (index 0):", dimensions[0])
print("Height (index 1):", dimensions[1])

# NOTE: We CANNOT do dimensions[0] = 2000. That would crash the program because tuples are locked!

# Tuple Methods
colors = ("red", "green", "red", "blue")
print("\nColors tuple:", colors)
print("Count of 'red':", colors.count("red"))
print("Index of 'green':", colors.index("green"))
