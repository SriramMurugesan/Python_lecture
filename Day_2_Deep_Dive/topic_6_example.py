# topic_6_example.py
# Examples of for loops, while loops, and loop control statements.

print("--- The For Loop ---")
print("Counting to 5 using range(1, 6):")
for number in range(1, 6):
    print("Number:", number)

print("\nIterating through a string one letter at a time:")
word = "Code"
for letter in word:
    print("Letter:", letter)

print("\n--- The While Loop ---")
counter = 3
print("Starting countdown...")
while counter > 0:
    print(counter)
    # Important: We must decrease the counter so the loop eventually stops!
    counter = counter - 1  
print("Go!")

print("\n--- Break and Continue ---")
print("Using 'break' to stop early when we hit 5:")
for number in range(1, 10):
    if number == 5:
        print("Hit number 5, breaking the loop!")
        break
    print(number)

print("\nUsing 'continue' to skip the number 3:")
for number in range(1, 6):
    if number == 3:
        print("Skipping number 3!")
        continue
    print(number)

print("\n--- Nested Loops ---")
print("An outer loop running 2 times, and an inner loop running 3 times:")
for outer in range(1, 3):
    for inner in range(1, 4):
        print(f"Outer Loop cycle: {outer} | Inner Loop cycle: {inner}")
