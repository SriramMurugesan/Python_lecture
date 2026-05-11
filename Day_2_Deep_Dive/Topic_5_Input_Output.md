# Topic 5: Input and Output Functions

## The input() Function
To make your programs interactive, you need to accept data from the user. Python provides the `input()` function to pause the program, display a message, and wait for the user to type something and press Enter.

### Everything is a String
It is critical to remember that `input()` ALWAYS returns a string (text), even if the user types a number. If you ask a user for their age and they type 25, Python sees it as the text "25", not the math number 25.

### Casting Input
Because input is always text, you cannot perform math on it right away. You must convert (cast) the string into an integer (`int`) or a decimal number (`float`).
Example: `int(input("Enter age: "))` takes the user's text and immediately turns it into a real number.

## The print() Function
We use `print()` to display output to the screen. While it seems simple, it has a few hidden features:
- Separating Items: You can print multiple items by separating them with commas. Python will automatically add a space between them.
- Custom Separator: You can control the separator space by using the `sep` argument.
- Custom Ending: By default, `print()` adds a new line (Enter key) at the end. You can change this behavior to keep the next print on the same line using the `end` argument.
