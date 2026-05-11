# Topic 6: Loops in Python

## Why do we need Loops?
Programming is about automating repetitive tasks. If you need to do the exact same action 100 times, you shouldn't write the same code 100 times. Loops allow you to repeat a block of code efficiently and dynamically.

## The For Loop
A `for` loop is used to iterate over a sequence (like a string of characters, or a list of numbers). It runs a specific, known number of times.
- `range(stop)`: Generates numbers starting from 0 up to, but not including, the stop number.
- `range(start, stop)`: Generates numbers from start up to stop.
- `range(start, stop, step)`: Generates numbers with a specific gap or step size.

## The While Loop
A `while` loop runs as long as a certain condition remains `True`. You must be very careful to update the condition inside the loop; otherwise, the condition will never become `False`, and the loop will run forever (this is called an infinite loop).

## Loop Control: Break and Continue
Sometimes you need to interrupt a loop based on a specific situation.
- `break`: Completely stops and destroys the loop immediately, moving on to the rest of the program.
- `continue`: Skips the rest of the current loop cycle and jumps directly back to the top to start the next iteration.

## Nested Loops
You can put a loop inside another loop. This is called nesting. The "inner loop" will finish all of its repetitions for every single repetition of the "outer loop". For example, if an outer loop runs 3 times and an inner loop runs 5 times, the inner code will execute 15 times total.
