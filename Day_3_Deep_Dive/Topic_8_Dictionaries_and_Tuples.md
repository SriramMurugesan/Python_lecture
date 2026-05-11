# Topic 8: Dictionaries & Tuples

## Dictionaries
While Lists use numbers (indexes) to organize data, **Dictionaries** use "Keys" and "Values". Think of a real dictionary: you look up a word (the Key) to find its definition (the Value).
- Created with curly braces `{}` and colons `:`.
- Example: `student = {"name": "John", "age": 20}`
- Keys must be unique and are usually text strings. Values can be anything at all (numbers, strings, even lists!).

### Accessing and Modifying Dictionaries
- Access a value: `student["name"]`
- Add or update a value: `student["grade"] = "A"`. If the key doesn't exist yet, Python creates it. If it already exists, Python overwrites it with the new value.

### Dictionary Methods
- `keys()`: Returns a list of all the keys in the dictionary.
- `values()`: Returns a list of all the values in the dictionary.
- `items()`: Returns key-value pairs. This is incredibly useful for loops!
- `pop(key)`: Removes a specific key-value pair based on its key.

---

## Tuples
A **Tuple** is incredibly similar to a List, but with one massive difference: it is **Immutable** (unchangeable). Once you create a tuple, you cannot add, remove, or change its items under any circumstances.
- Created with parentheses `()`.
- Example: `coordinates = (10, 20)`

### Why use Tuples?
1. **Safety**: If you have data that should NEVER change (like days of the week, or geographic map coordinates), using a tuple prevents accidental code bugs from modifying it.
2. **Speed**: Tuples are slightly faster for the computer to process than lists because their size is locked.

### Tuple Operations
Because they cannot be changed, tuples only have two methods:
- `count(item)`: Counts how many times an item appears.
- `index(item)`: Finds the position of an item.
