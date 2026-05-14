class InsufficientFundsError(Exception):
    pass

class InvalidCurrencyError(Exception):
    pass


def process_withdrawal(balance, amount, currency):
    if type(amount) is not int and type(amount) is not float:
        raise TypeError("Amount must be a number.")
        
    if amount < 0:
        raise ValueError("Cannot withdraw a negative amount.")

    if currency != "USD":
        raise InvalidCurrencyError(f"Currency '{currency}' is not supported. Use USD.")

    if amount > balance:
        raise InsufficientFundsError(f"Cannot withdraw {amount}. Current balance is {balance}.")

    new_balance = balance - amount
    return new_balance


def simulate_atm_transaction(user_balance, user_input_amount, user_input_currency):
    try:
        amount_to_withdraw = float(user_input_amount)
        print(f"Attempting to withdraw {amount_to_withdraw} {user_input_currency}...")
        
        final_balance = process_withdrawal(user_balance, amount_to_withdraw, user_input_currency)
        
    except ValueError as e:
        print(f"Data Error: {e}")
        
    except TypeError as e:
        print(f"Type Error: {e}")
        
    except InvalidCurrencyError as e:
        print(f"Currency System Error: {e}")
        
    except InsufficientFundsError as e:
        print(f"Transaction Declined: {e}")
        
    except Exception as e:
        print(f"An unexpected critical system error occurred: {e}")
        
    else:
        print(f"Success! Please take your cash. Your new balance is {final_balance}.")
        
    finally:
        print("Closing secure connection to bank server.\n")


simulate_atm_transaction(500, 100, "USD")

simulate_atm_transaction(500, 600, "USD")

simulate_atm_transaction(500, -50, "USD")

simulate_atm_transaction(500, 100, "EUR")

simulate_atm_transaction(500, "one hundred", "USD")
