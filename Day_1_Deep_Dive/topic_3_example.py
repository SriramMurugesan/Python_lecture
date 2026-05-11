# topic_3_example.py
# Examples of variables, data types, operators, and type casting.

print("--- Variables and Data Types ---")
user_name = "Alice"       # String (text)
age = 28                  # Integer (whole number)
account_balance = 150.75  # Float (decimal number)
is_active = True          # Boolean (True or False)

print("Name:", user_name)
print("Age:", age)
print("Balance:", account_balance)
print("Active Account:", is_active)

print("\n--- Arithmetic Operators ---")
x = 10
y = 3
print("Variables: x = 10, y = 3")
print("Addition (x + y):", x + y)
print("Division (x / y):", x / y)
print("Floor Division (x // y):", x // y)
print("Modulo/Remainder (x % y):", x % y)

print("\n--- Logical Operators ---")
has_money = True
has_time = False
print("Has money?", has_money)
print("Has time?", has_time)
print("Can go to movies? (has_money and has_time):", has_money and has_time)

print("\n--- Type Casting ---")
string_number = "50"
real_number = 10

print("We have a string number '50' and an integer 10.")
# We must convert the string to an integer before adding them together
total = int(string_number) + real_number
print("Total after type casting int('50') + 10:", total)
