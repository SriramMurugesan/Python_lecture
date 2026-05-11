# Topic 7: Lists in Python

## What is a List?
Variables hold a single piece of data. But what if you have 100 students? You can't create 100 separate variables. 
A **List** is a collection that allows you to store multiple items in a single variable. Lists are ordered, changeable (mutable), and allow duplicate values.
- Lists are created using square brackets: `[1, 2, 3]`

## Indexing and Slicing
Lists work exactly like Strings when it comes to positions! 
- Zero-based indexing: The first item is at index 0.
- You can slice lists just like strings to grab a chunk of items: `my_list[0:3]`.

## Modifying Lists
Because lists are changeable, you can modify an item directly by accessing its index.
- `my_list[0] = "New Value"` completely replaces the first item in the list.

## Essential List Methods
- `append(item)`: Adds a single item to the very end of the list.
- `insert(index, item)`: Inserts an item at a specific position, pushing everything else over.
- `remove(item)`: Removes the first occurrence of a specific value.
- `pop(index)`: Removes and returns the item at a specific index (or the very last item if index is left empty).
- `clear()`: Empties the entire list.
- `sort()`: Sorts the list in ascending order (permanently changes the list).
- `reverse()`: Reverses the order of the list (permanently changes the list).
- `count(item)`: Counts how many times an item appears in the list.
- `index(item)`: Finds the position of the first occurrence of an item.
