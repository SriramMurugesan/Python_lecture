# topic_7_example.py
# Examples of creating, slicing, modifying, and using List methods.

print("--- Creating and Accessing Lists ---")
fruits = ["apple", "banana", "cherry", "date"]
print("Original list:", fruits)
print("First fruit (index 0):", fruits[0])
print("Last fruit (index -1):", fruits[-1])
print("Slice of fruits (first two):", fruits[0:2])

print("\n--- Modifying Lists ---")
# Changing the second item
fruits[1] = "blueberry"
print("List after changing index 1 to blueberry:", fruits)

print("\n--- List Methods: Adding Items ---")
# Append adds to the end
fruits.append("elderberry")
print("After append('elderberry'):", fruits)

# Insert places an item at a specific index
fruits.insert(1, "orange")
print("After insert(1, 'orange'):", fruits)

print("\n--- List Methods: Removing Items ---")
# Remove deletes by matching the text value
fruits.remove("cherry")
print("After remove('cherry'):", fruits)

# Pop deletes by index (removes the last item by default)
popped_item = fruits.pop()
print("After pop() (removed the last item):", fruits)
print("The actual item that was removed:", popped_item)

print("\n--- List Methods: Sorting and Reversing ---")
numbers = [42, 8, 15, 23, 4, 16]
print("Original numbers:", numbers)

# Sort changes the list permanently
numbers.sort()
print("After sort() (ascending order):", numbers)

# Reverse flips the list permanently
numbers.reverse()
print("After reverse() (backwards):", numbers)

print("\n--- Finding Data in Lists ---")
print("Count of 'apple' in fruits:", fruits.count("apple"))
print("Index of 'orange' in fruits:", fruits.index("orange"))
