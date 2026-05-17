# Topic 15b: Regular Expressions (Regex) in Python

## What is Regex?
Regular Expressions (Regex or RE) are sequences of characters that define a search pattern. They are extremely powerful for string matching, searching, extracting, and replacing text based on specific rules.

## The `re` Module
Python has a built-in module called `re` to work with regular expressions.

```python
import re
```

## Common Regex Functions
- `re.search()`: Searches the string for a match, and returns a Match object if there is a match anywhere in the string.
- `re.findall()`: Returns a list containing all matches.
- `re.sub()`: Replaces one or many matches with a string.
- `re.match()`: Checks for a match only at the beginning of the string.

## Common Metacharacters
- `\d`: Returns a match where the string contains digits (numbers from 0-9).
- `\w`: Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character).
- `\s`: Returns a match where the string contains a white space character.
- `.`: Any character (except newline character).
- `^`: Starts with.
- `$`: Ends with.
