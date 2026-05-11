# Topic 4: String Operations (Comprehensive)

## Understanding Strings
A string is a sequence of characters enclosed in single or double quotes. Text processing is a massive part of programming, and Python makes it incredibly easy.

## Membership Operators: `in` and `not in`
You can easily check if a specific word or character exists inside a string without needing complex code.
- `"x" in "xyz"` -> True
- `"a" not in "xyz"` -> True

## String Indexing and Slicing
Python uses zero-based indexing, meaning the first character is at index 0.
- `string[0]`: First character.
- `string[-1]`: Last character (negative indexing).
- `string[start:stop:step]`: Slicing. Extracts from `start` up to (but not including) `stop`.

## Comprehensive String Methods
Since a string is a specific data type, it has built-in actions called "methods". Here is a complete list of the most important string methods:

### Finding and Counting
- `len(string)`: Function returning total number of characters.
- `count(substring)`: Counts occurrences of a substring.
- `find(substring)`: Returns the starting index of a substring. Returns `-1` if not found.
- `index(substring)`: Like `find()`, but crashes (throws an error) if the substring is not found.

### Changing Case
- `upper()` / `lower()`: Converts to all uppercase / lowercase.
- `capitalize()`: Capitalizes ONLY the very first letter of the string.
- `title()`: Capitalizes the first letter of EVERY word.
- `swapcase()`: Swaps uppercase to lowercase, and lowercase to uppercase.

### Checking String Content (Returns True/False)
- `startswith(prefix)` / `endswith(suffix)`: Checks if string starts/ends with a specific value.
- `isalpha()`: True if ALL characters are letters (no spaces or numbers).
- `isdigit()`: True if ALL characters are numbers.
- `isalnum()`: True if ALL characters are letters or numbers (alphanumeric).
- `islower()` / `isupper()`: True if all text is lowercase/uppercase.

### Modifying and Formatting
- `strip()`: Removes leading and trailing whitespaces.
- `replace(old, new)`: Swaps a specific part of the text with new text.
- `zfill(width)`: Adds zeros to the beginning of a string until it reaches the specified length (great for formatting numbers).

### Splitting and Joining
- `split(separator)`: Breaks a string into a list of words.
- `join(list)`: Glues a list of strings together into one string using a separator.

## String Formatting (f-strings)
By placing an `f` before the quotes, you can place variables directly inside curly braces `{}`.
