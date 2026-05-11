# topic_16_example.py
# Advanced Exceptions: Multiple Excepts, Finally, and Custom Classes.

print("--- 1. Multiple Except Blocks ---")
# Imagine getting input from a user on a website
user_input = "0"

try:
    print("Trying to convert input to a number and divide 100 by it...")
    # This might fail if user_input is a text word!
    number = int(user_input)
    
    # This might fail if the user_input is exactly 0!
    result = 100 / number
    print("Result is:", result)

except ValueError:
    print("ERROR CAUGHT: You must type a valid number, not text!")
except ZeroDivisionError:
    print("ERROR CAUGHT: You cannot mathematically divide by zero!")

print("\n--- 2. The 'finally' Block ---")
try:
    print("Opening a highly secure database...")
    # Simulating a massive crash reading the file
    crash = 1 / 0
except ZeroDivisionError:
    print("ERROR: Something went horribly wrong while reading the data!")
finally:
    # This runs no matter what happens!
    print("FINALLY: Forcefully closing the secure connection to prevent data leaks.")

print("\n--- 3. Custom Error Classes ---")
# Creating a brand new custom error specifically for our banking program
class BankBalanceError(Exception):
    pass # 'pass' just tells Python "do nothing else, the setup is complete"

account_balance = 50
withdrawal_amount = 100

print(f"Attempting to withdraw ${withdrawal_amount} from an account with ${account_balance}...")

# If you remove the hashtags below, it will raise OUR custom error!
# if withdrawal_amount > account_balance:
#     raise BankBalanceError("CRITICAL: You do not have enough money in your account!")

print("Withdrawal successful!")
